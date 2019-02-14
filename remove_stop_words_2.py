'''
Remove the words that do not add to the meaning of the sentence
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
#nltk.download('stopwords')

text = "Mary had a little lamb. Her fleece was white as snow."
words_tokenize = word_tokenize(text)
#Punctuations are treated as separate tokens in nltk
#Get a set of stop words from English language and a list of all punctuations available.
customStopWords = set(stopwords.words('english') + list(punctuation))

# for word in words_tokenize:
#     if(word not in customStopWords):
#        print(word)

words_without_stopwords = [word for word in words_tokenize if word not in customStopWords]
print(words_without_stopwords)
