import bin.htmlPython as py
import json
import sys

def test_generateHtml():

	ha = open("files/htmlTest.txt")
	ha = ha.read().strip()
	
	j = json.load(open("output/aaa/aaa.json"))

	htmlFile = open("aaa.html", "w")
	sha256 = j['analysis']['res']

	artefacts = j['analysis']['data']['art']
	metas = j['analysis']['met']

	py.generateHTML(metas, artefacts, sha256, htmlFile)
	htmlFile.close()

	htmlContent = open("aaa.html")
	
	assert htmlContent.read() == ha
