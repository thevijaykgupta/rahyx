import torch
from model import Encoder, Decoder
from utils import load_image, message_to_tensor, save_image

# Load models
encoder = Encoder()
decoder = Decoder()

encoder.load_state_dict(torch.load("encoder.pth"))
decoder.load_state_dict(torch.load("decoder.pth"))

encoder.eval()
decoder.eval()

# STEP 1: Load real image
image = load_image("data/input_images/input.png")

# STEP 2: Convert message
message = "Secret AI Message"
secret = message_to_tensor(message)

# STEP 3: Encode
stego = encoder(image, secret)

# STEP 4: Save stego image
save_image(stego, "data/output_images/ai_stego.png")

# STEP 5: Decode
recovered = decoder(stego)

print("Stego image saved!")

# # Test data
# image = torch.rand((1, 3, 64, 64))
# secret = torch.rand((1, 1, 64, 64))

# # Forward
# stego = encoder(image, secret)
# recovered = decoder(stego)

# print("Test completed!")