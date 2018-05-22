#!/usr/bin/env python3

"""
This module generates the HTML out of an JSON file. It first generates the HTML code with the help of "htmlPython.py" module then beautify it for simpler reading.
"""

import sys, os
from html5print import HTMLBeautifier

def generateHTML(json, html):

	#Create an temporary html file
	file = open("tmp.html","w")

	#Generates an unformatted html file from an json file
	os.system("python3 ./rev/scripts/htmlPython.py "+json+" "+html)

	#Writes the unformatted html file into our temporary html file formatted
	file.write(HTMLBeautifier.beautify(open(html), 4))
	file.close()

def main(args=None):
	
	#Initialize variables with arguments for better overview
	json = sys.argv[1]
	html = sys.argv[2]

	generateXML(json, html)
	print("Generated HTML Sucessfully")

if __name__ == '__main__':
	main()
