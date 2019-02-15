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
    print(type(text))
    return text.replace("?", " ")

text = getTextWithoutPunctuation(articleURL)
print(text.encode("utf-8"))
#------------------------------------------------------------------------------------------------------

#get a list of individual sentences (based on period followed by a space)
sents = sent_tokenize(text)
print(sents)

#get a list of words (words + punctuations)
word_sent = word_tokenize(text.lower())
print(word_sent)

#remove stop words from this list of words
_stopwords = set(stopwords.words('english') + list(punctuation))
print(_stopwords)
word_sent = [word for word in word_sent if word not in _stopwords]
print(word_sent)