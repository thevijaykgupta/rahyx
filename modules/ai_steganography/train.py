import torch
import torch.nn as nn
import torch.optim as optim
from model import Encoder, Decoder
from torchvision import transforms,datasets

# Load dataset (for future real training)
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])
dataset = datasets.CIFAR10(root='./data', download=True, transform=transform)
loader = torch.utils.data.DataLoader(dataset, batch_size=4)

# Initialize models
encoder = Encoder()
decoder = Decoder()

criterion = nn.MSELoss()
optimizer = optim.Adam(list(encoder.parameters()) + list(decoder.parameters()), lr=0.001)

# Dummy training (for now)
for epoch in range(5):
    # Fake data (you will replace later with real images)
    image = torch.rand((1, 3, 64, 64))
    secret = torch.rand((1, 1, 64, 64))

    # Forward
    stego = encoder(image, secret)
    recovered = decoder(stego)

    # Loss
    loss_image = criterion(stego, image)
    loss_secret = criterion(recovered, secret)
    loss = loss_image + loss_secret

    # Backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Save models
torch.save(encoder.state_dict(), "encoder.pth")
torch.save(decoder.state_dict(), "decoder.pth")