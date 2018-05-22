#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    scripts=[
    
	'ammet.py',
	'lib/xml2json.py',
	'met/scripts/generateGraph.py',
	'met/scripts/generateJSON.py',
	'met/scripts/generateHTML.py',
	'met/scripts/generateXML.py',
	'met/scripts/htmlPython.py',
	'met/scripts/xmlFormatter.py',
	'met/scripts/xmlMerger.py'
    ]
)
