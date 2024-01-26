import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Fragmento de texto
texto = """Ralph se sentó en la arena caliente, tocando la concha, sonriendo y asintiendo con la cabeza a los gritos de admiración. A su alrededor, los niños comenzaron a asentarse y a prestar atención. Era como si hubiesen oído por primera vez la brillante idea de la democracia."""

# Tokenización
oraciones = sent_tokenize(texto)
palabras = [word_tokenize(oracion) for oracion in oraciones]

# Etiquetado de Partes del Discurso (POS Tagging)
pos_tags = [pos_tag(palabra) for palabra in palabras]

# Lematización
lemmatizer = WordNetLemmatizer()
lemmas = [[lemmatizer.lemmatize(token[0], pos=token[1][0].lower()) if token[1][0].lower() in ['a', 'n', 'v'] else lemmatizer.lemmatize(token[0]) for token in pos_tag] for pos_tag in pos_tags]

# Análisis de Sentimientos
sentiment_analyzer = SentimentIntensityAnalyzer()
polaridad = sentiment_analyzer.polarity_scores(texto)

# Extracción de Entidades Nombradas (NER)
entidades_nombradas = ne_chunk(pos_tag(word_tokenize(texto)))

# Imprimir resultados
print("Oraciones tokenizadas:")
print(oraciones)

print("\nPalabras tokenizadas:")
print(palabras)

print("\nEtiquetado POS:")
print(pos_tags)

print("\nLematización:")
print(lemmas)

print("\nAnálisis de Sentimientos:")
print("Polaridad:", polaridad['compound'])

print("\nEntidades Nombradas:")
print(entidades_nombradas)
