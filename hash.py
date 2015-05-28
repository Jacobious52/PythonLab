import hashlib
import sys

def sha1hash(s):
	return hashlib.sha1(s.encode('utf-8')).hexdigest()

def md5hash(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

def main():
	args = sys.argv

	if len(args) == 3:
		switch = args[1]
		string = args[2]

		if switch == "md5":
			print("{0} : {1}".format(string, md5hash(string)))
		elif switch == "sha1":
			print("{0} : {1}".format(string, sha1hash(string)))

if __name__ == '__main__':
	main()