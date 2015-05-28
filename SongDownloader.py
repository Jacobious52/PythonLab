
import pafy
import requests
import sys
from getpass import getuser

class URLDownloader(object):
	"""docstring for URLDownloader"""
	def __init__(self, download_url, save_path):
		super(URLDownloader, self).__init__()
		self.download_url = download_url
		self.save_path = save_path

	def download(self):
		r = requests.get(self.download_url, stream=True)
		length = r.headers['content-length']
		downloaded = 0
		print('\n==================================\nInitialising Download\n')
		with open(self.save_path, 'wb') as f:
			for buff in r.iter_content(chunk_size=1024):
				f.write(buff)
				f.flush()
				downloaded += 1024
				sys.stdout.write('\r%s/%s bytes                                 ' % (str(downloaded), length))
				sys.stdout.flush()
		print('\n=========================================\nDownload Complete')
		

class SongDownloader(object):
	"""docstring for SongDownloader"""
	def __init__(self, youtube_url):
		super(SongDownloader, self).__init__()
		self.VIDEO_PATH = '/users/%s/music' % getuser()
		self.youtube_url = youtube_url
		self.video = pafy.new(self.youtube_url)

	def get_audio_streams(self):
		return self.video.audiostreams

	def get_video_info(self):
		return '%s - %s - %s' % (self.video.title, self.video.author, self.video.duration)

	def download(self, stream=None, save_path=None):
		if not stream:
			stream = self.video.getbestaudio()
		if not save_path:
			save_path = '%s/%s.%s' % (self.VIDEO_PATH, self.video.title, stream.extension)
		
		downloader = URLDownloader(stream.url, save_path)
		downloader.download()

def main():
	if len(sys.argv) != 2:
		return

	url = sys.argv[1]
	song_downloader = SongDownloader(url)
	print('\n=====================================================================\n%s\n===================================================================\n' % song_downloader.get_video_info())

	song_downloader.download()

if __name__ == '__main__':
	main()