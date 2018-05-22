from lxml import etree
import sys
import os
import re
import bin.generateXML as xm

def test_args():
	
	plim = "test.plim"
	xml = "test.xml"

	assert xm.checkArgs(plim ,xml)	

def test_validate():

	xml = open("output/aaa/aaa.xml")
	assert xm.validateXML(xml)
