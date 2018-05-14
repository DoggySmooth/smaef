import json
import sys

#Loads the json file in an variable j
j = json.load(open(sys.argv[1]))

#First part of the html page
print('<!DOCTYPE html><html lang="en"><head><title>Smoothin</title><meta name="description" content="Login"><meta name="Smooth" content="SitePoint"><link rel="stylesheet" href="../../res/styles/style.css" type="text/css"><script type="application/javascript">function toggle(attr) {var choice = document.getElementById(attr).style.display; if (choice == "block"){document.getElementById(attr).style.display = "none"; } else {document.getElementById(attr).style.display = "block"; }}</script></head><body><div class="horizontal-menu"><a class="search"> Teeeeeeeeeeeeeeeeeeeeest </a></div><div class="vertical-menu"><a class="logo">Jaro</a><a>Link 1</a><a>Link 2</a><a>Link 3</a><a> Link 4 </a></div><div class="content"><div class="box"><div class="box-header"><a> App </a></div><div class="box-content"></div>')

#Function that generates the content of the web page based on the JSON file
def generateHTML(artefacts, sha256):

	print('<div class="box-header"><a> Artefacts: '+sha256+'.apk</a></div>')
	
	for artefact in artefacts:
		where = artefact['where']
		what  = artefact['what']
		name  = artefact['name']
		level = artefact['level']
		descr = artefact['description']


	
		print('<div class="box-body" id="artefactsContent" ><table summary="Artefacts Content">')
		print('<tr><td><b>Where</b></td><td><b>What</b></td><td><b>Name</b></td><td><b>Level</b></td></tr>')
		print('<tr><td>'+where+'</td><td>'+what+'</td><td>'+name+'</td><td>'+level+'</td></tr></table>')
		print('<table><tr><td style="width: 100%;">'+descr+'</td></tr>')
		print('</table></div>')



sha256 = j['analisis']['sha256']
artefacts = j['analisis']['artefacts']['artefact']


#Checks if the key artefact is an dict, in case there is just one artefact, and tranforms it in an list for manipulation purpose. 
#If there are multiple artefact tags, a list is impicity created instead of an dict. 
#So by transforming the dict into a list we can use the same code to gather data of the JSON file.
if isinstance(artefacts, dict):
	artefacts = [artefacts]
	
generateHTML(artefacts, sha256)

#Lower part of the HTML file
print('</div></div></div></html>')



