#!/usr/bin/env python3

import sys, os, re, json
from lxml import etree

xmlOne = sys.argv[1]
xmlTwo = sys.argv[2]

xml_doc_one = etree.parse(xmlOne)
xml_doc_two = etree.parse(xmlTwo)

rootOne = xml_doc_one.getroot() 
rootTwo = xml_doc_two.getroot()

firstSha  = rootOne.find('sha256').text
secondSha = rootTwo.find('sha256').text

firstArtefacts  = rootOne.find('artefacts')
secondArtefacts = rootTwo.find('artefacts')


if firstSha != secondSha:
	raise ValueError('\n\nCan\'t merge files!\nSha are different!')

for artefact in rootOne[1]:
	flag = True
	for arte in rootTwo[1]:
		if artefact.find('name').text == arte.find('name').text and artefact.find('where').text == arte.find('where').text and artefact.find('what').text == arte.find('what').text:
			flag = False
			break
	if flag:
		child = etree.SubElement(secondArtefacts, "artefact")
		
		etree.SubElement(child, "where")
		child.find('where').text = artefact.find('where').text
		etree.SubElement(child, "what")
		child.find('what').text = artefact.find('what').text
		etree.SubElement(child, "name")
		child.find('name').text = artefact.find('name').text
		etree.SubElement(child, "level")
		child.find('level').text = artefact.find('level').text
		etree.SubElement(child, "description")
		child.find('description').text = artefact.find('description').text

my_tree = etree.ElementTree(rootTwo)

with open('./merged.xml', 'wb') as f:
    f.write(etree.tostring(my_tree, pretty_print=True))
f.close()
