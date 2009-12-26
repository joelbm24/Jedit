import wx
from wx import *

class jedit(wx.Frame):
	def __init__(self, parent, ID, title):
		wx.Frame.__init__(self, parent, ID, title, size=(640, 480))
		panel = wx.Panel(self, -1)

		fileMenu = wx.Menu()
		fileMenu.Append(1, 'New')
		fileMenu.Append(2, 'Open')
		fileMenu.Append(3, 'Save')

		editMenu = wx.Menu()
		editMenu.Append(1, 'Cut')
		editMenu.Append(2, 'Copy')
		editMenu.Append(3, 'Paste')

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, 'File')
		menuBar.Append(editMenu, 'Edit')
		self.SetMenuBar(menuBar)

		self.text = wx.TextCtrl(panel, -1,'',(0,0),(640,457), style = wx.TE_MULTILINE|wx.HSCROLL)
		self.Show(True)

app = wx.App()
jedit(None, -1, 'Jedit')
app.MainLoop()
