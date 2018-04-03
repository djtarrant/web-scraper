from urllib import urlopen
from bs4 import BeautifulSoup
import ssl
import re

def url_scrape(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    for script in html(["script", "style"]):
        script.extract() # Remove these two elements from the BeautifulSoup object
