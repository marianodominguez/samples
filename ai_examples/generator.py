import os
import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt

# Cargar MNIST
transform = transforms.ToTensor()
mnist = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
loader = torch.utils.data.DataLoader(mnist, batch_size=128, shuffle=True)
PATH = "./model/trained_model.pth" # You can use .pt or .pth extension

# Autoencoder básico
class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 64),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(64, 28*28),
            nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )

    def forward(self, x):
        z = self.encoder(x)
        out = self.decoder(z)
        return out

model = Autoencoder()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()
#si el modelo existe, lo cargamos

if os.path.isfile(PATH):
    model.load_state_dict(torch.load(PATH))
    model.eval()
else:
    # Entrenamiento
    for epoch in range(5):
        for img, _ in loader:
            output = model(img)
            loss = criterion(output, img)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), PATH)


# Visualizar generación
with torch.no_grad():
    #test_img = next(iter(loader))[0][:8]
    #recon = model(test_img)

    # Tomamos imágenes que NO fueron vistas en entrenamiento (del test set)
    test_data = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=8, shuffle=True)

    # Reconstrucción
    test_imgs, _ = next(iter(test_loader))
    recons = model(test_imgs)

    fig, axs = plt.subplots(2, 8, figsize=(12, 3))
    for i in range(8):
        axs[0, i].imshow(test_imgs[i][0], cmap='gray')
        axs[1, i].imshow(recons[i][0], cmap='gray')
        axs[0, i].axis('off')
        axs[1, i].axis('off')
    axs[0, 0].set_ylabel("Input")
    axs[1, 0].set_ylabel("Recon")
    plt.show()
