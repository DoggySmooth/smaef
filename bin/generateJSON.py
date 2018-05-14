#!/usr/bin/env python3

import sys, os, json, collections

#Initialize variables for better overview
json = sys.argv[1]
xml  = sys.argv[2]

#Generates an unformatted JSON file from an XML file stripping unwanted strings
os.system("lib/xml2json.py -t xml2json -o "+json+" "+xml+" --strip_text")

#Checks if the format of the JSON file is valide
os.system("lib/jsonlint "+json)

#Format JSON file for a better overview
os.system("python -m json.tool "+json+" > tmp.json")

print("Generatedd JSON Sucessfully!")
