import spacy

# Cargar el modelo en español de spaCy
nlp = spacy.load('es_core_news_sm')

# Texto de ejemplo en español
texto = """Ralph se sentó en la arena caliente, tocando la concha, sonriendo y asintiendo con la cabeza a los gritos de admiración. 
A su alrededor, los niños comenzaron a asentarse y a prestar atención. 
Era como si hubiesen oído por primera vez la brillante idea de la democracia."""

# Procesar el texto con spaCy
doc = nlp(texto)

# Tokenización y Etiquetado POS
oraciones = list(doc.sents)
palabras = [word.text for word in doc]
etiquetas_pos = [(word.text, word.pos_) for word in doc]

# Lematización
lemas = [word.lemma_ for word in doc]

# Análisis de Sentimientos
# NLTK SentimentIntensityAnalyzer no es óptimo para español, se puede usar otra herramienta o traducir el texto a inglés

# Extracción de Entidades Nombradas (NER)
entidades = [(ent.text, ent.label_) for ent in doc.ents]

# Imprimir resultados
print("Oraciones tokenizadas:")
for oracion in oraciones:
    print(oracion.text)
print("\nPalabras tokenizadas:")
print(palabras)
print("\nEtiquetas POS:")
print(etiquetas_pos)
print("\nLemas:")
print(lemas)
print("\nEntidades Nombradas:")
print(entidades)