gimport xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import sys
import lxml.etree as kk
import pycurl

#print 'Number pf arguments:', len(sys.argv), 'arguments.'

#print 'Argument List:', str(sys.argv)

if(len(sys.argv) < 2 ):
	print("Enter ./argument.py <layer_name> <style> <layer_name_2> <style2>.....")
	sys.exit(2)

argument_list = []


for str in sys.argv[1:]:
	argument_list.append(str)
#print "the argument list is "
#print argument_list


if len(argument_list) % 2 != 0:
	print("you are missing a layer or list since its odd number")
	print("Launch again")
	sys.exit(2)

layer_list = []
style_list = []
#this is for adding the odd number the odd list
for str in argument_list[::2]:
	layer_list.append(str)

#this is for adding the even number the style list
for str in argument_list[1::2]:
	style_list.append(str)
#checking whether its odd


#print "the layer list is "
#print layer_list

#print "the style list is "
#print style_list

group_name = raw_input("Enter the group name you want: ") # getting the group name

''' generating the xml file
'''

root=Element('layerGroup')
tree=ElementTree(root)
name=Element('name')
root.append(name) # name of the group
name.text = group_name

layers=Element('layers')
for s,style in zip(layer_list, style_list):
        layer=Element('layer')
        layer.text = s
        layers.append(layer)
        layer.set('style',style)

root.append(layers)
styles=Element('styles')
for s in style_list:
        style=Element('style')
        style.text = s
        styles.append(style)
root.append(styles)


#print etree.tostring(root)
tree.write(open(group_name + ".xml",'w'))

x = kk.parse(group_name + ".xml")
print "the xml file generated is "
print kk.tostring(x, pretty_print = True)

'''
this is where the sending goes
'''
f = open(group_name + ".xml", "r")
contents = f.read()
f.close()
print 'xml generated....'
print contents
c = pycurl.Curl();

c.setopt(c.HTTPHEADER, ["Content-type: text/xml"])
c.setopt(pycurl.USERPWD,"admin" + ":" + "geoserver")
c.setopt(pycurl.POSTFIELDS, contents)
c.setopt(pycurl.CUSTOMREQUEST,"POST")
c.setopt(c.VERBOSE,1)
c.setopt(c.URL, "http://localhost:8080/geoserver/rest/layergroups" )

c.perform()


	


