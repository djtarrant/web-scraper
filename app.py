from engine import url_scrape

url = input('Please enter the URL - ')
try:
    text = url_scrape(url)
except:
    print("There was an error with the URL. The program will now quit")
    quit()

#we should now have a bunch of text scraped from the url 
