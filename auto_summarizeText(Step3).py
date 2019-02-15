from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

#import downloadWebPage.py -----------------------------------------------------------------------------------
import urllib.request 
from bs4 import BeautifulSoup
articleURL = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.1c97964c9624"
def getTextWithoutPunctuation(url):
    page = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p : p.text, soup.find_all('article')))
    return text.replace("?", " ")

text = getTextWithoutPunctuation(articleURL)
#print(text.encode("utf-8"))
#---------------------------------------------------------------------------------------------------------------

#import preprocess_DownloadedText.py-----------------------------------------------------------------------------
sents = sent_tokenize(text)
#print(sents)

#get a list of words (words + punctuations)
word_sent = word_tokenize(text.lower())
#print(word_sent)

#remove stop words from this list of words
_stopwords = set(stopwords.words('english') + list(punctuation))
#print(_stopwords)
word_sent = [word for word in word_sent if word not in _stopwords]
#print(word_sent)
#-----------------------------------------------------------------------------------------------------------------
#summarize text
#Construct a frequence distribution - table with words in one column and the no. of times it occurs.
#Higher the frequency, higher the importance of the word.
from nltk.probability import FreqDist
freq = FreqDist(word_sent)
print(freq)

#Sort any collection using nlargest
from heapq import nlargest
nlargest(10, freq, key = freq.get)

#find significance score for each sentence = sum(freq of all words)
from collections import defaultdict
#create a default dict with key = sentences and value = significant score
#default dict = if you lookup a nonexistant key, it won't throw error but add it to the dict
ranking = defaultdict(int)

#enumerate() takes a list and returns a list of tuple where 1st element of tuple is index of list element of sents. 
for i, sent in enumerate(sents):
    for w in word_tokenize(sent.lower()):
        if(w in freq):
            ranking[i] += freq[w]
print(ranking)

#Pick the top N sentences where N=size of absract/no. of sentences in abstract
sents_idx = nlargest(4, ranking, key = ranking.get)
#Indices of sentences won't be in order so put them in order
print(sents_idx)

print([sents[j] for j in sorted(sents_idx)])


