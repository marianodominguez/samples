from transformers import AutoTokenizer, AutoModel
import torch
import matplotlib.pyplot as plt

# Elegimos un modelo chiquito tipo BERT
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_attentions=True)

# Ejemplo de texto
text = "The cat sat on the mat."
#text = "The dog chased the ball across the park."
#text = "Across the park, the ball was chased by the dog."

# Tokenización
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# Primer hidden state: representaciones por token
hidden_states = outputs.last_hidden_state  # shape: (1, num_tokens, hidden_size)
print("Shape:", hidden_states.shape)  # Ejemplo: (1, 10, 768)

# Atención (de cada cabeza en cada capa)
attentions = outputs.attentions  # Esto es una tupla de (layers) con tensores
print("Número de capas:", len(attentions))

layer = 0 # Capa de atención a visualizar
head = [1,0] # Cabeza de atención a visualizar

print("Shape atención capa f{layer}:", attentions[layer].shape)  # (batch, heads, tokens, tokens)

# Atención de la n capa, primera cabeza
attn = attentions[layer][0, 0].numpy()  # shape: (tokens, tokens)

tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
plt.figure(figsize=(8, 8))
plt.imshow(attn, cmap="viridis")
plt.xticks(range(len(tokens)), tokens, rotation=90)
plt.yticks(range(len(tokens)), tokens)
plt.title(f"Atención (capa {layer}, {head} )")
plt.colorbar()
plt.show()