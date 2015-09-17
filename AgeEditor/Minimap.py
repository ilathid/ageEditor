import wx.lib.ogl as ogl
import wx
import os
from SerializableAge import *

class RightClickMenu(wx.Menu):

    def onNew3DStandpoint(self, evt):
        self.newStandpointCallback(True, self.x, self.y)

    def onNew2DStandpoint(self, evt):
        self.newStandpointCallback(False, self.x, self.y)

    def __init__(self, icon_2d, icon_3d, x, y, newStandpointCallback):
        wx.Menu.__init__(self, "")
        self.newStandpointCallback = newStandpointCallback
        self.x = x
        self.y = y

        create3DMenuItem = wx.MenuItem(self, wx.ID_ANY, "Create 3D standpoint here")
        create3DMenuItem.SetBitmap(icon_3d)
        create3DMenu = self.AppendItem(create3DMenuItem)
        self.Bind(wx.EVT_MENU, self.onNew3DStandpoint, id=create3DMenu.GetId())

        create2DMenuItem = wx.MenuItem(self, wx.ID_ANY, "Create slide here")
        create2DMenuItem.SetBitmap(icon_2d)
        create2DMenu = self.AppendItem(create2DMenuItem)
        self.Bind(wx.EVT_MENU, self.onNew2DStandpoint, id=create2DMenu.GetId())

class MyEvtHandler(ogl.ShapeEvtHandler):
    def __init__(self, parent):
        ogl.ShapeEvtHandler.__init__(self)
        self.parent = parent

    def UpdateStatusBar(self, shape):
        pass
        #x, y = shape.GetX(), shape.GetY()
        #width, height = shape.GetBoundingBoxMax()
        #self.statbarFrame.SetStatusText("Pos: (%d, %d)  Size: (%d, %d)" %
        #                                (x, y, width, height))


    def selectStandpoint(self, canvas, shape, name):
        self.parent._setSelectedStandpoint(name)

        dc = wx.ClientDC(canvas)
        canvas.PrepareDC(dc)

        shapeList = canvas.GetDiagram().GetShapeList()
        toUnselect = []

        for s in shapeList:
            if s.Selected():
                # If we unselect it now then some of the objects in
                # shapeList will become invalid (the control points are
                # shapes too!) and bad things will happen...
                toUnselect.append(s)

        shape.Select(True, dc)

        if toUnselect:
            for s in toUnselect:
                s.Select(False, dc)

            ##canvas.Redraw(dc)
            canvas.Refresh(False)

    def OnLeftClick(self, x, y, keys=0, attachment=0):

        shape = self.GetShape()
        canvas = shape.GetCanvas()

        self.selectStandpoint(canvas, shape, shape.name)


    def OnEndDragLeft(self, x, y, keys=0, attachment=0):
        shape = self.GetShape()
        ogl.ShapeEvtHandler.OnEndDragLeft(self, x, y, keys, attachment)

        if not shape.Selected():
            self.OnLeftClick(x, y, keys, attachment)

        #self.UpdateStatusBar(shape)


    def OnSizingEndDragLeft(self, pt, x, y, keys, attch):
        ogl.ShapeEvtHandler.OnSizingEndDragLeft(self, pt, x, y, keys, attch)
        self.UpdateStatusBar(self.GetShape())


    def OnMovePost(self, dc, x, y, oldX, oldY, display):
        shape = self.GetShape()
        ogl.ShapeEvtHandler.OnMovePost(self, dc, x, y, oldX, oldY, display)
        #self.UpdateStatusBar(shape)
        if "wxMac" in wx.PlatformInfo:
            shape.GetCanvas().Refresh(False)
        self.parent.onMoveSlide(shape.name, int(x), int(y))

    def OnRightClick(self, x, y, keys, attachment):
        pass
        #self.log.WriteText("%s\n" % self.GetShape())

class MinimapStandpoint(ogl.BitmapShape):
    """Draws a bitmap (non-resizable)."""
    def __init__(self, name, is3D):
        ogl.BitmapShape.__init__(self)
        self._filename = ""
        self.name = name
        self.is3D = is3D


# =================================================================================================
# =================================================================================================

class Minimap(ogl.ShapeCanvas):

    ogl_initialised = False

    def __init__(self, mainFrame, parent, age, backgroundImg, standpointSelectedCallback, modificationCallback,
                 onCreateStandpointCallback):

        self.mainFrame = mainFrame
        self.backgroundImg = backgroundImg
        self.age = age
        self.standpoint2dIcon = wx.Bitmap("data/icon_standpoint2d.png")
        self.standpoint3dIcon = wx.Bitmap("data/icon_standpoint3d.png")
        self.homeIcon = wx.Bitmap("data/start.png")

        self.selectedStandpoint = None
        self.standpointSelectedCallback = standpointSelectedCallback
        self.modificationCallback = modificationCallback
        self.onCreateStandpointCallback = onCreateStandpointCallback

        if not Minimap.ogl_initialised:
            ogl.OGLInitialize()
            Minimap.ogl_initialised = True

        ogl.ShapeCanvas.__init__(self, parent)

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        if backgroundImg is None:
            maxWidth = 1000
            maxHeight = 1000
        else:
            maxWidth = max(backgroundImg.GetWidth(), 1000)
            maxHeight = max(backgroundImg.GetHeight(), 1000)
        self.SetScrollbars(1, 1, maxWidth, maxHeight)
        self.SetBackgroundColour(wx.WHITE)
        self.diagram = ogl.Diagram()
        self.SetDiagram(self.diagram)
        self.diagram.SetCanvas(self)
        self.shapes = []
        self.lines = []
        self.save_gdi = []

#        self.MyAddShape(
#            ogl.CircleShape(80),
#            75, 110, wx.Pen(wx.BLUE, 3), wx.GREEN_BRUSH, "Circle"
#            )
#
#        self.MyAddShape(
#            ogl.TextShape(120, 45),
#            160, 35, wx.GREEN_PEN, wx.LIGHT_GREY_BRUSH, "OGL is now a\npure Python lib!"
#            )
#
#        self.MyAddShape(
#            ogl.RectangleShape(85, 50),
#            305, 60, wx.BLACK_PEN, wx.LIGHT_GREY_BRUSH, "Rectangle"
#            )

        for currslide in age.getSlides():
            s = MinimapStandpoint(currslide.getId(), currslide.is3DSlide())
            if currslide.getId() == age.start:
                s.SetBitmap(self.homeIcon)
            elif currslide.is3DSlide():
                s.SetBitmap(self.standpoint3dIcon)
            else:
                s.SetBitmap(self.standpoint2dIcon)
            self.MyAddShape(s, currslide.getMinimapX(), currslide.getMinimapY(), None, None, "")

        self.updateLines()

#
#        s = MinimapStandpoint("sp1")
#        s.SetBitmap(self.standpoint2dIcon)
#        self.MyAddShape(s, 100, 100, None, None, "")
#
#        s = MinimapStandpoint("sp2")
#        s.SetBitmap(self.standpoint2dIcon)
#        self.MyAddShape(s, 225, 130, None, None, "")
#
#        s = MinimapStandpoint("sp3")
#        s.SetBitmap(self.standpoint3dIcon)
#        self.MyAddShape(s, 230, 256, None, None, "")
#
#        s = MinimapStandpoint("sp3")
#        s.SetBitmap(self.standpoint3dIcon)
#        self.MyAddShape(s, 95, 235, None, None, "")


        # EXAMPLE how to connect points with lines
#        for x in range(len(self.shapes)):
#            fromShape = self.shapes[x]
#            if x+1 == len(self.shapes):
#                toShape = self.shapes[0]
#            else:
#                toShape = self.shapes[x+1]
#
#            line = ogl.LineShape()
#            line.SetCanvas(self)
#            line.SetPen(wx.BLACK_PEN)
#            line.SetBrush(wx.BLACK_BRUSH)
#            line.AddArrow(ogl.ARROW_ARROW)
#            line.MakeLineControlPoints(2)
#            fromShape.AddLine(line, toShape)
#            self.diagram.AddShape(line)
#            line.Show(True)

        self.middleMouseButtonDown = False
        self.Bind(wx.EVT_MIDDLE_DOWN, self.onMiddleMouseButtonDown)
        self.Bind(wx.EVT_MIDDLE_UP, self.onMiddleMouseButtonUp)
        #self.Bind(wx.EVT_MOTION, self.onMouseMove)
        self.Bind(wx.EVT_MOUSE_CAPTURE_LOST, self.onMiddleMouseButtonUp)

    # ---------------------------------------------------------------------------------------------

    def setHomeStandpoint(self, standpointName):
        for s in self.shapes:
            if s.name == standpointName:
                s.SetBitmap(self.homeIcon)
            else:
                if s.is3D:
                    s.SetBitmap(self.standpoint3dIcon)
                else:
                    s.SetBitmap(self.standpoint2dIcon)
        self.Refresh()

    # ---------------------------------------------------------------------------------------------

    # Override the base class's paint to be able to place a background
    def OnPaint(self, evt):
        dc = wx.AutoBufferedPaintDC(self)
        self.PrepareDC(dc)

        dc.SetBackground(wx.Brush(self.GetBackgroundColour(), wx.SOLID))
        dc.Clear()

        if self.backgroundImg is not None:
            dc.DrawBitmap(self.backgroundImg, 0, 0)

        if self.GetDiagram():
            self.GetDiagram().Redraw(dc)

    # ---------------------------------------------------------------------------------------------

    def MyAddShape(self, shape, x, y, pen, brush, text):
        # Composites have to be moved for all children to get in place
        if isinstance(shape, ogl.CompositeShape):
            dc = wx.ClientDC(self)
            self.PrepareDC(dc)
            shape.Move(dc, x, y)
        else:
            shape.SetDraggable(True, True)
        shape.SetCanvas(self)
        shape.SetX(x)
        shape.SetY(y)
        if pen:    shape.SetPen(pen)
        if brush:  shape.SetBrush(brush)
        if text:
            for line in text.split('\n'):
                shape.AddText(line)
        #shape.SetShadowMode(ogl.SHADOW_RIGHT)
        self.diagram.AddShape(shape)
        shape.Show(True)

        evthandler = MyEvtHandler(self)
        evthandler.SetShape(shape)
        evthandler.SetPreviousHandler(shape.GetEventHandler())
        shape.SetEventHandler(evthandler)

        self.shapes.append(shape)
        return shape

    # ---------------------------------------------------------------------------------------------

    def OnBeginDragLeft(self, x, y, keys):
        pass
        #print "OnBeginDragLeft: %s, %s, %s\n" % (x, y, keys)

    # ---------------------------------------------------------------------------------------------

    def OnEndDragLeft(self, x, y, keys):
        print "= End dragging ="
        pass
        #print "OnEndDragLeft: %s, %s, %s\n" % (x, y, keys)

    # ---------------------------------------------------------------------------------------------

    def updateLines(self):

        self.Freeze()

        # Build a dictionary since we will search for slides by name in a loop - this avoids
        # the O(n^2) case
        slidesByName = {}
        for curr in self.age.getSlides():
            slidesByName[curr.getId()] = curr

        # Remove lines that are no more there
        updatedLinesList = []

        for curr in self.lines:
            keepLine = False

            if curr.GetFrom().name in slidesByName:
                slideFrom = slidesByName[curr.GetFrom().name]
                slideToName = curr.GetTo().name

                for h in slideFrom.getHotspots():
                    if h.getDestination() == slideToName:
                        keepLine = True
                        break

            if not keepLine:
                self.RemoveShape(curr)
            else:
                updatedLinesList.append(curr)

        self.lines = updatedLinesList

        # Again avoid the O(n^2) case by building a dictionary
        linesByOrigin = {}
        for curr in self.lines:
            if curr.GetFrom().name not in linesByOrigin:
                linesByOrigin[curr.GetFrom().name] = []
            linesByOrigin[curr.GetFrom().name].append(curr.GetTo().name)

        shapesByName = {}
        for curr in self.shapes:
            shapesByName[curr.name] = curr

        # Add new lines
        for currslide in self.age.getSlides():
            if currslide.getId() in linesByOrigin:
                lines_starting_here = linesByOrigin[currslide.getId()]
            else:
                lines_starting_here = []

            for hotspot in currslide.getHotspots():
                destination = hotspot.getDestination()
                if (destination not in lines_starting_here) and (destination in shapesByName):
                    fromShape = shapesByName[currslide.getId()]
                    toShape = shapesByName[destination]
                    line = ogl.LineShape()
                    line.SetCanvas(self)
                    line.SetPen(wx.BLACK_PEN)
                    line.SetBrush(wx.BLACK_BRUSH)
                    line.AddArrow(ogl.ARROW_ARROW)
                    line.MakeLineControlPoints(2)
                    fromShape.AddLine(line, toShape)
                    self.diagram.AddShape(line)
                    line.Show(True)
                    self.lines.append(line)

        self.Thaw()
        self.Refresh()

    # ---------------------------------------------------------------------------------------------

    # User requested the creation of a new standpoint/slide
    def onCreateStandpoint(self, is3D, x, y):
        print "Creating standpoint required at ", x, y, ", 3d =", is3D

        i = 1
        while self.age.slideWithNameExists(self.age.name + str(i)):
            i += 1

        name = wx.GetTextFromUser("Select the name of the new " + ("standpoint" if is3D else "slide"),
                                  "Please choose a name", self.age.name + str(i))
        if name == "":
            return

        if is3D:
            files = [XMLFile(FilePath(name + "_n.jpg", None, None)),
                     XMLFile(FilePath(name + "_e.jpg", None, None)),
                     XMLFile(FilePath(name + "_s.jpg", None, None)),
                     XMLFile(FilePath(name + "_w.jpg", None, None)),
                     XMLFile(FilePath(name + "_t.jpg", None, None)),
                     XMLFile(FilePath(name + "_b.jpg", None, None))]
        else:
            files = [XMLFile(FilePath(name + ".jpg", None, None))]

        if not self.age.addSlide(XMLSlide(name, is3D, [x, y], files, onentrance=None, onexit=None, hotspots=[])):
            return

        if is3D:
            s = MinimapStandpoint(name, is3D)
            s.SetBitmap(self.standpoint3dIcon)
            self.MyAddShape(s, x, y, None, None, "")
        else:
            s = MinimapStandpoint(name, is3D)
            s.SetBitmap(self.standpoint2dIcon)
            self.MyAddShape(s, x, y, None, None, "")

        self.Refresh()
        self.onCreateStandpointCallback(name)

        #print "self.mainFrame.latestSlideDir", self.mainFrame.latestSlideDir
        #if self.mainFrame.latestSlideDir is not None:
        #    print "Looking for ", os.path.join(self.mainFrame.latestSlideDir, name + '.png')
        if is3D and self.mainFrame.latestSlideDir is not None and os.path.isfile(os.path.join(self.mainFrame.latestSlideDir, name + '.png')):
            #print "Might wanna look at ", os.path.join(self.mainFrame.latestSlideDir, name + '.png')
            print "Auto-loading", os.path.join(self.mainFrame.latestSlideDir, name + '.png')
            self.mainFrame.doImportCubeMap(os.path.join(self.mainFrame.latestSlideDir, name + '.png'), name)

    # ---------------------------------------------------------------------------------------------

    # Get the ID of the standpoint that is currently selected
    def getSelectedStandpoint(self):
        return self.selectedStandpoint

    # ---------------------------------------------------------------------------------------------

    # Set the ID of the standpoint that is currently selected
    # (internal use by MyEvtHandler ONLY, does NOT work to select a new standpoint)
    def _setSelectedStandpoint(self, name):
        print "You selected standpoint " + name
        self.selectedStandpoint = name
        self.standpointSelectedCallback(name)

    # ---------------------------------------------------------------------------------------------

    def renameSelectedStandpoint(self, newname):
        for curr in self.shapes:
            if curr.name == self.selectedStandpoint:
                curr.name = newname
                break
        self.selectedStandpoint = newname

    # ---------------------------------------------------------------------------------------------

    # Select a new standpoint
    def selectStandpointNamed(self, name):
        for shape in self.shapes:
            if shape.name == name:
                shape.GetEventHandler().selectStandpoint(self, shape, shape.name)
                return
        raise Exception("Cannot find standpoint named '" + name + "'")

    # ---------------------------------------------------------------------------------------------

    def deleteStandpoint(self, spName):
        for curr in self.shapes:
            if curr.name == self.selectedStandpoint:
                canvas = curr.GetCanvas()
                dc = wx.ClientDC(canvas)
                canvas.PrepareDC(dc)
                curr.Select(False, dc)
                self.shapes.remove(curr)
                self.RemoveShape(curr)
                break

        if self.selectedStandpoint == spName:
            self.selectedStandpoint = None

        self.Refresh()

    # ---------------------------------------------------------------------------------------------

    def onMoveSlide(self, slide, x, y):
        print "Move", slide, "to", x, y
        self.age.getSlideNamed(slide).setMinimapCoords(x, y)
        self.modificationCallback()

    # ---------------------------------------------------------------------------------------------

    # Override base class method to add some right-click code
    def OnMouseEvent(self, evt):
        if evt.RightUp():
            (scale_x, scale_y) = self.GetScrollPixelsPerUnit()
            (scroll_x, scroll_y) = self.GetViewStart()
            m = RightClickMenu(self.standpoint2dIcon, self.standpoint3dIcon,
                               evt.GetX() + scroll_x * scale_x, evt.GetY() + scroll_y * scale_y,
                               lambda is3D, x, y : self.onCreateStandpoint(is3D, x, y))
            self.PopupMenu(m, wx.Point(evt.GetX(), evt.GetY()))
        elif evt.LeftUp():
            self.Refresh()
        elif self.middleMouseButtonDown:
            d_x = self.drag_previous_x - evt.GetX()
            d_y = self.drag_previous_y - evt.GetY()

            scroll = self.GetViewStart()
            self.Scroll(max(0, scroll.x + d_x), max(0, scroll.y + d_y))

            self.drag_previous_x = evt.GetX()
            self.drag_previous_y = evt.GetY()

        ogl.ShapeCanvas.OnMouseEvent(self, evt)

    # ---------------------------------------------------------------------------------------------

    def onMiddleMouseButtonDown(self, evt):
        self.middleMouseButtonDown = True
        self.CaptureMouse()
        self.drag_previous_x = evt.GetX()
        self.drag_previous_y = evt.GetY()

    # ---------------------------------------------------------------------------------------------

    def onMiddleMouseButtonUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()
        self.middleMouseButtonDown = False
