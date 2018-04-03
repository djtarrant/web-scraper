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


class InvalidURLError(Exception):
    """Throw this when URL is not correct format."""
