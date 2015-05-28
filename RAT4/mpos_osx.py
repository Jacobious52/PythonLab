from Cocoa import NSEvent

class Point(object):
	def __init__(self, x, y):
		self.X = x
		self.Y = y

def get_mouse_pos():
	return Point(NSEvent.mouseLocation().x, NSEvent.mouseLocation().y)