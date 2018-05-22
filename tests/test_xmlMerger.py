from lxml import etree
import bin.xmlMerger as merger

def test_sha():

	xml_doc_one = etree.parse(open("output/aa/aa.xml"))
	xml_doc_two = etree.parse(open("output/aaa/aaa.xml"))
	
	rootOne = xml_doc_one.getroot()
	rootTwo = xml_doc_two.getroot()
	
	firstSha  = rootOne.find('res').text
	secondSha = rootTwo.find('res').text
	
	assert merger.checkSha(firstSha, secondSha) == True

def test_merge():

	xml_doc_one = etree.parse(open("output/aa/aa.xml"))
	xml_doc_two = etree.parse(open("output/aaa/aaa.xml"))
	
	rootOne = xml_doc_one.getroot()
	rootTwo = xml_doc_two.getroot()
	
	firstSha  = rootOne.find('res').text
	secondSha = rootTwo.find('res').text
	
	firstArtefacts  = rootOne.find('data')
	secondArtefacts = rootTwo.find('data')

	merger.mergeFiles(rootOne, rootTwo, secondArtefacts)	
	
	one = open("files/merged.xml")
	two = open("./merged.xml")

	one = one.read().strip()
	two = two.read().strip()
	assert ( one == two )

	
