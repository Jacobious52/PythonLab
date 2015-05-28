from fuzzywuzzy import process

words = []

with open('wordsEn.txt') as f:
	words = f.readlines()

inp = 'teh one who requierd to exterminat everone frrom existince'

inwords = inp.split(' ')

outwords = ''

for w in inwords:
	print('correcting %s' % w)
	outwords += process.extractOne(w, words)[0]

print outwords