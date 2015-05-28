import socket

class client(object):
	def __init__(self, ip, port, time):
		self.ip = ip
		self.port = port
		self.connected = False
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.settimeout(time)

	def connect(self):
		if self.sock.connect_ex((self.ip, self.port)) == 0:
			self.connected = True
		else:
			self.connected = False
		return self.connected

	def send(self, msg):
		self.sock.send(msg)

	def disconnect(self):
		self.sock.close()