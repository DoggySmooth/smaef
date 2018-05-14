#!/usr/bin/env python3

import sys, os, re
from lxml import etree

#Initialize variables for better overview
plim = sys.argv[1]
xml  = sys.argv[2]

#Check if the arguments are passed correctly
regex = r".*\."
resultPlim = re.sub(regex, "", plim)
resultXml = re.sub(regex, "", xml)

if resultPlim == resultXml:
	raise ValueError('\n\nWrong arguments has been passed to the script!\nThis happens if there are multiple plim files in smaef directory\n')

if resultXml != 'xml':
	raise ValueError('Second argument has to be an .xml extension')

#Generated an unformatted XML file from an PLIM file
os.system("lib/plimc "+plim+" -o "+xml)

#Created an temporary xml file
file = open("tmp.xml","w")

#Validates XML schema based on an SCHEMA 
xmlschema_doc = etree.parse("res/schema/s2extend")
xmlschema = etree.XMLSchema(xmlschema_doc)

xml_doc = etree.parse(xml)
result = xmlschema.validate(xml_doc)

#Writes a formatted XML file to the temporary file
xml_doc.write("tmp.xml", encoding="utf-8", pretty_print=True)
file.close()

if result:
	print("XML file is valid!")
else:
	print("XML Schema is invalid!")
	raise ValueError("Schema is invalid!")

print('XML Generated Sucessfully!')
