#Use BeautifulSoup to extract the opening price of Facebook stock from Yahoo Finance.

from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://finance.yahoo.com/quote/FB?p=FB"

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tag = soup.find('div', id="quote-summary").div.table.tbody

tag1 = tag.findAll('tr')
tag2 = tag1[1]
tag3 = tag2.findAll('td')
tag4 = tag3[1]

print (tag4.text)
       
       
       #.span['class'])