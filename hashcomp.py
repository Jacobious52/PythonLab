from hashlib import md5
import sys

def md5hash(s):
	return md5(s.encode('utf-8')).hexdigest()

def hashfile(fname):
	hashes = []
	with open(fname, 'r') as f:
		lines = [l.rstrip() for l in f]
		count = 0
		length = len(lines)
		for line in lines[::-1]:
			count = count + 1
			sys.stdout.flush()
			print('{0}/{1}'.format(count, length), end='\r')
			hashes.append((md5hash(line), line))
	return hashes

def main():
		try:
			hashes = hashfile("hashes.txt")
			with open('hashtabble.txt', 'w') as f:
				for h in hashes:
					f.write('%s:%s\n' % h)
		except KeyboardInterrupt:
			print("operation cancelled by user")

if __name__ == '__main__':
	main()