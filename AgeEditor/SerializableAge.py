from XmlIO import CommaSeparatedList
from XmlIO import StringAttribute
from XmlIO import TextContents
from XmlIO import DirectChildrenList
from FilePath import FilePath
import wx

# TODO: Add support for images
#        <image id="dni59image">
#            <file archive="images.zip">59_00000.png</file>
#            <rect>391,125</rect>
#            <alpharef>0,0</alpharef>
#        </image>


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def getAttrOrNone(xmlNode, attrName):
    if xmlNode.hasAttribute(attrName): return xmlNode.getAttribute(attrName)
    return None

def getChildContentsOrNone(xmlNode, childName):
    children = xmlNode.getElementsByTagName(childName)
    if len(children) == 0: return None
    else: return getText(children[0].childNodes)

# =============================================================================
class XMLHotspot(object):
    
    XML_NAME = "hotspot"
    
    # cursor : a string
    # rect : a list of 4 integers, format [x, y, width, height]
    # dest : a string
    # action : optional script to execute when clicking on this hotspot
    def __init__(self, cursor, rect, dest, action = None, polygon = []):
        self.cursor = StringAttribute(cursor)
        self.rect = CommaSeparatedList(rect)
        self.polygon = CommaSeparatedList(polygon)
        self.dest = dest
        self.action = action
        self.destOrientation = 0
    
    def getCursor(self):
        return self.cursor

    def setCursor(self, cursorname):
        self.cursor = StringAttribute(cursorname)

    def getRect(self):
        return self.rect
    
    def isPolygonHotspot(self):
        return len(self.rect) == 0 and len(self.polygon) > 0
    
    def getPolygon(self):
        return self.polygon
    
    def getPolygonCenter(self):
        i = 0
        sum_x = 0
        sum_y = 0
        count = 0
        while i < len(self.polygon) - 3:
            sum_x += self.polygon[i]
            sum_y += self.polygon[i + 1]
            count += 1
            i += 2
        average_x = float(sum_x) / float(count)
        average_y = float(sum_y) / float(count)
        return [int(average_x), int(average_y)]
    
    # format [x, y, w, h]
    def setRect(self, rect):
        if not isinstance(rect, list): raise Exception("Rect must be a list")
        if len(rect) != 4: raise Exception("Expected 4 elements in the rectangle")
        
        self.rect = CommaSeparatedList(rect)
    
    def getDestination(self):
        return self.dest
    
    def setDestination(self, destinationStandpoint):
        self.dest = destinationStandpoint
    
    def getAction(self):
        return self.action
    
    def setAction(self, action):
        self.action = action
    
    # The angle at which the player should start in the dest slide (if 3d slide). 0 to 360 degrees
    def getDestOrientation(self):
        return self.destOrientation
    
    # The angle at which the player should start in the dest slide (if 3d slide). 0 to 360 degrees
    def setDestOrientation(self, angle):
        self.destOrientation = angle
    
    @classmethod
    def deserialize(cls, xmlNode):
        rect = []
        rectnode = xmlNode.getElementsByTagName("rect")
        if rectnode is not None and len(rectnode) > 0:
            rectNodeText = getText(rectnode[0].childNodes)
            if len(rectNodeText) > 0:
                rect = map(lambda x: int(x), rectNodeText.split(","))
        
        polygonPoints = []
        polygonNode = xmlNode.getElementsByTagName("polygon")
        if polygonNode is not None and len(polygonNode) > 0:
            polyText = getText(polygonNode[0].childNodes)
            if len(polyText) > 0:
                polygonPoints = map(lambda x: int(x), polyText.split(","))
        
        hspt = XMLHotspot(xmlNode.getAttribute("cursor"),
                          rect,
                          getChildContentsOrNone(xmlNode, "dest"),
                          getChildContentsOrNone(xmlNode, "action"),
                          polygon = polygonPoints)
        hspt.destOrientation = int(xmlNode.getAttribute("destOrientation"))
        return hspt
        

# =============================================================================
class XMLFile(object):
    
    XML_NAME = "file"
    
    def __init__(self, fileRef):
        self.path = TextContents(fileRef.getFileName())
        
        if fileRef.getArchiveName() is not None:
            self.archive = StringAttribute(fileRef.getArchiveName())
        else:
            self.archive = None
        
        # TODO: fileRef.getEncryption
    
    def getPath(self):
        return self.path
    
    def getArchive(self):
        return self.archive
    
    def setPath(self, filepath, archive):
        self.path = TextContents(filepath)
        
        if archive is not None:
            self.archive = StringAttribute(archive)
        else:
            self.archive = None
    
    @classmethod
    def deserialize(cls, xmlNode):
        return XMLFile(FilePath(getText(xmlNode.childNodes),
                                getAttrOrNone(xmlNode, "archive"),
                                None))

# =============================================================================
class XMLMovie(object):
    
    XML_NAME = "movie"
    
    # rect : a list of 4 integers, format [x, y, width, height]
    # endFunc : a string, the name of the function to call when the movie is over
    def __init__(self, movieId, fileName, rect, endFunc):
        self.id = StringAttribute(movieId)
        self.rect = CommaSeparatedList(rect)
        self.endfunc = endFunc
        self.file = fileName
        
    def getId(self):
        return self.id
    
    def setId(self, movieId):
        self.id = StringAttribute(movieId)

    def getRect(self):
        return self.rect

    def setRect(self, rect):
        self.rect = CommaSeparatedList(rect)
        
    def getFile(self):
        return self.file
    
    def setFile(self, fileName):
        self.file = fileName

    def getEndFunc(self):
        return self.endfunc
    
    def setEndFunc(self, endFunc):
        self.endfunc = endFunc
    
    @classmethod
    def deserialize(cls, xmlNode):
        return XMLMovie(xmlNode.getAttribute("id"),
                        getChildContentsOrNone(xmlNode, "file"),
                        [int(x) for x in getChildContentsOrNone(xmlNode, "rect").split(",")],
                        getChildContentsOrNone(xmlNode, "endfunc"))

# =============================================================================
class XMLMusic(object):
    
    XML_NAME = "music"
    
    def __init__(self, musicId, fileName, volume):
        self.id = StringAttribute(musicId)
        self.volume = str(volume)
        self.file = fileName
        self.type = StringAttribute("std")
        
    def getId(self):
        return self.id
    
    def setId(self, movieId):
        self.id = StringAttribute(movieId)

    def getFile(self):
        return self.file
    
    def setFile(self, fileName):
        self.file = fileName
    
    def getVolume(self):
        return float(self.volume)
        
    @classmethod
    def deserialize(cls, xmlNode):
        return XMLMusic(xmlNode.getAttribute("id"),
                        getChildContentsOrNone(xmlNode, "file"),
                        getChildContentsOrNone(xmlNode, "volume"))
        
# =============================================================================
class XMLSlide(object):
    
    XML_NAME = "slide"

    # fileRef : a list of type FilePath
    def __init__(self, slideId, is3D, minimapCoords, fileRef, onentrance, onexit, hotspots):
        
        if not isinstance(fileRef[0], XMLFile):
            raise Exception("fileRef should be a list of XMLFile")
        
        self.id = StringAttribute(slideId)
        self.minimapCoords = CommaSeparatedList(minimapCoords)
        self.file = DirectChildrenList(fileRef)
        self.onentrance = onentrance
        self.onexit = onexit
        self.hotspots = DirectChildrenList(hotspots)
        self.is3D = StringAttribute("true" if is3D else "false");

    def setMinimapCoords(self, x, y):
        self.minimapCoords[0] = x
        self.minimapCoords[1] = y

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = StringAttribute(newid)

    def getOnEntranceScript(self):
        return self.onentrance

    def setOnEntranceScript(self, script):
        self.onentrance = script

    def getOnExitScript(self):
        return self.onexit

    def setOnExitScript(self, script):
        self.onexit = script
    
    def getMinimapX(self):
        return self.minimapCoords[0]

    def getMinimapY(self):
        return self.minimapCoords[1]
    
    def is3DSlide(self):
        return self.is3D == "true"

    def getFiles(self):
        return self.file

    def getHotspots(self):
        return self.hotspots

    def addHotspot(self, hotspot):
        self.hotspots.append( hotspot )
        return len(self.hotspots) - 1

    def removeHotspot(self, hotspot):
        self.hotspots.remove(hotspot)
    
    @classmethod
    def deserialize(cls, xmlNode):
        onentrance = getChildContentsOrNone(xmlNode, "onentrance")
        onexit = getChildContentsOrNone(xmlNode, "onexit")
        
        files = []
        for curr in xmlNode.getElementsByTagName("file"):
            files.append(XMLFile.deserialize(curr))
        
        hotspots = []
        for curr in xmlNode.getElementsByTagName("hotspot"):
            hotspots.append(XMLHotspot.deserialize(curr))
            
        is3D = (xmlNode.hasAttribute("is3D") and xmlNode.getAttribute("is3D") == "true")
        
        minimapCoords = map(lambda x: int(x), getText(xmlNode.getElementsByTagName("minimapCoords")[0].childNodes).split(","))
        
        return XMLSlide(xmlNode.getAttribute("id"), is3D, minimapCoords, files, onentrance, onexit, hotspots)

# =============================================================================
class XMLAge(object):
    
    XML_NAME = "age"
    
    def __init__(self, name, start, slides, movies = [], musics=[]):
        
        self.name = StringAttribute(name)
        self.start = StringAttribute(start)
        self.slides = DirectChildrenList(slides)
        self.movies = DirectChildrenList(movies)
        self.musics = DirectChildrenList(musics)
        
    def addSlide(self, slide):
        
        for curr in self.slides:
            if curr.id == slide.id:
                wx.MessageBox("There is already a slide with this name")
                return False
        
        self.slides.append(slide)
        return True
    
    def clearMovies(self):
        self.movies = DirectChildrenList([])
    
    def clearMusics(self):
        self.musics = DirectChildrenList([])
        
    def addMovie(self, mov):
        
        if not isinstance(mov, XMLMovie):
            raise "Movie must be an instance of XMLMovie"
        
        self.movies.append(mov)
    
    def addMusic(self, music):
        
        if not isinstance(music, XMLMusic):
            raise "Music must be an instance of XMLMusic"
        
        self.musics.append(music)
        
    def getMusics(self):
        return self.musics
    
    def getMovies(self):
        return self.movies
        
    def getSlides(self):
        return self.slides
    
    def slideWithNameExists(self, name):
        for curr in self.slides:
            if curr.getId() == name:
                return True
        return False
            
    def getSlideNamed(self, name):
        for curr in self.slides:
            if curr.getId() == name:
                return curr
        raise Exception("There is no slide named '" + name + "' in this age")
    
    def removeSlideNamed(self, name):
        for curr in self.slides:
            if curr.getId() == name:
                self.slides.remove(curr)
                return
        raise Exception("There is no slide named '" + name + "' in this age")
    
    @classmethod
    def deserialize(cls, xmlNode):
        slides = []
        for curr in xmlNode.getElementsByTagName("slide"):
            slides.append(XMLSlide.deserialize(curr))
        
        movies = []
        for curr in xmlNode.getElementsByTagName("movie"):
            movies.append(XMLMovie.deserialize(curr))
        
        musics = []
        for curr in xmlNode.getElementsByTagName("music"):
            musics.append(XMLMusic.deserialize(curr))
            
        return XMLAge(xmlNode.getAttribute("name"),
                      xmlNode.getAttribute("start"),
                      slides, movies, musics)



# =============================================================================
# =============================================================================
# test
# =============================================================================

#slides = [XMLSlide("pres", False, [XMLFile(FilePath("pres.jpg", None, None))], onentrance="playpresmusic", onexit=None, hotspots=[]),
#          XMLSlide("dni1", True, [XMLFile(FilePath("dnichamber1.jpg", "slides.zip", None)),
#                                  XMLFile(FilePath("dnichamber2.jpg", "slides.zip", None)),
#                                  XMLFile(FilePath("dnichamber3.jpg", "slides.zip", None)),
#                                  XMLFile(FilePath("dnichamber4.jpg", "slides.zip", None)),
#                                  XMLFile(FilePath("dnichamber4.jpg", "slides.zip", None)),
#                                  XMLFile(FilePath("dnichamber5.jpg", "slides.zip", None))], onentrance="playfirstmusic", onexit=None,
#                   hotspots=[XMLHotspot("left", [0, 0, 100, 500], "dni3"),
#                             XMLHotspot("right", [700,0,100,500], "dni2")])]
#
#testage = XMLAge("Dni", "dni1", slides)
#asXml = xmlSerialize(testage)
#
#
#print asXml
#
#print "==========================================="
#
#age2 = XMLAge.deserialize(xml.dom.minidom.parseString(asXml).childNodes[0])
#
#print "==========================================="
#
#print xmlSerialize(age2)

