import urllib.request
#To parse the webpage 
from bs4 import BeautifulSoup
articleURL = "https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.1c97964c9624"

'''
#Proxy settings
proxy_support = urllib.request.ProxyHandler({"http":"http://146.194.56.20:8080"})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
'''

def getTextWithoutPunctuation(url):
    #Download the webpage
    page = urllib.request.urlopen(url).read().decode('utf-8')
    #creates a Tree structure within it representing the HTML Structure of the page. 
    soup = BeautifulSoup(page, "lxml")
    '''
    #print the whole structure of the article including the tags and extra details
    print(soup)

    #Find the tags that contain the article and print it (returns first instance + )
    soup.find('article')
    #print only the text
    soup.find('article').text
    '''

    #Print all the article elements and combine it into one single string
    text = ' '.join(map(lambda p : p.text, soup.find_all('article')))
    #print(text)
    print(type(text))
    #Text contains special characters so need encoding. Remove special characters
    #return text.encode('ascii', errors = 'replace').replace("?", " ")
    return text.replace("?", " ")

text = getTextWithoutPunctuation(articleURL)
print(text.encode("utf-8"))
