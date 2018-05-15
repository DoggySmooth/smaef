import json
import sys

def firstpart():
#First part of the html page
	print('<!DOCTYPE html><html lang="en"><head><title>Smoothin</title><meta name="description" content="Login"><meta name="Smooth" content="SitePoint"><link rel="stylesheet" href="../../res/styles/style.css" type="text/css"><script type="application/javascript">function toggle(attr) {var choice = document.getElementById(attr).style.display; if (choice == "block"){document.getElementById(attr).style.display = "none"; } else {document.getElementById(attr).style.display = "block"; }}</script></head><body><div class="horizontal-menu"><a class="search"> Teeeeeeeeeeeeeeeeeeeeest </a></div><div class="vertical-menu"><a class="logo">REV</a><a>Link 1</a><a>Link 2</a><a>Link 3</a><a> Link 4 </a></div><div class="content"><div class="box"><div class="box-header"><a> App </a></div><div class="box-content"></div>')

#Function that generates the content of the web page based on the JSON file
def generateHTML(metas, artefacts, sha256):
	i = 0
	print('<div class="box-header"><a> Metas </a></div>')
	for infos in metas:
		index = i
		i += 1
		date = infos['date']
		access = infos['access']
		accessloc = infos['accessloc']
		author = infos['author']
		email = infos['email']
		permission = infos['permission']
		tags = infos['tags'].split(',')

		print('<div class="box-header"><a> Author '+str(author)+' with index '+str(i)+' </a></div>')
		print('<div class="meta-body" id="authorContent" ><table summary="Author Content">')
		
		print("<table><tr><td>Date</td><td>access</td><td>access location</td><td>email</td><td>permission</td></tr><tr><td>"+date+"</td><td> "+access+"</td><td> "+accessloc+" </td><td> "+email+"</td><td> "+permission+"</td></tr></table>")	
		print('<div class="box-header"><a>Malware Tags</a></div><table><tr>')
		for items in tags:
			print("<td>"+items+"</td>")
		print("</tr></table>")

	print('<div class="box-header"><a> Analysis </a></div>')
	print('<div class="box-header"><a> Artefacts: '+str(sha256)+'.apk</a></div>')
	
	for artefact in artefacts:
		where = artefact['loc']
		what  = artefact['type']
		name  = artefact['name']
		level = artefact['level']
		descr = artefact['descr']


	
		print('<div class="box-body" id="artefactsContent" ><table summary="Artefacts Content">')
		print('<tr><td><b>Where</b></td><td><b>What</b></td><td><b>Name</b></td><td><b>Level</b></td></tr>')
		print('<tr><td>'+where+'</td><td>'+what+'</td><td>'+name+'</td><td>'+level+'</td></tr></table>')
		print('<table><tr><td style="width: 100%;">'+descr+'</td></tr>')
		print('</table></div>')





def main(args=None):

	#Loads the json file in an variable j
	j = json.load(open(sys.argv[1]))

	sha256 = j['analysis']['res']
	artefacts = j['analysis']['data']['art']
	metas = j['analysis']['met']

	firstpart()
	#Checks if the key artefact is an dict, in case there is just one artefact, and tranforms it in an list for manipulation purpose. 
#If there are multiple artefact tags, a list is impicity created instead of an dict. 
#So by transforming the dict into a list we can use the same code to gather data of the JSON file.
	if isinstance(artefacts, dict):
		artefacts = [artefacts]
	
	if isinstance(metas, dict):
		metas = [metas]

	generateHTML(metas, artefacts, sha256)

	#Lower part of the HTML file
	print('</div></div></div></html>')



if __name__ == '__main__':
	main()
