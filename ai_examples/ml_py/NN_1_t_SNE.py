
d = r"./diabetes.csv.gz"
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

xy = np.loadtxt(d, delimiter=',', dtype=np.float32)
x_data = Variable(torch.from_numpy(xy[:,0:-1]))
y_data = Variable(torch.from_numpy(xy[:,[-1]]))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.l1=torch.nn.Linear(8,6)
        self.l2=torch.nn.Linear(6,4)
        self.l3=torch.nn.Linear(4,1)
        
        self.sigmoid = torch.nn.Sigmoid()
        
    def forward(self,x):
        out1 = F.relu(self.l1(x))
        out2 = F.relu(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))
        return y_pred

model = Model()

criterion = torch.nn.BCELoss(size_average=True)  # Para clasificación binaria (salida entre 0 y 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

losses = []
activations_l1 = []
activations_l2 = []

for epoch in range(1000):
    y_pred = model(x_data)
    
    loss = criterion(y_pred, y_data)
    losses.append(loss.item())
    
    # Guardamos activaciones de las dos capas ocultas (para visualización)
    with torch.no_grad():
        a1_all = F.relu(model.l1(x_data))
        a2_all = F.relu(model.l2(a1_all))
        outputs = model.sigmoid(model.l3(a2_all))

    # Convertir a numpy
    a2_np = a2_all.numpy()
    labels = y_data.numpy().flatten()  # 0 o 1
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
# Aplicar t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
a2_2d = tsne.fit_transform(a2_np)

with torch.no_grad():
    pred = model(x_data)
    predicted_classes = (pred > 0.5).float()
    accuracy = (predicted_classes == y_data).sum() / y_data.shape[0]
    print("Accuracy final:", accuracy.item())

# Graficar
plt.figure(figsize=(8, 6))
plt.scatter(a2_2d[labels == 0, 0], a2_2d[labels == 0, 1], label="No Diabetes", alpha=0.6)
plt.scatter(a2_2d[labels == 1, 0], a2_2d[labels == 1, 1], label="Diabetes", alpha=0.6, color="red")
plt.legend()
plt.title("t-SNE de las activaciones (Capa 2)")
plt.xlabel("Dim 1")
plt.ylabel("Dim 2")
plt.grid(True)
plt.show()