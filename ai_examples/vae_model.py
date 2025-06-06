import torch
from torch import nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

# === Modelo VAE ===
class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 400),
            nn.ReLU()
        )
        self.fc_mu = nn.Linear(400, 2)        # espacio latente 2D
        self.fc_logvar = nn.Linear(400, 2)
        self.decoder = nn.Sequential(
            nn.Linear(2, 400),
            nn.ReLU(),
            nn.Linear(400, 28*28),
            nn.Sigmoid()
        )

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        x_flat = self.encoder(x)
        mu = self.fc_mu(x_flat)
        logvar = self.fc_logvar(x_flat)
        z = self.reparameterize(mu, logvar)
        recon = self.decoder(z)
        return recon.view(-1, 1, 28, 28), mu, logvar

# === Pérdida VAE ===
def vae_loss(recon_x, x, mu, logvar):
    BCE = nn.functional.binary_cross_entropy(recon_x.view(-1, 28*28), x.view(-1, 28*28), reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + KLD

# === Datos MNIST ===
transform = transforms.ToTensor()
mnist = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
loader = DataLoader(mnist, batch_size=128, shuffle=True)

# === Entrenamiento ===
vae = VAE()
optimizer = torch.optim.Adam(vae.parameters(), lr=1e-3)

vae.train()
for epoch in range(5):  # puedes aumentar este valor
    total_loss = 0
    for batch, _ in loader:
        optimizer.zero_grad()
        recon_batch, mu, logvar = vae(batch)
        loss = vae_loss(recon_batch, batch, mu, logvar)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/len(loader.dataset):.4f}")

# === Visualización del espacio latente ===
vae.eval()
n = 10  # malla 10x10
grid_x = np.linspace(-3, 3, n)
grid_y = np.linspace(-3, 3, n)

canvas = np.empty((28 * n, 28 * n))

with torch.no_grad():
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z = torch.tensor([[xi, yi]], dtype=torch.float32)
            out = vae.decoder(z).view(28, 28).numpy()
            canvas[i * 28:(i + 1) * 28, j * 28:(j + 1) * 28] = out

plt.figure(figsize=(8, 8))
plt.imshow(canvas, cmap="gray")
plt.axis("off")
plt.title("Malla del espacio latente (VAE)")
plt.show()
