import json

variables = {'@win': 'C:\\Windows',
			 '@sys': 'C:\\Windows\\system32',
			 '@yas': '10.71.36',
			 ' '   : '&',
			 '_'   : ' ',
			 '`'   : '{BACKSPACE}'}

with open('test.json', 'w') as f:
	json.dump(variables, f)

v = {}

with open('test.json', 'r') as f:
	v = json.load(f)

print v