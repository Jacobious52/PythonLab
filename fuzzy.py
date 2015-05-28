from fuzzywuzzy import process
names = ['jacob', 'luisa', 'lily']
print(process.extractOne('jacov', names))