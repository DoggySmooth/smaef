#!/usr/bin/env python3

import sys
import os
import json

import bin.xmlMerger as merger
import bin.xmlFormatter as formatter
import bin.generateXML as generateXML
import bin.generateJSON as generateJSON
import bin.generateHTML as generateHTML
import bin.generateGraph as generateGraph

from lxml import etree


def m():
	xmlOne = sys.argv[2]
	xmlTwo = sys.argv[3]

	xml_doc_one = etree.parse(xmlOne)
	xml_doc_two = etree.parse(xmlTwo)

	rootOne = xml_doc_one.getroot()
	rootTwo = xml_doc_two.getroot()


	firstSha  = rootOne.find('res').text
	secondSha = rootTwo.find('res').text

	firstArtefacts  = rootOne.find('data')
	secondArtefacts = rootTwo.find('data')

	merger.checkSha(firstSha, secondSha)
	merger.mergeFiles(rootOne, rootTwo, secondArtefacts)
		
	parser = etree.XMLParser(remove_blank_text=True)
	formatter.formatXML("merged.xml",parser)
	
def xml(plim,xml):

        generateXML.checkArgs(plim, xml)

        #Generated an unformatted XML file from an PLIM file
        os.system("lib/plimc "+plim+" -o "+xml)
        result = generateXML.validateXML(xml)

        if result:
                print("XML file is valid!")
                generateXML.writeXML(xml)
                print('XML Generated Sucessfully!')
        else:
                print("XML Schema is invalid!")
                raise ValueError("Schema is invalid!")

def jsong(xml, jsonName):
	
	generateJSON.generateJSON(xml, jsonName)
	generateJSON.validateJSON(jsonName)
	print("JSON Generated Sucessfully!")

def html(jsonName, html):

	generateHTML.generateHTML(jsonName, html)
	print("HTML Generated Sucessfully!")

def graph(x):
	
	j = json.load(open(x))
	artefacts = j['analysis']['data']['art']
	assert len(sys.argv) % 2 == 0, "All operations must be paired with a file."
	if isinstance(artefacts, dict):
		artefacts = [artefacts]
	g = generateGraph.generateGraph(artefacts)
	g.render()
	print("Graph generated successfully")
	
def clean(name):

	os.remove("Graph.gv")
	if not os.path.exists('output/'+name):
		os.makedirs('output/'+name)
		
	for filename in os.listdir("."):
		if filename.startswith("tmp"):
			os.rename(filename, 'output/'+name+'/'+name+filename[3:])
		if filename.startswith("Graph"):
			os.rename(filename, 'output/'+name+'/'+filename)
	
	os.remove('./files/'+name+'.json')
	os.remove('./files/'+name+'.xml')
	os.remove('./files/'+name+'.html')
		
def main():

	if sys.argv[1] == '-m':

		m()

	else:

		targetPLIM = sys.argv[1]
		
		name = os.path.basename(targetPLIM)
		name = os.path.splitext(name)[0]
		base = os.path.splitext(targetPLIM)[0]
		
		targetXML  = base+'.xml'
		targetJSON = base+'.json'
		targetHTML = base+'.html'
		
		xml(targetPLIM, targetXML)
		jsong(targetXML, targetJSON)
		html(targetJSON, targetHTML)
		graph(targetJSON)
		clean(name)

if __name__ == '__main__':
	main()
