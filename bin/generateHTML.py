#!/usr/bin/env python3

import sys, os
from html5print import HTMLBeautifier

#Initialize variables with arguments for better overview
json = sys.argv[1]
html = sys.argv[2]

#Create an temporary html file
file = open("tmp.html","w")

#Generates an unformatted html file from an json file
os.system("python3 ./bin/htmlPython.py "+json+" > "+html)

#Writes the unformatted html file into our temporary html file formatted
file.write(HTMLBeautifier.beautify(open(html), 4))
file.close()

print("Generated HTML Sucessfully")
