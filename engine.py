from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import nltk
from nltk.corpus import stopwords # filter out stopwords, such as 'the', 'or', 'and'

def test_url(url):
    print("Testing URL: ", url, "...")
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    print(urls, 'Length:', len(urls))
    if len(urls) == 1:
        return True
    else:
        raise InvalidURLError("URL not in correct format.")

def url_scrape(url):
    # ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    for script in soup(["script", "style"]):
        script.extract() # remove these two elements from the BeautifulSoup object

    text = soup.get_text()
    text = re.sub("[^a-zA-Z' ]","", text) # remove everything that's not a word
    textPieces = text.split()

    stop_words = set(stopwords.words("english")) # lists pointless words like 'it', 'the' etc
    textPieces = [word for word in textPieces if not word in stop_words] # remove stopwords from the text

    return (textPieces)

def frequency_distribution(text, num_common=50):
    fdist = nltk.FreqDist(text)#(word.lower for word in text) # get the frequency of each word
    return fdist.most_common(num_common)


def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    diversity_score = vocab_size / word_count
    return diversity_score

def generate_json(text, large=150, small=20):
    fdist = frequency_distribution(text)
    lowest = fdist[-1][1]
    highest = fdist[0][1]
    #print("l",lowest,"h",highest)
    fhand = open('js/wordcloud.js','w')
    fhand.write("wordcloud = [")
    first = True
    for tup in fdist: # freqdist is a list of tuples
        if not first : fhand.write( ",\n")
        first = False
        size = tup[1] # tup[1] is the frequency in freqdist
        size = (size - lowest) / float(highest - lowest)
        size = int((size * large) + small)
        # tup[0] is the word in freqdist
        word = re.sub("[']","", tup[0]) # remove ' as it messes with the js
        fhand.write("{text: '"+word+"', size: "+str(size)+"}")
    fhand.write( "\n];\n")
    fhand.close()


class InvalidURLError(Exception):
    """Throw this when URL is not correct format."""
