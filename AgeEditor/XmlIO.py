# This file contains a set of utility functions and classes to
# serialize (nearly) regular Python objects into XML

from xml.dom.minidom import Document

class StringAttribute(str):
    def __new__(cls,*args,**kw):
        return str.__new__(cls,*args,**kw)

class TextContents(str):
    def __new__(cls,*args,**kw):
        return str.__new__(cls,*args,**kw)

class CommaSeparatedList(list):
    def __getitem__(self, key):
        return super(CommaSeparatedList, self).__getitem__(key)

class DirectChildrenList(list):
    def __getitem__(self, key):
        return super(DirectChildrenList, self).__getitem__(key)

# Utility class to _serialize a class hierarchy to XML
def _serialize(obj, parent, doc):
    typename = obj.__class__.XML_NAME #obj.__class__.__name__
    xmlNode = doc.createElement(typename)
    
    #print "Serializing " +  obj.__class__.XML_NAME
    #print "    " + str(dir(obj))
    
    for curr in dir(obj):
        if curr.startswith("_") or curr == "XML_NAME": continue
        
        curr_val = obj.__getattribute__(curr)

        
        #print curr + " has type " + type(curr_val).__name__
        
        if curr_val is None: continue
        
        if type(curr_val).__name__ in ('function', 'builtin_function_or_method', 'instancemethod'):
            continue
        elif isinstance(curr_val, TextContents):
            tagContents = doc.createTextNode(str(curr_val))
            xmlNode.appendChild(tagContents)
        elif isinstance(curr_val, int) or isinstance(curr_val, float) or isinstance(curr_val, StringAttribute):
            xmlNode.setAttribute(curr, str(curr_val))
        elif isinstance(curr_val, list) and not isinstance(curr_val, CommaSeparatedList):
            if isinstance(curr_val, DirectChildrenList):
                for o in curr_val:
                    _serialize(o, xmlNode, doc)
            else:
                child = doc.createElement(curr)
                xmlNode.appendChild(child)
                
                for o in curr_val:
                    _serialize(o, child, doc)
        else:
            
            if isinstance(curr_val, CommaSeparatedList):
                curr_val = ",".join(map(lambda a: str(a), curr_val))

            
            if isinstance(curr_val, str) or isinstance(curr_val, unicode):
                child = doc.createElement(curr)
                xmlNode.appendChild(child)
                tagContents = doc.createTextNode(str(curr_val))
                child.appendChild(tagContents)
            else:
                _serialize(curr_val, xmlNode, doc)
    
    parent.appendChild(xmlNode)
    return xmlNode

def xmlSerialize(obj):
    doc = Document()
    _serialize(obj, doc, doc)
    
    asXml = doc.toprettyxml(indent="  ")
    
    # By default, toprettyxml adds too many linebreaks. Work around that
    # Thanks to http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python for the tip
    import re
    text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
    asXml = text_re.sub('>\g<1></', asXml)
    
    return asXml

