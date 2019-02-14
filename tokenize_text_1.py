'''
Break text into sentences and words (which includes punctuation as well)
'''
import nltk
#nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize
text = "Mary had a little lamb. Her fleece was white as snow."

sentence_tokenize = sent_tokenize(text)
print(sentence_tokenize)


for words in sentence_tokenize:
    words_tokenize = word_tokenize(words) 
print(words_tokenize)
    
