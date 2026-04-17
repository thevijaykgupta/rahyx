import torch
import torch.nn as nn
import cv2
import numpy as np


# 🔥 ATTENTION BLOCK
class AttentionBlock(nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, in_channels, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return x * self.conv(x)


# 🔴 ENCODER
class Encoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(5, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.attention = AttentionBlock(32)
        self.conv3 = nn.Conv2d(32, 3, 3, padding=1)

        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, image, secret):

        # 🔥 FIXED EDGE EXTRACTION
        img_np = image.detach().cpu().squeeze().permute(1,2,0).numpy()
        img_np = (img_np * 255).clip(0,255).astype(np.uint8)

        edges = cv2.Canny(img_np, 100, 200)

        edge_tensor = torch.tensor(edges / 255.0, dtype=torch.float32)
        edge_tensor = edge_tensor.unsqueeze(0).unsqueeze(0)
        edge_tensor = edge_tensor.to(image.device)

        # CONCAT
        x = torch.cat((image, secret, edge_tensor), dim=1)

        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.attention(x)

        x = self.sigmoid(self.conv3(x))
        x = torch.clamp(x, 0, 1)

        # 🔥 BLENDING (CRITICAL FOR PSNR)
        return 0.85 * image + 0.15 * x


# 🔵 DECODER
class Decoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 1, 3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, stego):
        return self.conv(stego)