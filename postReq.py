import requests as r
name = raw_input('Name: ')
req = r.post('http://localhost:8000', data=name)
print(req.text)
print('===================\n\n')
req = r.get('http://localhost:8000')
print req.text