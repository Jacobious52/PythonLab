
import pafy
import webbrowser
import sys
from getpass import getuser

header = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Video Links</title>
</head>
<body>
<strong>%s</strong>
<p>%s</p>
<p><img name="Thumbnail" src="%s" width="120" height="90"/></p>
'''
#1 - title
#2 - description
#3 - thumb url

footer = '''
</body>
</html>
'''

temp_file = '/Users/%s/Library/Caches/TemporaryItems/linkstemp.html' % getuser()

video_url = sys.argv[1]
video = pafy.new(video_url)

title = video.title
description = video.description
thumb = video.bigthumb

html_file = open(temp_file, 'w')
html_file.write(header % (title, description, thumb))

div_tag = '<div>%s - <a href="%s">%s - %s</a></div>\n'
#1 - type
#2 - url
#3 - ext
#4 - quality

for stream in video.allstreams:
	html_file.write(div_tag % (stream.mediatype, stream.url, stream.extension, stream.quality))	

html_file.write(footer)
html_file.close()

webbrowser.open_new_tab('file://%s' % temp_file)
