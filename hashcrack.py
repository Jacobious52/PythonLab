from hashlib import md5
import sys

def md5hash(s):
	return md5(s.encode('utf-8')).hexdigest()

def hashfile(fname, inhash):
	with open(fname, 'r') as f:
		lines = [l.rstrip() for l in f]
		count = 0
		length = len(lines)
		for line in lines[::-1]:
			count = count + 1
			sys.stdout.flush()
			print('{0}/{1}'.format(count, length), end='\r')
			if md5hash(line) == inhash:
				return line;
	return 'could not find hash'

def main():
	if len(sys.argv) == 2:
		text = sys.argv[1]
		print("\n")
		try:
			h = hashfile("hashes.txt", text)
			sys.stdout.flush()
			print("\n")
			print("found: {0}".format(h))
		except KeyboardInterrupt:
			print("operation cancelled by user")
if __name__ == '__main__':
	main()