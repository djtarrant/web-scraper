# Web Scraper in Python

## Basic Function
Takes in a URL and outputs a JSON data file of the most common words within that URL, along with a couple of other pieces of language processing information.

## Pip Install Python and Initialise Program
To initialise the program, run app.py within a Python IDE. If you have not done so, the program will require installation or import of the Python libraries for NLTK and BeautifulSoup.

These can be found here:

[NLTK](http://www.nltk.org/)

[Beautfiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## I/O
The program prompts you to enter a URL, or defaults to the [bbc.co.uk](http://www.bbc.co.uk) main page and then processes the text at that URL. Please take care to obey scraping advice from the target website. It outputs lexical diversity (proportion of unique words across whole text), frequency distribution (the most common words and the number of times they are used) and a JSON file of the frequency distribution.

## HTML/JS files
The d3.js and wordcloud Javascript files were obtained from the internet and were not the focus of this project. When utilised within the wordcloud.html file they create a wordcloud of the most common words within the target URL. Parameters can be altered within the py files to change the wordcloud size and shape. Opening wordcloud.html is the final prompt of the app.py file output, which tries to do this automatically.

## TO DO
* Format space errors in text processing
* Web wrapper for URL entry
