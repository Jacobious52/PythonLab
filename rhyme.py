import requests
from bs4 import BeautifulSoup
import sys

print ("Powered by www.rhymezone.com\n")

def pretty_print(CL_output):
    columns = len(CL_output)//100+2
    lines = ("".join(s.ljust(20) for s in CL_output[i:i+columns-1])+CL_output[i:i+columns][-1] for i in range(0, len(CL_output), columns))
    return "\n".join(lines)

if len(sys.argv) != 2:
	print('usage: rhyme <word>')
	sys.exit()

url = 'http://www.rhymezone.com/r/rhyme.cgi'
word = sys.argv[1]

r = requests.get(url, params={'Word':word, 'typeofrhyme':'perfect'})
soup = BeautifulSoup(r.text.decode('utf-8'))

rhymes = []

for link in soup.find_all('a'):
	href = link.get('href')
	if href.startswith('d='):
		href_parts = href.split('=')
		if len(href_parts) is not 2:
			continue
		if not '_' in href_parts[1]:
			rhymes.append(href_parts[1])

print (pretty_print(rhymes))