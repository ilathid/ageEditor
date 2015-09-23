#!/usr/bin/env python
import wxversion
wxversion.select('2.9','3.0')
import wx
from IlathidAgeEditorWelcomeFrame import IlathidAgeEditorWelcomeFrame
import sys
import traceback
import wx.lib.dialogs

class MyApp (wx.App) :
    def OnInit (self) :
        sys.excepthook = _excepthook
        return True

def _excepthook (etype, value, tb) :
    traceback.print_exception(etype, value, tb)
    
    dlg = wx.lib.dialogs.ScrolledMessageDialog(None, "Oops, a problem occurred :( \n\nUnhandled exception of type '" + etype.__name__ + "' occurred :(\n\n" + str(value) + "\n" + ' '.join(traceback.format_tb(tb)), "Exception report")
    dlg.SetSize(wx.Size(1000, 600))
    dlg.Center()
    dlg.ShowModal()
    
    
    #wx.MessageBox("Oops, a problem of type '" + etype.__name__ + "' occurred :(\n\n" + str(value) + "\n" + ' '.join(traceback.format_tb(tb)))
    #sys.stderr.write(traceback)
    
app = MyApp(False)  # Create a new app, don't redirect stdout/stderr to a window.

frame = IlathidAgeEditorWelcomeFrame(None)
frame.Show(True)
app.MainLoop()
