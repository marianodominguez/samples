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
example = x_data[0].unsqueeze(0)  # Agrega dimensión batch (1, 8)

def plot_vector(vec, title, ax):
    vec = vec.squeeze().numpy()
    ax.bar(range(len(vec)), vec)
    ax.set_title(title)
    ax.set_ylim(0, 1)  # para comparabilidad

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
    
    with torch.no_grad():
        a1 = F.relu(model.l1(example))
        a2 = F.relu(model.l2(a1))
        output = model.sigmoid(model.l3(a2))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
print("Entrada:")
print(example)
print("Después de capa 1 (ReLU):")
print(a1)
print("Después de capa 2 (ReLU):")
print(a2)
print("Salida (sigmoid):")
print(output)

fig, axs = plt.subplots(1, 4, figsize=(16, 4))

plot_vector(example, "Entrada (8)", axs[0])
plot_vector(a1, "Capa 1 (6)", axs[1])
plot_vector(a2, "Capa 2 (4)", axs[2])
#plot_vector(output, "Salida (1)", axs[3])

plt.tight_layout()
plt.show()