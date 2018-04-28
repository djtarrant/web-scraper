from engine import ScraperEngine
#test_url, url_scrape, frequency_distribution, lexical_diversity, generate_json
import webbrowser, os, re, time

filename = 'wordcloud.html'
url = input('Please enter the URL to scrape: ')
if(len(url) == 0):
    url = 'http://www.bbc.co.uk'

page_object = ScraperEngine(url)
#print(page_object.url)
try:
    page_object.test_url()
except:
    print("There was an error with the URL. The program will now quit")
    quit()

# present the options
print("Please select an option from 1-3:")
print("Select 1: Wordcloud of Frequency Distribution (most common words)")
print("Select 2: Wordcloud of Longest Words")
print("Select 3: Wordcloud of Word Lengths (most common word lengths)")
option_selected = False
while(not option_selected):

    option = input('Please enter a number from 1-3 OR 0 to quit: ')

    try:
        option = int(option)
    except Exception as e:
        print("Please input a number 1,2 or 3")
        continue

    if option == 0:
        print("Quitting...")
        option_selected = True
        continue
    print("Working...")
    # process the selection
    if option == 1:
        # frequency distribution
        option_selected = True
        text = page_object.url_scrape()
        print("Lexical diversity:", page_object.lexical_diversity(text))
        #print("Frequency Distribution:", page_object.frequency_distribution(text, 50))
        fdist = page_object.frequency_distribution(text, 50)
        #generate our JSON for the wordcloud
        print("Generating the JSON, may take a few seconds...")
        page_object.generate_json(fdist, "Frequency Distribution", 150, 20) # optionally add the font sizes
        print("Open",filename,"in the browser to see the wordcloud. Trying to open...")
        webbrowser.open('file://' + os.path.realpath(filename))

    elif option == 2:
        # longest words
        option_selected = True
        text = page_object.url_scrape()
        longest_words = page_object.longest_words(text,20)
        #print(longest_words)
        #generate our JSON for the wordcloud
        print("Generating the JSON, may take a few seconds...")
        page_object.generate_json(longest_words, "Longest Words", 150, 20) # optionally add the font sizes
        time.sleep(5) # allow the json to be generated
        print("Open",filename,"in the browser to see the wordcloud. Trying to open...")
        webbrowser.open('file://' + os.path.realpath(filename))

    elif option == 3:
        # list of word lengths
        option_selected = True
        text = page_object.url_scrape()
        word_lengths = page_object.word_lengths(text)
        print("The following is a list of word lengths by frequency, thus: (<wordlength>,<frequency>)")
        print(word_lengths)
        #generate our JSON for the wordcloud
        print("Generating the JSON, may take a few seconds...")
        page_object.generate_json(word_lengths, "Word Lengths", 150, 20) # optionally add the font sizes
        print("Open",filename,"in the browser to see the wordcloud. Trying to open...")
        webbrowser.open('file://' + os.path.realpath(filename))

    else:
        print("Please input 0,1,2 or 3")
        continue
