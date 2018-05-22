#!/usr/bin/env python3

import sys, os, re
from lxml import etree

def formatXML(xml,parser):

	xmldoc = etree.parse(xml, parser)
	os.remove(xml)
	xmldoc.write(xml, encoding="utf-8", pretty_print=True)

def main(args=None):

	xml = sys.argv[1]
	parser = etree.XMLParser(remove_blank_text=True)
	formatXML(xml,parser)

if __name__ == '__main__':
	main()
