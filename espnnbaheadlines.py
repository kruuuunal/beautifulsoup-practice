#Use BeautifulSoup to extract headlines from www.espn.com/nba

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.espn.com/nba"

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll("h1")

for each in tags:
    print (each.text)