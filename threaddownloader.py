import threading
import requests

test_url = 'http://mirror.internode.on.net/pub/test/100meg.test'

parts = {}
def download(url, start, chunk):
	print(str(start) + ' getting')
	r = requests.get(url, headers={'Range':'bytes=%s-%s' % (start, start+chunk)})
	print(str(start) + ' done')
	parts[start] = r.content

def main():
	r = requests.get(test_url, stream=True)
	length = int(r.headers['content-length'])
	chunk_size = length / 10
	left_over = length % 10

	threads = []

	for i in xrange(0,10):
		t = threading.Thread(target=download, args=(test_url, i*chunk_size, chunk_size))
		t.start()
		threads.append(t)

	t = threading.Thread(target=download, args=(test_url, i*chunk_size, left_over))
	t.start()
	threads.append(t)

	print('waiting for join')

	for t in threads:
		t.join()

	print('joined.. combining')

	data = ''
	for i in xrange(0,len(threads)-1):
		data += parts[i*chunk_size]

	print('writing')

	with open('/Users/Jacob/Downloads/10meg.test', 'wb') as f:
		f.write(data)

	print('done all')

if __name__ == '__main__':
	main()