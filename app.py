from engine import  test_url, url_scrape, frequency_distribution, lexical_diversity, generate_json
import webbrowser, os

filename = 'wordcloud.html'
url = input('Please enter the URL - ')
if(len(url) == 0):
    url = 'http://www.bbc.co.uk'

try:
    test_url(url)
except:
    print("There was an error with the URL. The program will now quit")
    quit()

text = url_scrape(url)
#we should now have a list of words scraped from the url
print(text)
print("Lexical diversity:",lexical_diversity(text))
print("Frequency Distribution:",frequency_distribution(text, 20))
#generate our JSON for the wordcloud
generate_json(text)#optionally add the font sizes
print("Open",filename,"in the browser to see the wordcloud. Trying to open...")
webbrowser.open('file://' + os.path.realpath(filename))
