#!/usr/bin/env python3
# coding: utf-8

d = r"./diabetes.csv.gz"
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt

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

criterion = torch.nn.BCELoss(size_average=True)
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
        a1 = F.relu(model.l1(x_data))
        a2 = F.relu(model.l2(a1))
        activations_l1.append(a1.mean().item())  # Promedio de activación
        activations_l2.append(a2.mean().item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
plt.plot(losses)
plt.title("Pérdida durante entrenamiento")
plt.xlabel("Época")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

plt.plot(activations_l1, label="Capa 1 (ReLU)")
plt.plot(activations_l2, label="Capa 2 (ReLU)")
plt.title("Activación media por capa")
plt.xlabel("Época")
plt.ylabel("Valor promedio de activación")
plt.legend()
plt.grid(True)
plt.show()

with torch.no_grad():
    pred = model(x_data)
    predicted_classes = (pred > 0.5).float()
    accuracy = (predicted_classes == y_data).sum() / y_data.shape[0]
    print("Accuracy final:", accuracy.item())