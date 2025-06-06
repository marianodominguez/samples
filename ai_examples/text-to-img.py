import torch
from torch import nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

# --- Definimos el VAE (igual que antes) ---
class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 400),
            nn.ReLU()
        )
        self.fc_mu = nn.Linear(400, 2)
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

# --- Pérdida del VAE ---
def vae_loss(recon_x, x, mu, logvar):
    BCE = F.binary_cross_entropy(recon_x.view(-1, 28*28), x.view(-1, 28*28), reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + KLD

# --- Datos ---
transform = transforms.ToTensor()
mnist = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# Para simplificar, usamos solo las imágenes de los dígitos del 0 al 9 (todo MNIST)
loader = DataLoader(mnist, batch_size=128, shuffle=True)

# --- Entrenamos el VAE primero ---
vae = VAE()
optimizer = torch.optim.Adam(vae.parameters(), lr=1e-3)

vae.train()
for epoch in range(5):
    total_loss = 0
    for batch, _ in loader:
        optimizer.zero_grad()
        recon_batch, mu, logvar = vae(batch)
        loss = vae_loss(recon_batch, batch, mu, logvar)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/len(loader.dataset):.4f}")

# --- Creamos un diccionario simple texto->index ---
text_to_idx = {
    'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
    'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9
}

# --- Creamos embeddings one-hot para cada palabra ---
def text_to_onehot(text):
    idx = text_to_idx[text]
    onehot = torch.zeros(len(text_to_idx))
    onehot[idx] = 1.0
    return onehot.unsqueeze(0)  # batch dim

# --- Dataset para entrenar el text->z ---
# Para esto, calculamos mu (vector latente medio) de imágenes etiquetadas con su dígito
digit_to_mu = {i: [] for i in range(10)}
vae.eval()
with torch.no_grad():
    for img, label in mnist:
        img = img.unsqueeze(0)
        _, mu, _ = vae(img)
        digit_to_mu[label].append(mu.squeeze(0).numpy())
for k in digit_to_mu:
    digit_to_mu[k] = np.mean(digit_to_mu[k], axis=0)  # vector promedio por dígito

# --- Modelo pequeño que aprende text->z ---
class TextToZ(nn.Module):
    def __init__(self):
        super(TextToZ, self).__init__()
        self.fc = nn.Linear(len(text_to_idx), 2)
    def forward(self, x):
        return self.fc(x)

text2z = TextToZ()
optimizer_t2z = torch.optim.Adam(text2z.parameters(), lr=0.01)
criterion = nn.MSELoss()

# --- Entrenamiento text->z ---
for epoch in range(500):
    optimizer_t2z.zero_grad()
    loss_epoch = 0
    for text, idx in text_to_idx.items():
        input_vec = text_to_onehot(text)
        target_vec = torch.tensor(digit_to_mu[idx], dtype=torch.float32).unsqueeze(0)
        pred = text2z(input_vec)
        loss = criterion(pred, target_vec)
        loss.backward()
        optimizer_t2z.step()
        loss_epoch += loss.item()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss {loss_epoch/10:.4f}")

# --- Prueba generación de imágenes a partir de texto ---
vae.eval()
text2z.eval()

def generar_imagen(text):
    with torch.no_grad():
        input_vec = text_to_onehot(text)
        z_pred = text2z(input_vec)
        img = vae.decoder(z_pred).view(28, 28).numpy()
    plt.imshow(img, cmap='gray')
    plt.title(f'Imagen generada para "{text}"')
    plt.axis('off')
    plt.show()

# --- Ejemplo ---
generar_imagen("tres")
generar_imagen("siete")
