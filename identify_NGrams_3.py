'''
Identify words that occur frequently together.
'''
import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from remove_stop_words import words_without_stopwords
#Collocations are any words that occur together
bigram_measures =  nltk.collocations.BigramAssocMeasures()
#BigramCollocationFinder construct Bigrams from a given list of words
finder = BigramCollocationFinder.from_words(words_without_stopwords)
print(sorted(finder.ngram_fd.items()))

#can use BigramCollocationFinder to find words in groups of 2 
#TrigramCollocationFinder for words in groups of 3