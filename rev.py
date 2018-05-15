#!/usr/bin/env python3

import os, sys

def main():

	if sys.argv[1] == '-m':
		fileOne = sys.argv[2]
		fileTwo = sys.argv[3]

		os.system("./rev/scripts/xmlMerger.py "+fileOne+" "+fileTwo)
		os.system("./rev/scripts/xmlFormatter.py merged.xml")
		print("Make sure you change merged.xml file location!\nConsecutive execution will overwrite the file!")

	else:
		targetPLIM = sys.argv[1]

		name = os.path.basename(targetPLIM)
		name = os.path.splitext(name)[0]

		base = os.path.splitext(targetPLIM)[0]	

		targetXML  = base+'.xml'
		targetJSON = base+'.json'
		targetHTML = base+'.html'
		
		os.system('./rev/scripts/generateXML.py '+targetPLIM+' '+targetXML)
		
		os.system('./rev/scripts/generateJSON.py '+targetJSON+' '+targetXML)

		os.system('./rev/scripts/generateHTML.py '+targetJSON+' '+targetHTML)

		os.system('./rev/scripts/generateGraph.py '+targetJSON)
		
		os.remove("Graph.gv")
		if not os.path.exists('output/'+name):
			os.makedirs('output/'+name)
		
		for filename in os.listdir("."):
			if filename.startswith("tmp"):
				os.rename(filename, 'output/'+name+'/'+name+filename[3:])
			if filename.startswith("Graph"):
				os.rename(filename, 'output/'+name+'/'+filename)
		

		os.remove('./plims/'+name+'.json')
		os.remove('./plims/'+name+'.xml')
		os.remove('./plims/'+name+'.html')

if __name__ == '__main__':
	main()
