#!/usr/bin/env python3

import json, re, graphviz as gv, sys

def generateGraph(artefacts):

	g = gv.Graph(format='svg')
	g.format = 'svg'
	regex = r"(.*)\/"
	subst = ""

	pkgs = {}
	g.node('packages', shape='square')

		
	for artefact in artefacts:
		
		where = artefact['loc']
		what  = artefact['type']
		name  = artefact['name']
		level = artefact['level']
		descr = artefact['descr']
		
		match = re.match(regex, where)
		result  = re.sub(regex, subst, where, 0, re.MULTILINE)
		
		packageName = match.group(1)
		if 'malicious' in level:
			color = 'red'
		else:
			color = 'yellow'


		if packageName not in pkgs:
		
			pkgs[packageName] = ''
			g.node(packageName)
			g.edge('packages', packageName)
			g.node("file"+packageName, "file")
			g.edge(packageName, "file"+packageName)
		
		g.node(what+packageName, what)
		g.edge(result+packageName, what+packageName)


		g.node(result+packageName, result)
		g.edge("file"+packageName, result+packageName)		

		g.node(name+packageName, name, style="filled", fillcolor=color)
		g.edge(what+packageName, name+packageName)

	return g	

def main(args=None):
 

	jsonFile = sys.argv[1]
	j = json.load(open(jsonFile))

	artefacts = j['analysis']['data']['art']

	

	assert len(sys.argv) % 2 == 0, "All operations must be paired with a file."
	if isinstance(artefacts, dict):
        	artefacts = [artefacts]

	g = generateGraph(artefacts)
	g.render()
	print("Graph generated successfully")

if __name__ == '__main__':
	main()
	
