import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import sys
import lxml.etree as kk
import pycurl

#getting number of arguments

if(len(sys.argv) < 2):
	print("Enter ./argument.py <filename> <storename>")
	sys.exit(2)



argument_list = sys.argv[1:]

file_name = []
store_name = []

for i in argument_list[::2]:
	file_name.append(i)
for i in argument_list[1::2]:
	store_name.append(i)

workspace_name= raw_input("Enter the workspace name you want it to be into:");


#uploading the zip files
for zip_file_name,store_file_name in zip(file_name,store_name):
	data = open(zip_file_name,'rb')
	c = pycurl.Curl()
	c.setopt(pycurl.HTTPHEADER, (["Content-type: application/zip"]))
	c.setopt(pycurl.USERPWD,"admin" + ":" + "geoserver")	
	c.setopt(c.URL,"http://localhost:8080/geoserver/rest/workspaces/"+ workspace_name + "/datastores/" + store_file_name + "/file.shp" )
	c.setopt(pycurl.PUT,1)
	c.setopt(c.VERBOSE,1)
	c.setopt(pycurl.INFILE,data)
	c.perform()
	data.close()
	
	


