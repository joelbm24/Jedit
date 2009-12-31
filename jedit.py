import wx
from wx import *

class jedit(wx.Frame):
	def __init__(self, parent, ID, title):
		wx.Frame.__init__(self, parent, ID, title, size=(640, 480))

		fileMenu = wx.Menu()
		fileMenu.Append(1, '&New\tCtrl+N', 'New')
		fileMenu.Append(2, '&Open\tCtrl+O', 'Open')
		fileMenu.Append(3, '&Save\tCtrl+S', 'Save')
		fileMenu.Append(9, 'Save As\tShift+Ctrl+S', 'Save As')

		editMenu = wx.Menu()
		editMenu.Append(4, 'Cut\tCtrl+X', 'Cut')
		editMenu.Append(5, '&Copy\tCtrl+C', 'Copy')
		editMenu.Append(6, 'Paste\tCtrl+V', 'Paste')
		editMenu.Append(7, 'Select &All\tCtrl+A', 'Select All')

		helpMenu = wx.Menu()
		helpMenu.Append(8, 'About')

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, 'File')
		menuBar.Append(editMenu, 'Edit')
		menuBar.Append(helpMenu, 'Help')
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.onNew, id=1)
		self.Bind(wx.EVT_MENU, self.onOpen, id=2)
		self.Bind(wx.EVT_MENU, self.onSave, id=3)
		self.Bind(wx.EVT_MENU, self.onCut, id=4)
		self.Bind(wx.EVT_MENU, self.onCopy, id=5)
		self.Bind(wx.EVT_MENU, self.onPaste, id=6)
		self.Bind(wx.EVT_MENU, self.onSelAll, id=7)
		self.Bind(wx.EVT_MENU, self.onAbout, id=8)
		self.Bind(wx.EVT_MENU, self.onSaveAs, id=9)
		

		self.text = wx.TextCtrl(self, -1,'',(0,0),(640,457), wx.TE_MULTILINE|wx.HSCROLL)
		self.Centre()
		self.Show(True)

	def onAbout(self, event):
		aboutBox = wx.MessageBox('Program: Jedit\nAuthor: Joel Moore\nLisence: GPLv3','About', wx.OK)
	def onPaste(self, event):
		self.text.Paste()
	def onCopy(self, event):
		self.text.Copy()
	def onCut(self, event):
		self.text.Cut()
	def onSelAll(self, event):
		self.text.SelectAll()
	def onOpen(self, event):
		fileOpen = wx.FileDialog(self, "Open a file",'.','', 'File (*.*)|*.*| Python (*.py)|*.py', wx.OPEN)
		fileOpen.ShowModal()
		global filePath
		filePath = fileOpen.GetPath()
		self.text.LoadFile(fileOpen.GetPath())
	def onSaveAs(self, event):
		fileSaveAs = wx.FileDialog(self, "Save as",'.','', 'File (*.*)|*.*| Python (*.py)|*.py', wx.SAVE)
		fileSaveAs.ShowModal()
		global filePath
		filePath = fileSaveAs.GetPath()
		self.text.SaveFile(fileSaveAs.GetPath())
	def onNew(self, event):
		global filePath
		filePath = ''
		self.text.Clear()
	def onSave(self, event):
		self.text.SaveFile(filePath)
		
app = wx.App()
jedit(None, -1, 'Jedit')
app.MainLoop()
