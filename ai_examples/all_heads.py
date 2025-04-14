from transformers import AutoTokenizer, AutoModel
import torch
import matplotlib.pyplot as plt

# Carga modelo y tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_attentions=True)
model.eval()

# Texto a analizar
#text = "The cat sat on the mat."

text = "the cat eats the mouse"
# Tokeniza
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# Atención de la capa 0 (puedes cambiarla)
layer = 0
attentions = outputs.attentions[layer][0]  # shape: (heads, tokens, tokens)

tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
num_heads = attentions.shape[0]

# Visualización: una subfigura por cabeza
cols = 4
rows = (num_heads + cols - 1) // cols
fig, axes = plt.subplots(rows, cols, figsize=(cols * 3, rows * 3))
fig.suptitle(f'Cabezas por capa {layer}', fontsize=16)

for i in range(num_heads):
    ax = axes[i // cols, i % cols]
    im = ax.imshow(attentions[i].numpy(), cmap="viridis")
    ax.set_title(f"Cabeza {i}")
    ax.set_xticks(range(len(tokens)))
    ax.set_yticks(range(len(tokens)))
    ax.set_xticklabels(tokens, rotation=90)
    ax.set_yticklabels(tokens)
    ax.tick_params(axis='both', which='both', length=0)
    
# Si sobran cuadros, los ocultamos
for j in range(num_heads, rows * cols):
    axes[j // cols, j % cols].axis("off")

plt.tight_layout()

plt.show()
