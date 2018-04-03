from engine import  test_url, url_scrape, frequency_distribution, lexical_diversity


url = input('Please enter the URL - ')
if(len(url) == 0):
    url = 'http://www.darrentarrant.co.uk/myportfolio.php'

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
