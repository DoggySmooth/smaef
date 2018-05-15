#!/usr/bin/env python3

import sys, os, re
from lxml import etree
#Check if the arguments are passed correctly
def checkArgs(plim, xml):
	regex = r".*\."
	resultPlim = re.sub(regex, "", plim)
	resultXml = re.sub(regex, "", xml)

	if resultPlim == resultXml:
		raise ValueError('\n\nWrong arguments has been passed to the script!\nThis happens if there are multiple plim files in smaef directory\n')

	if resultXml != 'xml':
		raise ValueError('Second argument has to be an .xml extension')



#Validates XML schema based on an SCHEMA 
def validateXML(xml):
	
	xmlschema_doc = etree.parse("res/schema/s2extend")
	xmlschema = etree.XMLSchema(xmlschema_doc)

	xml_doc = etree.parse(xml)
	result = xmlschema.validate(xml_doc)

	return result

#Writes a formatted XML file to the temporary file
def writeXML(xml):
	
	xml_doc = etree.parse(xml)
	file = open("tmp.xml","w")
	xml_doc.write("tmp.xml", encoding="utf-8", pretty_print=True)
	file.close()



def main(args=None):

	#Initialize variables for better overview
	plim = sys.argv[1]
	xml  = sys.argv[2]
	
	checkArgs(plim, xml)
	
	#Generated an unformatted XML file from an PLIM file
	os.system("lib/plimc "+plim+" -o "+xml)
	result = validateXML(xml)
	
	if result:
		print("XML file is valid!")
		writeXML(xml)
		print('XML Generated Sucessfully!')
	else:
		print("XML Schema is invalid!")
		raise ValueError("Schema is invalid!")




if __name__ == '__main__':
	main()
