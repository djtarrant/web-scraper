from engine import ScraperEngine
#test_url, url_scrape, frequency_distribution, lexical_diversity, generate_json
import webbrowser, os

filename = 'wordcloud.html'
url = input('Please enter the URL - ')
if(len(url) == 0):
    url = 'http://www.bbc.co.uk'

page_object = ScraperEngine(url)
#print(page_object.url)
try:
    page_object.test_url()
except:
    print("There was an error with the URL. The program will now quit")
    quit()

text = page_object.url_scrape()
#we should now have a list of words scraped from the url
#print(text)
print("Lexical diversity:",page_object.lexical_diversity(text))
print("Frequency Distribution:",page_object.frequency_distribution(text, 50))
#generate our JSON for the wordcloud
page_object.generate_json(text, 150, 20) # optionally add the font sizes
print("Open",filename,"in the browser to see the wordcloud. Trying to open...")
webbrowser.open('file://' + os.path.realpath(filename))
