from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re, nltk
nltk.download('stopwords')
from nltk.corpus import stopwords # filter out stopwords, such as 'the', 'or', 'and'

class ScraperEngine:

    wordList = [w for w in nltk.corpus.words.words('en')] # list of English words
    urlPattern = '((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'
    #https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))'

    def __init__(self, url):
        self.url = url

    def test_url(self):
        print("Testing URL: ", self.url, "...")
        urls = re.findall(ScraperEngine.urlPattern+'+', self.url)
        print(urls, 'Length:', len(urls))
        if len(urls) == 1:
            return True
        else:
            raise InvalidURLError("URL not in correct format.")

    def url_scrape(self):
        # ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urlopen(self.url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")

        for script in soup(["script", "style"]):
            script.extract() # remove these two elements from the BeautifulSoup object

        text = soup.get_text()
        # remove url's
        text = re.sub(ScraperEngine.urlPattern, "", text)
        text = re.sub("[^a-zA-Z' ]","", text) # remove everything that's not a word
        textPieces = text.split()

        stopWords = set(stopwords.words("english")) # lists pointless words like 'it', 'the' etc
        textPieces = [word for word in textPieces if not word in stopWords] # remove stopwords from the text
        #print(textPieces)

        return (textPieces)

    def lexical_diversity(self,text):
        word_count = len(text)
        vocab_size = len(set(text))
        diversity_score = vocab_size / word_count
        return diversity_score

    def frequency_distribution(self, text, num=50):
        fdist = nltk.FreqDist(text)#(word.lower for word in text) # get the frequency of each word
        return fdist.most_common(num)

    def longest_words(self, text, num=50):
        text.sort() # sorts normally by alphabetical order
        text.sort(key=len, reverse=True) # sorts by descending length
        #length_order = [(word, len(word)) for word in text] # get the frequency of each word
        length_order = list()
        for word in text:
            if word in self.wordList: # check the word is valid:
                tup = (word,len(word))
                length_order.append(tup)
        return length_order[:num]

    def word_lengths(self, text, num=50):
        fdist = nltk.FreqDist(len(word) for word in text) # get the frequency of each word
        return fdist.most_common(num)

    def generate_json(self, fdist, type, large=150, small=20):
        #fdist = self.frequency_distribution(text)
        lowest = fdist[-1][1]
        highest = fdist[0][1]
        #print("l",lowest,"h",highest)
        fhand = open('js/wordcloud.js','w')
        fhand.write('url = "'+self.url+'"; type = "'+type+'";')
        fhand.write("wordcloud = [")
        first = True
        for tup in fdist: # freqdist is a list of tuples
            # tup[0] is the word in freqdist
            word = re.sub("[']","", str(tup[0])) # remove ' as it messes with the js
            wordFrequency = tup[1] # tup[1] is the frequency in freqdist
            #textRemoved = [word for word in textPieces if word not in wordList] # keep track of removed non-English 'real' words
            #textPieces = [word for word in textPieces if word in wordList and wordFrequency > 1] # only keep real words
            if wordFrequency < 4: # if the 'word' is used only <n times
                if word not in self.wordList: # check the word is valid
                    continue # it's not a valid word only used <n so disregard
            if not first : fhand.write( ",\n")
            first = False
            size = wordFrequency
            size = (size - lowest) / float(highest - lowest)
            size = int((size * large) + small)
            fhand.write("{text: '"+word+"', size: "+str(size)+"}")

        fhand.write( "\n];\n")
        fhand.close()


class InvalidURLError(Exception):
    """Throw this when URL is not correct format."""
