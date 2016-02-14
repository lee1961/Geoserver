import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import sys
import lxml.etree as kk
import pycurl


print("To change the style of the layer")
workspace_name = raw_input("Enter the workspace name: ")
layer_name = raw_input("Enter the layername you would like to edit: ")
style_name = raw_input("Enter the stylename you would like to replace: ")

c = pycurl.Curl();

c.setopt(c.HTTPHEADER, ["Content-type: text/xml"])
c.setopt(pycurl.USERPWD,"admin" + ":" + "geoserver")
c.setopt(pycurl.POSTFIELDS, "<layer><defaultStyle><name>" + style_name + "</name></defaultStyle></layer>")
c.setopt(pycurl.CUSTOMREQUEST,"PUT")
c.setopt(c.VERBOSE,1)
c.setopt(c.URL, "http://localhost:8080/geoserver/rest/layers/" + workspace_name + ":" + layer_name )

c.perform()



