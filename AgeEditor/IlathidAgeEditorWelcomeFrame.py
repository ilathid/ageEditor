"""Subclass of WelcomeFrame, which is generated by wxFormBuilder."""

import WelcomeFrame
import os.path
from SerializableAge import *
from IlathidAgeEditorMainFrame import IlathidAgeEditorMainFrame
import xml

# Implementing WelcomeFrame
class IlathidAgeEditorWelcomeFrame( WelcomeFrame.WelcomeFrame ):
    def __init__( self, parent ):
        WelcomeFrame.WelcomeFrame.__init__( self, parent )
        
        defaultVal = wx.ConfigBase.Get().Read("agePath", "")
        if len(defaultVal) > 0:
            self.m_ageDirPicker.GetTextCtrl().SetValue(defaultVal)
    
    # Handlers for WelcomeFrame events.
    def onAgeFolderSelected( self, event ):
        
        ageDir = self.m_ageDirPicker.GetTextCtrl().GetValue()
        if not os.path.exists(ageDir):
            os.makedirs(ageDir)
        
        # remember the selection for next time
        wx.ConfigBase.Get().Write("agePath", ageDir)
        
        # Check if there is an age in the specified directory. If yes, load it. If not, create a new one
        loadedAge = None
        agexml = os.path.join(ageDir, "age.xml")
        if os.path.isfile(agexml):
            loadedAge = XMLAge.deserialize(xml.dom.minidom.parse(agexml).childNodes[0])
        
        age = None
        
        if loadedAge:
            age = loadedAge
        else:
            import re
            agename = os.path.split(ageDir)[-1]
            
            if re.match(r'\A[a-zA-Z0-9_]+\Z', agename) is None:
                wx.MessageBox("An age name may only contain letters, cannot be '" + agename + "'")
                return

            answer = wx.MessageBox("Will create a new age called '" + agename + "'. That's OK?", "Confirm", wx.OK | wx.CANCEL | wx.CENTRE)
            if answer != wx.OK:
                return
        
            # create a new empty age
            age = XMLAge(agename, agename+"1", [XMLSlide(agename+"1", True, [100, 100],
                                                         [XMLFile(FilePath(agename+"1_n.jpg", None, None)),
                                                          XMLFile(FilePath(agename+"1_e.jpg", None, None)),
                                                          XMLFile(FilePath(agename+"1_s.jpg", None, None)),
                                                          XMLFile(FilePath(agename+"1_w.jpg", None, None)),
                                                          XMLFile(FilePath(agename+"1_t.jpg", None, None)),
                                                          XMLFile(FilePath(agename+"1_b.jpg", None, None))],
                         onentrance=None, onexit=None, hotspots=[])])
        
        frame = IlathidAgeEditorMainFrame(None, ageDir, age)
        frame.Maximize()
        frame.Show()
        self.Close()
        self.Destroy()
    
    
