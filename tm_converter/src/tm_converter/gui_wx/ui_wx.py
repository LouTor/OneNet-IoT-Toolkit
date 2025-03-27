# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
###########################################################################
## Class Frame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"物模型转换工具", pos = wx.DefaultPosition, size = wx.Size( 425,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		frameSizer = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainSizer = wx.BoxSizer( wx.VERTICAL )

		sizerRoll1 = wx.BoxSizer( wx.HORIZONTAL )

		self.textVersion = wx.StaticText( self.mainPanel, wx.ID_ANY, u"选择版本：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textVersion.Wrap( -1 )

		sizerRoll1.Add( self.textVersion, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choVersion1Choices = [u"自动检测源版本", u"融合平台(开放平台)", u"城市平台v1.2", u"城市平台v2.x", u"城市平台v3.0"]
		self.choVersion1 = wx.Choice( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), choVersion1Choices, 0 )
		self.choVersion1.SetSelection( 0 )
		sizerRoll1.Add( self.choVersion1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textTrans = wx.StaticText( self.mainPanel, wx.ID_ANY, u"——>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textTrans.Wrap( -1 )

		self.textTrans.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		sizerRoll1.Add( self.textTrans, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choVersion2Choices = [u"融合平台(开放平台)", u"城市平台v1.2", u"城市平台v2.x", u"城市平台v3.0"]
		self.choVersion2 = wx.Choice( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), choVersion2Choices, 0 )
		self.choVersion2.SetSelection( 0 )
		sizerRoll1.Add( self.choVersion2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		mainSizer.Add( sizerRoll1, 1, wx.EXPAND, 5 )

		sizerRoll2 = wx.BoxSizer( wx.HORIZONTAL )

		self.textModel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"模型文件：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textModel.Wrap( -1 )

		sizerRoll2.Add( self.textModel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CtextModPath = wx.TextCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerRoll2.Add( self.CtextModPath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.butnModPath = wx.Button( self.mainPanel, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.butnModPath.SetMaxSize( wx.Size( 20,-1 ) )

		sizerRoll2.Add( self.butnModPath, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.butnTrans = wx.Button( self.mainPanel, wx.ID_ANY, u"开始转换", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerRoll2.Add( self.butnTrans, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		mainSizer.Add( sizerRoll2, 1, wx.EXPAND, 5 )

		sizerRoll3 = wx.BoxSizer( wx.HORIZONTAL )

		self.textSave = wx.StaticText( self.mainPanel, wx.ID_ANY, u"保存路径：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textSave.Wrap( -1 )

		sizerRoll3.Add( self.textSave, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CtextSavePath = wx.TextCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerRoll3.Add( self.CtextSavePath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.butnOpenFile = wx.Button( self.mainPanel, wx.ID_ANY, u"打开转换后文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerRoll3.Add( self.butnOpenFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		mainSizer.Add( sizerRoll3, 1, wx.EXPAND, 5 )


		self.mainPanel.SetSizer( mainSizer )
		self.mainPanel.Layout()
		mainSizer.Fit( self.mainPanel )
		frameSizer.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( frameSizer )
		self.Layout()
		self.menu = wx.MenuBar( 0 )
		self.menuHelp = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"说明文档", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuHelp.Append( self.m_menuItem5 )

		self.m_menuItem4 = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"检查更新", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuHelp.Append( self.m_menuItem4 )

		self.menu.Append( self.menuHelp, u"帮助" )

		self.menuFeedback = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.menuFeedback, wx.ID_ANY, u"意见建议", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFeedback.Append( self.m_menuItem3 )

		self.menu.Append( self.menuFeedback, u"反馈" )

		self.SetMenuBar( self.menu )


		self.Centre( wx.BOTH )

		# Connect Events
		self.butnModPath.Bind( wx.EVT_BUTTON, self.SelectFilePath )
		self.butnTrans.Bind( wx.EVT_BUTTON, self.StartConvert )
		self.butnOpenFile.Bind( wx.EVT_BUTTON, self.openFile )
		self.Bind( wx.EVT_MENU, self.help_document, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.help_downloadAddress, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.suggestion, id = self.m_menuItem3.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SelectFilePath( self, event ):
		event.Skip()

	def StartConvert( self, event ):
		event.Skip()

	def openFile( self, event ):
		event.Skip()

	def help_document( self, event ):
		event.Skip()

	def help_downloadAddress( self, event ):
		event.Skip()

	def suggestion(self, event):
		event.Skip()



