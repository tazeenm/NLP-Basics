'''
Find out meaning of words based on the contexrt in which ir occurs.
Using wordnet (something like a Thesaurus) and synsets (1 definition of a word)
A word can have multiple meanings and each meaning is a synset (meaning of word + number/index)
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
#nltk.download('wordnet')
for ss in wn.synsets('bass'):
    print(ss, ss.definition())

#lesk is an algorithm for Word sense disambiguation
from nltk.wsd import lesk
sense1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), 'bass')
print("\nDEFINITION 1: ", sense1, sense1.definition())

sense2 = lesk(word_tokenize("This sea bass was really hard to catch"), 'bass')
print("\nDEFINITION 2: ", sense2, sense2.definition())