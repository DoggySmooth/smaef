#!/usr/bin/env python3

import sys, os, re
from lxml import etree

xml = sys.argv[1]

parser = etree.XMLParser(remove_blank_text=True)
xmldoc = etree.parse(xml, parser)
xmldoc.write("mergedFile.xml", encoding="utf-8", pretty_print=True)
print(xml)
os.remove(xml)


