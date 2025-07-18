import os
import json
import torch
from torch.utils.data import Dataset
from PIL import Image, ImageFile, ImageDraw
import numpy as np
from torchvision.ops import masks_to_boxes

ImageFile.LOAD_TRUNCATED_IMAGES = True


class VehiDEDataset(Dataset):
    def __init__(self, image_dir, annotation_json, transform=None):
        self.image_dir = image_dir
        self.transform = transform

        with open(annotation_json, 'r') as f:
            self.annotations = json.load(f)

        self.image_ids = list(self.annotations.keys())
        self.class_to_idx = self._build_class_index()

    def _build_class_index(self):
        classes = set()
        for v in self.annotations.values():
            for region in v.get('regions', []):
                classes.add(region['class'])
        class_list = sorted(classes)
        return {cls_name: idx + 1 for idx, cls_name in enumerate(class_list)}  # 0 = background

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, idx):
        while True:
            img_id = self.image_ids[idx]
            ann = self.annotations[img_id]
            img_path = os.path.join(self.image_dir, ann["name"])

            try:
                image = Image.open(img_path).convert("RGB")
                break  # exit loop if loaded successfully
            except (OSError, ValueError) as e:
                print(f"[WARNING] Skipping corrupted image: {img_path} - {e}")
                idx = (idx + 1) % len(self)  # move to next image

        width, height = image.size

        masks = []
        boxes = []
        labels = []

        for region in ann.get("regions", []):
            all_x = region["all_x"]
            all_y = region["all_y"]
            poly = np.array([list(zip(all_x, all_y))], dtype=np.int32)

            mask = np.zeros((height, width), dtype=np.uint8)
            mask = Image.fromarray(mask)
            draw = ImageDraw.Draw(mask)
            draw.polygon(list(zip(all_x, all_y)), outline=1, fill=1)
            mask = np.array(mask)
            masks.append(mask)

            labels.append(self.class_to_idx[region["class"]])

        if masks:
            masks = torch.as_tensor(masks, dtype=torch.uint8)
            boxes = masks_to_boxes(masks)
        else:
            # image with no labeled damage
            masks = torch.zeros((0, height, width), dtype=torch.uint8)
            boxes = torch.zeros((0, 4), dtype=torch.float32)

        target = {
            "boxes": boxes,
            "labels": torch.as_tensor(labels, dtype=torch.int64),
            "masks": masks,
            "image_id": torch.tensor([idx]),
        }

        if self.transform:
            image = self.transform(image)

        return image, target
    

def clean_broken_images(image_dir, dry_run=True):
    bad_images = []
    for f in os.listdir(image_dir):
        try:
            Image.open(os.path.join(image_dir, f)).verify()
        except Exception as e:
            bad_images.append(f)
            print(f"Broken image: {f}, Error: {e}")
    return bad_images


if __name__ == "__main__":
    # Example usage
    dataset = VehiDEDataset(
        image_dir="datasets/VehiDE/image/image/",
        annotation_json="datasets/VehiDE/0Train_via_annos.json"
    )
    
    print(f"Dataset size: {len(dataset)}")
    
    for i in range(len(dataset)):
        image, target = dataset[i]
        print(f"Image {i}: {image.size}, Target: {target}")
