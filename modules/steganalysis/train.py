import os
import random
import torch
import torch.nn as nn
import torch.optim as optim

from modules.steganalysis.model import StegDetector
from modules.ai_steganography.utils import load_image, message_to_tensor
from modules.ai_steganography.model import Encoder

# ---------------- SETUP ----------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = StegDetector().to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.005)

# Load encoder (already trained)
encoder = Encoder().to(device)
encoder.load_state_dict(torch.load("encoder.pth"))
encoder.eval()

# Load dataset
image_files = os.listdir("data/input_images")

# ---------------- TRAINING ----------------

for epoch in range(50):

    # 🔥 RANDOM IMAGE
    img_path = random.choice(image_files)
    image = load_image(f"data/input_images/{img_path}").to(device)

    # 🔥 RANDOM MESSAGE
    msg = str(random.randint(0, 100000))
    secret = message_to_tensor(msg).to(device)

    # 🔥 GENERATE STEGO IMAGE
    stego = encoder(image, secret).detach()

    # 🔥 ADD NOISE (ATTACK SIMULATION)
    noisy = stego + torch.randn_like(stego) * 0.05

    # Labels
    clean_label = torch.zeros((1,1)).to(device)
    stego_label = torch.ones((1,1)).to(device)

    # Predictions
    output_clean = model(image)
    output_stego = model(stego)
    output_noisy = model(noisy)

    # 🔥 FINAL LOSS
    loss = (
        criterion(output_clean, clean_label) +
        criterion(output_stego, stego_label) +
        criterion(output_noisy, stego_label)
    )

    # Backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Save trained detector
torch.save(model.state_dict(), "detector.pth")

print("Detector training completed!")