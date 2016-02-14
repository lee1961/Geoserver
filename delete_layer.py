import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import sys
import lxml.etree as kk
import pycurl

# to delete a file 
#use python delete_layer <layer_name> <layer_name>
#you wont be able to delete a layer if its already referened by another group

if (len(sys.argv) < 2):
	print("Enter delete_layer.py <layer_name> <layer_name2> ....")
	sys.exit(2)

for arg in sys.argv[1:]:
	c = pycurl.Curl();
	c.setopt(c.URL,"http://localhost:8080/geoserver/rest/layers/" + arg)
	c.setopt(c.HTTPHEADER, ["Content-type: text/xml"])
	c.setopt(pycurl.USERPWD,"admin" + ":" + "geoserver")
	c.setopt(pycurl.CUSTOMREQUEST,"DELETE")
	c.setopt(c.VERBOSE,1)
	c.perform()
