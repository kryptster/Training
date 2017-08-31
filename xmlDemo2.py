import os
from xml.etree import ElementTree

xml_file='emplist.xml'
dom = ElementTree.parse(xml_file)

emps = dom.findall('emp')
for emp in emps:
	print(emp)
