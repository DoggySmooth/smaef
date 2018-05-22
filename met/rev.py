#!/usr/bin/env python3

import os, sys

def main():

	targetPLIM = sys.argv[1]
	base = os.path.splitext(targetPLIM)[0]	

	targetXML  = base+'.xml'
	targetJSON = base+'.json'
	targetHTML = base+'.html'
	
	os.system('./scripts/generateXML.py '+targetPLIM+' '+targetXML)

if __name__ == '__main__':
	main()
