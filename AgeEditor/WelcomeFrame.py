# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May  5 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class WelcomeFrame
###########################################################################

class WelcomeFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome to the Ilathid Age Editor v.0.1", pos = wx.DefaultPosition, size = wx.Size( 650,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Please select the age directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.label1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"To create a new age, simply select an empty directory bearing the name of the age", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		bSizer9.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"This is beta software, please keep backups of anything important you work on!!", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 40, 40 ) )
		
		bSizer9.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_ageDirPicker = wx.DirPickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL )
		bSizer9.Add( self.m_ageDirPicker, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.LEFT|wx.RIGHT, 35 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_okBtn = wx.Button( self.m_panel5, wx.ID_ANY, u"Create/Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_okBtn.SetDefault() 
		bSizer9.Add( self.m_okBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer9 )
		self.m_panel5.Layout()
		bSizer9.Fit( self.m_panel5 )
		bSizer8.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_okBtn.Bind( wx.EVT_BUTTON, self.onAgeFolderSelected )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onAgeFolderSelected( self, event ):
		event.Skip()
	

