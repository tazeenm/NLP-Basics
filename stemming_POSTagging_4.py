'''
Stemming: same meaning words treated as 1 word. Reduce words to their stem words.
Part of Speech Tagging: Tag words based on whether it is a noun, verb, adjective, etc.
'''
import nltk
from nltk.tokenize import word_tokenize

#Stemmer used: Lancaster Stemmer
text = "Mary closed on closing night when she was in the mood to close."
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(text)]
print(stemmedWords)

#Tagging - Noun, Verb, Adverb, Adjective, etc
#NNP-Proper Noun, VBD-Verb, NN-Noun, PRP-Pronoun
#nltk.download('averaged_perceptron_tagger')
pos_taggs = nltk.pos_tag(word_tokenize(text))
print(pos_taggs)
