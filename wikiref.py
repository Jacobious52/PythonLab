from bs4 import BeautifulSoup
import requests
import time

url = "http://en.wikipedia.org/wiki/Viscosity"

r = requests.get(url)
soup = BeautifulSoup(r.text)

title = soup.title.find_all(text=True)[0]
time = time.strftime("%d/%m/%Y")
author = "Various Contributors"

last = soup.find('li', id='footer-info-lastmod').contents[0]

print('%s: %s, %s %s. Last Visited: %s' % (title, url, author, last[15:], time))