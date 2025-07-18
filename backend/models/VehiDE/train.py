import torch
from torch.utils.data import DataLoader
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
from dataset import VehiDEDataset
from torchvision import transforms
import torchvision

def get_transform():
    return transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
    ])

def collate_fn(batch):
    return tuple(zip(*batch))

def get_model(num_classes):
    model = maskrcnn_resnet50_fpn(weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)
    mask_in_features = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden = model.roi_heads.mask_predictor.conv5_mask.out_channels
    model.roi_heads.mask_predictor = torchvision.models.detection.mask_rcnn.MaskRCNNPredictor(mask_in_features, hidden, num_classes)
    return model

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_ds = VehiDEDataset(
        image_dir="datasets/VehiDE/image/image/",
        annotation_json="datasets/VehiDE/0Train_via_annos.json",
        transform=get_transform()
    )

    train_loader = DataLoader(train_ds, batch_size=2, shuffle=True, collate_fn=collate_fn)

    num_classes = len(train_ds.class_to_idx) + 1  # +1 for background
    model = get_model(num_classes=num_classes)
    model.to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)

    model.train()
    for epoch in range(10):
        total_loss = 0
        for images, targets in train_loader:
            try:
                images = [img.to(device) for img in images]
                targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

                loss_dict = model(images, targets)
                losses = sum(loss for loss in loss_dict.values())

                optimizer.zero_grad()
                losses.backward()
                optimizer.step()

                total_loss += losses.item()
            except Exception as e:
                print(f"Error during training: {e}")
                continue
        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

    torch.save(model.state_dict(), "maskrcnn_vehide.pth")

if __name__ == "__main__":
    main()
