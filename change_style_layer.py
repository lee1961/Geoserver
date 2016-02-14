import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import sys 
import lxml.etree as kk
import pycurl


workspace_name = raw_input("Enter the workspace name: ")
layer_name = raw_input("Enter your the layername: ")

style_name = raw_input("Enter the style name you want: ")

c = pycurl.Curl()
c.setopt(pycurl.POSTFIELDS, "<layer><defaultStyle><name>"+ style_name + "</name></defaultStyle></layer>");
c.setopt(c.HTTPHEADER, ["Content-type: text/xml"])
c.setopt(pycurl.USERPWD,"admin" + ":" + "geoserver")
c.setopt(pycurl.CUSTOMREQUEST,"PUT")
c.setopt(c.VERBOSE,1)
c.setopt(c.URL, "http://localhost:8080/geoserver/rest/layers/" + workspace_name +":" + layer_name )
c.perform()
