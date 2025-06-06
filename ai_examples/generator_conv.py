import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

# 📥 Dataset: MNIST
transform = transforms.Compose([
    transforms.ToTensor()
])

train_data = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# 🧠 Autoencoder convolucional
class ConvAutoencoder(nn.Module):
    def __init__(self):
        super(ConvAutoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, 3, stride=2, padding=1),  # 28x28 → 14x14
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1), # 14x14 → 7x7
            nn.ReLU()
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, 3, stride=2, padding=1, output_padding=1),  # 7x7 → 14x14
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, 3, stride=2, padding=1, output_padding=1),   # 14x14 → 28x28
            nn.Sigmoid()  # para imágenes entre 0 y 1
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# 🛠️ Entrenamiento
model = ConvAutoencoder()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(5):
    for data in train_loader:
        imgs, _ = data
        outputs = model(imgs)
        loss = criterion(outputs, imgs)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 🧾 Mostrar resultados
def show_images(original, reconstructed, n=8):
    fig, axes = plt.subplots(2, n, figsize=(n*2, 4))
    for i in range(n):
        axes[0, i].imshow(original[i][0].detach().numpy(), cmap='gray')
        axes[0, i].axis('off')
        axes[1, i].imshow(reconstructed[i][0].detach().numpy(), cmap='gray')
        axes[1, i].axis('off')
    axes[0, 0].set_title("Original", fontsize=12)
    axes[1, 0].set_title("Reconstrucción", fontsize=12)
    plt.show()

# 🔍 Visualizar
test_imgs, _ = next(iter(train_loader))
reconstructed = model(test_imgs)
show_images(test_imgs, reconstructed)

# 🔄 Obtener los vectores latentes de un lote grande
model.eval()
latents = []
labels = []

with torch.no_grad():
    for imgs, lbls in train_loader:
        encoded = model.encoder(imgs)             # [batch, 32, 7, 7]
        flattened = encoded.view(encoded.size(0), -1)  # [batch, 1568]
        latents.append(flattened)
        labels.append(lbls)
        if len(latents) > 10: break  # Solo usamos ~640 muestras para velocidad

latents = torch.cat(latents, dim=0).numpy()
labels = torch.cat(labels, dim=0).numpy()

# 🔻 t-SNE para reducir a 2D
tsne = TSNE(n_components=2, random_state=42)
latents_2d = tsne.fit_transform(latents)

# 🎨 Graficar con colores por dígito


plt.figure(figsize=(10, 8))
scatter = plt.scatter(latents_2d[:, 0], latents_2d[:, 1], c=labels, cmap='tab10', alpha=0.7)
plt.colorbar(scatter, ticks=range(10))
plt.title("Espacio Latente de MNIST codificado (t-SNE)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.grid(True)
plt.show()