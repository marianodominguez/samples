from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Cargamos un modelo pre-finetuneado (opcional: puedes entrenar el tuyo)
model_name = "rogelioplatt/distilbert-base-multilingual-cased-Sarcasmo_Esp"  # puedes cambiarlo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Creamos pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Probar una frase
text = "Wow, qué buena idea dejar el paraguas en casa justo hoy que llueve a cántaros."

id2label = model.config.id2label

result = classifier(text)
label_id = 0
label_name = id2label[label_id] if label_id in id2label else "Unknown"

print(result)
print(f"Predicción: {label_name} (confianza: {result[0]['score']:.2f})")