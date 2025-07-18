from torch.utils.data import Dataset
import pandas as pd
from PIL import Image
import os


class CarDamageDataset(Dataset):
    def __init__(self, csv_file, img_dir, transform=None):
        self.data = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.transform = transform

        # Create label → index mapping
        self.label2idx = {label: idx for idx, label in enumerate(self.data['classes'].unique())}
        self.idx2label = {v: k for k, v in self.label2idx.items()}

        # Precompute numerical labels
        self.data['label_idx'] = self.data['classes'].map(self.label2idx)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        img_path = os.path.join(self.img_dir, os.path.basename(row['image']))
        image = Image.open(img_path).convert("RGB")
        label = row['label_idx']

        if self.transform:
            image = self.transform(image)

        return image, label