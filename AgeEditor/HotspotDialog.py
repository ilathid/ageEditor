# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 17 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class HotspotDialog
###########################################################################

class HotspotDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hotspot Settings", pos = wx.DefaultPosition, size = wx.Size( 1050,600 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		verticalSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Cursor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_cursorPopupContainer = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_cursorPopupContainer, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_action = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_action.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer1.Add( self.m_action, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Destination", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_destinationChoiceChoices = []
		self.m_destinationChoice = wx.ComboBox( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_destinationChoiceChoices, 0 )
		bSizer2.Add( self.m_destinationChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_selectFromMapBtn = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"data/map.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.m_selectFromMapBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		verticalSizer.Add( self.m_panel2, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Orientation on destination", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		verticalSizer.Add( self.m_staticText5, 0, wx.LEFT, 15 )
		
		self.m_orientation_preview = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_orientation_preview.SetMinSize( wx.Size( -1,256 ) )
		self.m_orientation_preview.SetMaxSize( wx.Size( -1,256 ) )
		
		verticalSizer.Add( self.m_orientation_preview, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Delete this hotspot", wx.DefaultPosition, wx.DefaultSize, 0 )
		verticalSizer.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_okBtn = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_okBtn.SetDefault() 
		verticalSizer.Add( self.m_okBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		
		self.SetSizer( verticalSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_destinationChoice.Bind( wx.EVT_COMBOBOX, self.onSelectDestination )
		self.m_destinationChoice.Bind( wx.EVT_TEXT, self.onSelectDestination )
		self.m_destinationChoice.Bind( wx.EVT_TEXT_ENTER, self.onSelectDestination )
		self.m_selectFromMapBtn.Bind( wx.EVT_BUTTON, self.onSelectFromMap )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onDeleteHotspot )
		self.m_okBtn.Bind( wx.EVT_BUTTON, self.onOKButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectDestination( self, event ):
		event.Skip()
	
	
	
	def onSelectFromMap( self, event ):
		event.Skip()
	
	def onDeleteHotspot( self, event ):
		event.Skip()
	
	def onOKButton( self, event ):
		event.Skip()
	

