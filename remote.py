import requests
import re

MAGNET_URL = 'magnet:?xt=urn:btih:a48e6202c171224693dafcc0c112ed9952fe9b82&dn=J.R.R.+Tolkien+-+The+Silmarillion&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337'
SERVER_URL = 'http://10.0.1.7:8080/gui'
AUTH = requests.auth.HTTPBasicAuth('admin','admin')
TOKEN = ''
COOKIES = {}

def extract_token(html):
	return re.search(r'<div[^>]*id=[\"\']token[\"\'][^>]*>([^<]*)</div>', html).group(1)

def main():
	#first connect and get token for later use
	r = requests.get('%s/token.html' % SERVER_URL, auth=AUTH)
	COOKIES = r.cookies.get_dict()
	TOKEN = extract_token(r.text)

	#add torrent url
	params = {	'action': 'add-url',
				'token': TOKEN,
				's': MAGNET_URL
			 }
	r = requests.get(SERVER_URL, auth=AUTH, cookies=COOKIES, params=params)
	print(r.json)
if __name__ == '__main__':
	main()