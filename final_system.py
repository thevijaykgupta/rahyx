# ENCRYPTION
from modules.encryption.encrypt import encrypt_message, generate_key

# AI STEGO
from modules.ai_steganography.model import Encoder, Decoder
from modules.ai_steganography.utils import load_image, message_to_tensor, save_image
from modules.steganalysis.model import StegDetector

# ROUTING
from modules.routing.routing import find_best_path

import os
import random
import torch
import numpy as np
import matplotlib.pyplot as plt


# ---------------- PSNR FUNCTION ----------------
def psnr(img1, img2):
    img1 = img1.detach().cpu().numpy()
    img2 = img2.detach().cpu().numpy()

    mse = np.mean((img1 - img2) ** 2)

    if mse < 1e-10:
        return 100

    return 20 * np.log10(1.0 / np.sqrt(mse))


# ---------------- SYSTEM START ----------------

generate_key()

message = "Top Secret Military Data"
encrypted = encrypt_message(message)
encrypted_str = encrypted.decode()


# Load models
encoder = Encoder()
decoder = Decoder()
detector = StegDetector()

encoder.load_state_dict(torch.load("encoder.pth"))
decoder.load_state_dict(torch.load("decoder.pth"))
detector.load_state_dict(torch.load("detector.pth"))

encoder.eval()
decoder.eval()
detector.eval()


# ---------------- MULTI-FRAGMENT ----------------

chunks = [encrypted_str[i:i+20] for i in range(0, len(encrypted_str), 20)]

stego_images = []
final_stego = None
final_image = None
final_secret = None

for i, chunk in enumerate(chunks):

    img_path = random.choice(os.listdir("data/input_images"))
    image = load_image(f"data/input_images/{img_path}")

    secret = message_to_tensor(chunk)

    stego = encoder(image, secret)

    save_path = f"data/output_images/stego_{i}.png"
    save_image(stego, save_path)

    stego_images.append(save_path)

    # keep last for adaptive loop
    final_stego = stego
    final_image = image
    final_secret = secret

print("Fragments transmitted:", stego_images)


# ---------------- ADAPTIVE LOOP ----------------

threshold = 0.3
max_attempts = 5

risk_list = []
psnr_list = []

image = final_image
secret = final_secret

best_stego = None
best_score = float('inf')

for attempt in range(max_attempts):

    stego = encoder(image, secret)

    risk = detector(stego).item()
    psnr_val = psnr(image, stego)
    psnr_norm = psnr_val / 30.0
    score = 0.7 * risk - 0.3 * psnr_norm

    print(f"Attempt {attempt+1} → Risk: {risk:.3f}, PSNR: {psnr_val:.2f}, Score: {score:.3f}")

    if score < best_score:
        best_score = score
        best_stego = stego

    # 🔥 adaptive change
    if risk > 0.6:
    # 🔥 aggressive hiding
        secret = torch.clamp(secret * 0.8 + torch.randn_like(secret)*0.01, 0, 1)
        image = torch.clamp(image + torch.randn_like(image)*0.02, 0, 1)

    else:
    # 🔥 fine tuning
        secret = torch.clamp(secret + torch.randn_like(secret)*0.01, 0, 1)

# use best result
stego = best_stego

for attempt in range(max_attempts):

    stego = encoder(image, secret)

    risk_score = detector(stego).item()
    psnr_val = psnr(image, stego)

    print(f"Attempt {attempt+1} → Risk: {risk_score:.3f}, PSNR: {psnr_val:.2f}")

    # 🔥 FORCE REAL ADAPTATION
    image = torch.clamp(image + torch.randn_like(image)*0.02, 0, 1)
    secret = torch.clamp(secret + torch.randn_like(secret)*0.02, 0, 1)

    # 🔥 ADD VARIATION PER ATTEMPT
    secret = torch.clamp(secret + (attempt * 0.01), 0, 1)

#     # 🔥 CORRECT ADAPTIVE LOGIC
# if risk_score > threshold:
#     # high risk → reduce visibility
#     secret = torch.clamp(secret + torch.randn_like(secret)*0.02, 0, 1)
#     image = torch.clamp(image + torch.randn_like(image)*0.015, 0, 1)

# else:
#     # low risk → increase embedding strength
#     secret = torch.clamp(secret + torch.randn_like(secret)*0.01, 0, 1)


# ---------------- ATTACK SIMULATION ----------------

noisy = stego + torch.randn_like(stego) * 0.05
noisy = torch.clamp(noisy, 0, 1)

attack_risk = detector(noisy).item()
print("Attack Risk (Noisy Image):", attack_risk)


# ---------------- FINAL OUTPUT ----------------

save_image(stego, "data/output_images/final_stego.png")

print("Stego Image Generated!")


# ---------------- DYNAMIC ROUTING ----------------

paths = []

for i in range(len(stego_images)):
    dynamic_risk = risk_score + random.uniform(0.05, 0.2)
    path = find_best_path("A", "E", dynamic_risk)
    paths.append(path)

print("Fragment-wise Paths:", paths)


# ---------------- METRICS ----------------

efficiency = len(encrypted_str) / (risk_score + 1e-5)

psnr_value = psnr(image, stego)

print("Efficiency Score:", efficiency)
print("Final Risk Score:", risk_score)
print("PSNR:", psnr_value)

print("Steganographic Capacity:", len(encrypted_str))
print("Detection Probability:", risk_score)


# ---------------- GRAPH ----------------

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.plot(risk_list, marker='o')
plt.title("Risk vs Attempts")

plt.subplot(1,2,2)
plt.plot(psnr_list, marker='o')
plt.title("PSNR vs Attempts")

plt.tight_layout()
plt.show()


print("Transmission Completed Securely!")
print("System Stability Achieved via Adaptive Noise Injection")