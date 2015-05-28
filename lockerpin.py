import hash
import itertools
 
for combination in itertools.product(xrange(10), repeat=4):
	pin = ''.join(map(str, combination))
   	hashed = hash.md5hash('%s%s' % (pin, 'oPL4oPoCqxGPnh')) #add salt
	if hashed == 'b22e1c623159edd4f3d8e5d0bcf49d70': #check against hash
		print pin
		break