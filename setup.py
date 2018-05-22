#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    scripts=[
    
	'amrev.py',
	'lib/xml2json.py',
	'rev/scripts/generateGraph.py',
	'rev/scripts/generateJSON.py',
	'rev/scripts/generateHTML.py',
	'rev/scripts/generateXML.py',
	'rev/scripts/htmlPython.py',
	'rev/scripts/xmlFormatter.py',
	'rev/scripts/xmlMerger.py'
    ]
)
