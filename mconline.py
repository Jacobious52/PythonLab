import requests
from bs4 import BeautifulSoup

r = requests.get('http://xpaw.ru/mcstatus/')
html = r.text

soup = BeautifulSoup(html)

print(soup.title)

print(soup.find('div', id="login"))

if 'Online' in html:
	print('Minecraft is Online')
else:
	print('Minecraft is Offline')