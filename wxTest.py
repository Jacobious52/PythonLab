import wx

class TestWindow(wx.Frame):
	def __init__(self, *args, **kargs):
		super(TestWindow, self).__init__(*args, **kargs)
		self.initUI()

	def initUI(self):
		menubar = wx.MenuBar()
		filemenu = wx.Menu()
		fitem = filemenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
		menubar.Append(filemenu, '&File')
		self.SetMenuBar(menubar)

		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

		self.SetSize((300, 200))
		self.SetTitle('MenuTest')
		self.Centre()
		self.Show(True)

	def OnQuit(self, e):
		self.Close()

def main():
	app = wx.App()
	TestWindow(None)
	app.MainLoop()

if __name__ == '__main__':
	main()