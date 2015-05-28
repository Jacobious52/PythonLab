class Torrent(object):
	"""docstring for Torrent"""

	def magnet_url_from_hash(self, hash):
		return "magnet:?xt=urn:btih:%s" % hash

	def __init__(self, title, size, seeders, leechers, magnet):
		self.title = title
		self.size = size
		self.seeders = seeders
		self.leechers = leechers
		self.magnet = magnet
		self.url = self.magnet_url_from_hash(self.magnet)

torrents = []

print ('loading torrents..\n')

with open('complete','r') as f:
	for line in f.readlines():
		line_split = line.split('|')
		if len(line_split) == 6:
			t = Torrent(line_split[1], line_split[2], line_split[3], line_split[4], line_split[5])
			torrents.append(t)

def search(name=""):
	i = 0
	for torrent in torrents:
		if name in torrent.title:
			print( "%s - %s | %s (MB)" % (i ,torrent.title, str(int(torrent.size) / 1024**2)))
		i+=1

def search_list(names=[]):
	i = 0
	for torrent in torrents:
		for name in names:
			if name in torrent.title:
				print( "%s - %s | %s (MB)" % (i ,torrent.title, str(int(torrent.size) / 1024**2)))
		i+=1

def look(torrent_id):
	torrent = torrents[torrent_id]
	print("Title: %s\nSize: %s (MB)\nSeeders: %s\nLeechers: %s\nMagnet:\n%s\n" %
		(torrent.title, str(int(torrent.size) / 1024**2), torrent.seeders, torrent.leechers, torrent.url))
