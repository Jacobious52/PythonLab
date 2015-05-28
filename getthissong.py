#!/usr/bin/env python
import urllib
import requests
import re
import pafy
import webbrowser
import subprocess

ascript = '''
tell application \"iTunes\"
	name of current track & \" - \" & artist of current track
end tell
'''
n = ''
p = subprocess.Popen(
        ['/usr/bin/osascript', '-e ' + ascript], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE)
out, err = p.communicate(ascript)
if p.returncode:
    print 'ERROR:', err
else:
    n = out
r = requests.get('https://www.youtube.com/results?search_query='+urllib.quote_plus(n))
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', r.text)
v = pafy.new(search_results[0])
bestaudio = v.getbestaudio()
webbrowser.open_new_tab(bestaudio.url)