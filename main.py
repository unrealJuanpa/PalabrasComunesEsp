import nltk
import numpy as np

# Descarga la lista de frecuencia de palabras en español de nltk
nltk.download('stopwords')
nltk.download('cess_esp')
stopwords_es = nltk.corpus.stopwords.words('spanish')
words_es = nltk.corpus.cess_esp.words()

# Crea una lista de palabras en español sin las palabras de parada
words_cleaned = [word.lower() for word in words_es if word.lower() not in stopwords_es and word.isalpha()]

# Crea un diccionario con la frecuencia de cada palabra
freq_dist = nltk.FreqDist(words_cleaned)

# Obtiene las 4096 palabras más comunes
most_common_words = [word for word, freq in freq_dist.most_common(4096)]

# Imprime las primeras 10 palabras
print(len(most_common_words))

np.save('palabras.npy', np.array(most_common_words))