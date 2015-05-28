import socket
import struct

class client(object):
	"""docstring for Client"""
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

	def us32int(self, value):
		return struct.pack('I', value)

	def us32int_for_str(self, text):
		return self.us32int(len(text))

	def send(self, msg):
		try:
			self.sock.send(self.us32int_for_str(msg))
			self.sock.send(msg)
		except:
			self.disconnect()

	def recv(self):
		try:
			data = self.sock.recv(4)
			length = struct.unpack('I', data)[0]
			msg = ''
			while len(msg) < length:
				read = self.sock.recv(length - len(msg))
				if read is None:
					break
				msg += read
			return msg
		except:
			return 'timeout from server'

	def disconnect(self):
		self.sock.close()