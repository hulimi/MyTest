#-*- coding: utf-8 -*-

"""
demo: print "hello world"
"""
import wx
print "wx.version: ", wx.version()
print "hello world"

#class MainPanel(wx.Panel)
#	def __init__(self):
#		wx.Frame.__init__(self, None, -1, "Main Frame", size = (300, 400))

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "Main Frame", size = (300, 400))
	
	def __init__(self, title):
		wx.Frame.__init__(self, None, -1, title, size = (300, 400))

	def __init__(self, title, size):
		wx.Frame.__init__(self, None, -1, title, size)
			
	def createButton(self, text, size, enable = True):
		print self, text, size, enable
		self.button = wx.Button(self, -1,text, size)
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()
	
	def OnClick(self, event):
		if self.button.GetLabel() == "stop":
			self.button.SetLabel("start")
		elif self.button.GetLabel() == "start":	
			self.button.SetLabel("stop")

	
def main():
	app = wx.PySimpleApp()
	main_frame = MainFrame("hello world",(500, 500))
	main_frame.Show(True)
	main_frame.createButton("start",(20, 10))
	app.MainLoop()
		
if __name__ == '__main__':
	main()
