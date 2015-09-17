# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May  5 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

ID_REMOVE_STANDPOINT = 1000
ID_MAP_TOOL = 1001
wx.ID_SAVE_TOOL = 1002

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ilathid Age Editor", pos = wx.DefaultPosition, size = wx.Size( 1600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ageSlidesPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_standpointsSplitter = wx.SplitterWindow( self.m_ageSlidesPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DSASH|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.m_standpointsSplitter.SetSashGravity( 0 )
		self.m_standpointsSplitter.Bind( wx.EVT_IDLE, self.m_standpointsSplitterOnIdle )
		self.m_standpointsSplitter.SetMinimumPaneSize( 300 )
		
		self.leftPanel = wx.Panel( self.m_standpointsSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		leftSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar = wx.ToolBar( self.leftPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar.SetToolBitmapSize( wx.Size( 32,32 ) )
		self.m_toolBar.AddLabelTool( ID_REMOVE_STANDPOINT, u"Delete standpoint", wx.Bitmap( u"data/icon_remove.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Delete standpoint", wx.EmptyString, None ) 
		
		self.m_toolBar.AddLabelTool( ID_MAP_TOOL, u"Select Map", wx.Bitmap( u"data/map.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Select Map", wx.EmptyString, None ) 
		
		self.m_toolBar.AddLabelTool( wx.ID_SAVE_TOOL, u"Save", wx.Bitmap( u"data/icon_save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar.Realize() 
		
		leftSizer.Add( self.m_toolBar, 0, wx.EXPAND, 5 )
		
		
		self.leftPanel.SetSizer( leftSizer )
		self.leftPanel.Layout()
		leftSizer.Fit( self.leftPanel )
		self.m_panel3 = wx.Panel( self.m_standpointsSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetMinSize( wx.Size( 10,10 ) )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Standpoint Properties" ), wx.VERTICAL )
		
		sbSizer1.SetMinSize( wx.Size( 5,5 ) ) 
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1.SetMinSize( wx.Size( 5,5 ) ) 
		self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_standpointName = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_standpointName.Enable( False )
		self.m_standpointName.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer7.Add( self.m_standpointName, 0, wx.ALL, 5 )
		
		self.m_saveNameBtn = wx.Button( self.m_panel3, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_saveNameBtn.Enable( False )
		
		bSizer7.Add( self.m_saveNameBtn, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Type :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 15 )
		
		self.m_standpointType = wx.StaticText( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_standpointType.Wrap( -1 )
		self.m_standpointType.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer7.Add( self.m_standpointType, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		
		fgSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_fileList = wx.grid.Grid( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.m_fileList.CreateGrid( 6, 2 )
		self.m_fileList.EnableEditing( True )
		self.m_fileList.EnableGridLines( True )
		self.m_fileList.EnableDragGridSize( False )
		self.m_fileList.SetMargins( 0, 0 )
		
		# Columns
		self.m_fileList.SetColSize( 0, 250 )
		self.m_fileList.SetColSize( 1, 250 )
		self.m_fileList.EnableDragColMove( False )
		self.m_fileList.EnableDragColSize( True )
		self.m_fileList.SetColLabelSize( 30 )
		self.m_fileList.SetColLabelValue( 0, u"Filename" )
		self.m_fileList.SetColLabelValue( 1, u"Archive" )
		self.m_fileList.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_fileList.EnableDragRowSize( True )
		self.m_fileList.SetRowLabelSize( 80 )
		self.m_fileList.SetRowLabelValue( 0, u"North" )
		self.m_fileList.SetRowLabelValue( 1, u"East" )
		self.m_fileList.SetRowLabelValue( 2, u"South" )
		self.m_fileList.SetRowLabelValue( 3, u"West" )
		self.m_fileList.SetRowLabelValue( 4, u"Top" )
		self.m_fileList.SetRowLabelValue( 5, u"Bottom" )
		self.m_fileList.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_fileList.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer1.Add( self.m_fileList, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"On entrance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_onEntrance = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_onEntrance, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"On Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer6.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_onExit = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_onExit, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_startCheckbox = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Age starts here", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_startCheckbox, 0, wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_rectangleTool = wx.BitmapButton( self.m_panel3, wx.ID_ANY, wx.Bitmap( u"data/tool_rectangle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_rectangleTool.SetBackgroundColour( wx.Colour( 86, 155, 228 ) )
		
		bSizer10.Add( self.m_rectangleTool, 0, wx.ALL, 5 )
		
		self.m_polygonTool = wx.BitmapButton( self.m_panel3, wx.ID_ANY, wx.Bitmap( u"data/tool_polygon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer10.Add( self.m_polygonTool, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		self.m_slideImages = wx.ScrolledWindow( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_slideImages.SetScrollRate( 5, 5 )
		self.m_slideImages.SetMinSize( wx.Size( 10,10 ) )
		
		sbSizer1.Add( self.m_slideImages, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( sbSizer1 )
		self.m_panel3.Layout()
		sbSizer1.Fit( self.m_panel3 )
		self.m_standpointsSplitter.SplitVertically( self.leftPanel, self.m_panel3, 500 )
		bSizer3.Add( self.m_standpointsSplitter, 1, wx.EXPAND, 5 )
		
		
		self.m_ageSlidesPanel.SetSizer( bSizer3 )
		self.m_ageSlidesPanel.Layout()
		bSizer3.Fit( self.m_ageSlidesPanel )
		self.m_notebook1.AddPage( self.m_ageSlidesPanel, u"Standpoints", True )
		self.ageSettingsTab = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.ageSettingsTab, wx.ID_ANY, u"Movie files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer8.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_addMovieBt = wx.BitmapButton( self.ageSettingsTab, wx.ID_ANY, wx.Bitmap( u"data/icon_add_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer8.Add( self.m_addMovieBt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer71.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_moviesList = wx.grid.Grid( self.ageSettingsTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_moviesList.CreateGrid( 0, 4 )
		self.m_moviesList.EnableEditing( True )
		self.m_moviesList.EnableGridLines( True )
		self.m_moviesList.EnableDragGridSize( False )
		self.m_moviesList.SetMargins( 0, 0 )
		
		# Columns
		self.m_moviesList.SetColSize( 0, 200 )
		self.m_moviesList.SetColSize( 1, 200 )
		self.m_moviesList.SetColSize( 2, 200 )
		self.m_moviesList.SetColSize( 3, 200 )
		self.m_moviesList.EnableDragColMove( False )
		self.m_moviesList.EnableDragColSize( True )
		self.m_moviesList.SetColLabelSize( 30 )
		self.m_moviesList.SetColLabelValue( 0, u"Identifier" )
		self.m_moviesList.SetColLabelValue( 1, u"Filename" )
		self.m_moviesList.SetColLabelValue( 2, u"Position" )
		self.m_moviesList.SetColLabelValue( 3, u"onEnd script" )
		self.m_moviesList.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_moviesList.EnableDragRowSize( True )
		self.m_moviesList.SetRowLabelSize( 80 )
		self.m_moviesList.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_moviesList.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_moviesList.SetMinSize( wx.Size( -1,200 ) )
		self.m_moviesList.SetMaxSize( wx.Size( -1,200 ) )
		
		bSizer71.Add( self.m_moviesList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer71.AddSpacer( ( 15, 15), 0, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.ageSettingsTab, wx.ID_ANY, u"Music files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer9.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_addMusicBtn = wx.BitmapButton( self.ageSettingsTab, wx.ID_ANY, wx.Bitmap( u"data/icon_add_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_addMusicBtn, 0, wx.ALL, 5 )
		
		
		bSizer71.Add( bSizer9, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_musicsList = wx.grid.Grid( self.ageSettingsTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_musicsList.CreateGrid( 0, 3 )
		self.m_musicsList.EnableEditing( True )
		self.m_musicsList.EnableGridLines( True )
		self.m_musicsList.EnableDragGridSize( False )
		self.m_musicsList.SetMargins( 0, 0 )
		
		# Columns
		self.m_musicsList.SetColSize( 0, 200 )
		self.m_musicsList.SetColSize( 1, 200 )
		self.m_musicsList.SetColSize( 2, 200 )
		self.m_musicsList.EnableDragColMove( False )
		self.m_musicsList.EnableDragColSize( True )
		self.m_musicsList.SetColLabelSize( 30 )
		self.m_musicsList.SetColLabelValue( 0, u"Identifier" )
		self.m_musicsList.SetColLabelValue( 1, u"Filename" )
		self.m_musicsList.SetColLabelValue( 2, u"Volume" )
		self.m_musicsList.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_musicsList.EnableDragRowSize( True )
		self.m_musicsList.SetRowLabelSize( 80 )
		self.m_musicsList.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_musicsList.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_musicsList.SetMinSize( wx.Size( -1,200 ) )
		self.m_musicsList.SetMaxSize( wx.Size( -1,200 ) )
		
		bSizer71.Add( self.m_musicsList, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.ageSettingsTab.SetSizer( bSizer71 )
		self.ageSettingsTab.Layout()
		bSizer71.Fit( self.ageSettingsTab )
		self.m_notebook1.AddPage( self.ageSettingsTab, u"Age Settings", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar = wx.MenuBar( 0 )
		self.m_fileMenu = wx.Menu()
		self.m_menuSave = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Save"+ u"\t" + u"ctrl-S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_menuSave )
		
		self.m_generatePyMenu = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Generate Python file", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_generatePyMenu )
		
		self.m_menuExit = wx.MenuItem( self.m_fileMenu, wx.ID_ANY, u"Exit"+ u"\t" + u"ctrl-Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_fileMenu.AppendItem( self.m_menuExit )
		
		self.m_menubar.Append( self.m_fileMenu, u"File" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.Bind( wx.EVT_TOOL, self.onDeleteStandpoint, id = ID_REMOVE_STANDPOINT )
		self.Bind( wx.EVT_TOOL, self.onSelectMap, id = ID_MAP_TOOL )
		self.Bind( wx.EVT_TOOL, self.onSave, id = wx.ID_SAVE_TOOL )
		self.m_standpointName.Bind( wx.EVT_TEXT, self.onStandpointNameEdited )
		self.m_standpointName.Bind( wx.EVT_TEXT_ENTER, self.onSaveStandpointName )
		self.m_saveNameBtn.Bind( wx.EVT_BUTTON, self.onSaveStandpointName )
		self.m_fileList.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.onGridEdited )
		self.m_fileList.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.onGridCellRightClick )
		self.m_fileList.Bind( wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.onGridCellRightClick )
		self.m_onEntrance.Bind( wx.EVT_TEXT, self.onEntranceScriptEdited )
		self.m_onEntrance.Bind( wx.EVT_TEXT_ENTER, self.onEntranceScriptEdited )
		self.m_onExit.Bind( wx.EVT_TEXT, self.onExitScriptEdited )
		self.m_onExit.Bind( wx.EVT_TEXT_ENTER, self.onExitScriptEdited )
		self.m_startCheckbox.Bind( wx.EVT_CHECKBOX, self.onStartCheckbox )
		self.m_rectangleTool.Bind( wx.EVT_BUTTON, self.onSelectToolRectangle )
		self.m_polygonTool.Bind( wx.EVT_BUTTON, self.onSelectToolPolygon )
		self.m_addMovieBt.Bind( wx.EVT_BUTTON, self.onAddMovie )
		self.m_moviesList.Bind( wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.moviesListRightClick )
		self.m_addMusicBtn.Bind( wx.EVT_BUTTON, self.onAddMusic )
		self.m_musicsList.Bind( wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.musicListRightClick )
		self.Bind( wx.EVT_MENU, self.onSave, id = self.m_menuSave.GetId() )
		self.Bind( wx.EVT_MENU, self.onGeneratePython, id = self.m_generatePyMenu.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.m_menuExit.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()
	
	def onDeleteStandpoint( self, event ):
		event.Skip()
	
	def onSelectMap( self, event ):
		event.Skip()
	
	def onSave( self, event ):
		event.Skip()
	
	def onStandpointNameEdited( self, event ):
		event.Skip()
	
	def onSaveStandpointName( self, event ):
		event.Skip()
	
	
	def onGridEdited( self, event ):
		event.Skip()
	
	def onGridCellRightClick( self, event ):
		event.Skip()
	
	
	def onEntranceScriptEdited( self, event ):
		event.Skip()
	
	
	def onExitScriptEdited( self, event ):
		event.Skip()
	
	
	def onStartCheckbox( self, event ):
		event.Skip()
	
	def onSelectToolRectangle( self, event ):
		event.Skip()
	
	def onSelectToolPolygon( self, event ):
		event.Skip()
	
	def onAddMovie( self, event ):
		event.Skip()
	
	def moviesListRightClick( self, event ):
		event.Skip()
	
	def onAddMusic( self, event ):
		event.Skip()
	
	def musicListRightClick( self, event ):
		event.Skip()
	
	
	def onGeneratePython( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	
	def m_standpointsSplitterOnIdle( self, event ):
		self.m_standpointsSplitter.SetSashPosition( 500 )
		self.m_standpointsSplitter.Unbind( wx.EVT_IDLE )
	

