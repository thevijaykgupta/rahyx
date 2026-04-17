import cv2
import torch
import os

def load_image(path):
    print("Loading image from:", path)
    print("Exists:", os.path.exists(path))

    img = cv2.imread(path)

    if img is None:
        raise ValueError(f"Image not found or cannot be read: {path}")

    img = cv2.resize(img, (64, 64))
    img = img / 255.0

    img = torch.tensor(img, dtype=torch.float32).permute(2,0,1).unsqueeze(0)

    return img

def message_to_tensor(message):
    binary = ''.join(format(ord(c), '08b') for c in message)

    # pad to fit 64x64
    binary = binary.ljust(64*64, '0')

    data = [int(bit) for bit in binary[:64*64]]

    tensor = torch.tensor(data, dtype=torch.float32)
    tensor = tensor.view(1, 1, 64, 64)

    return tensor

def save_image(tensor, path):
    img = tensor.squeeze(0).permute(1, 2, 0).detach().numpy()
    img = (img * 255).astype('uint8')
    cv2.imwrite(path, img)