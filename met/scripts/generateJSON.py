#!/usr/bin/env python3

"""
This module generates a JSON file out of the xml. Validate the JSON format and finally pretty print it.
"""

import sys, os, json, collections

def generateJSON(xml, jsonName):

	#Generates an unformatted JSON file from an XML file stripping unwanted strings
	os.system("lib/xml2json.py -t xml2json -o "+jsonName+" "+xml+" --strip_text")

def validateJSON(jsonName):
	#Checks if the format of the JSON file is valide
	with open(jsonName) as f:
		json.loads(f.read())
		print("JSON is valid!")
	#Format JSON file for a better overview
	os.system("python -m json.tool "+jsonName+" > tmp.json")


def main(args=None):

	#Initialize variables for better overview
	json = sys.argv[1]
	xml  = sys.argv[2]
	
	generateJSON(xml, json)
	validateJSON(json)

	print("Generated JSON Sucessfully!")

if __name__ == '__main__':
	main()
