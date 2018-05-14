import json, re, graphviz as gv, sys

g = gv.Graph(format='svg')

jsonFile = sys.argv[1]

j = json.load(open(jsonFile))


artefacts = j['analisis']['artefacts']['artefact']

regex = r"(.*)\."
subst = ""


def generateGraph(artefacts):

	pkgs = {}
	g.node('packages', shape='square')

		
	for artefact in artefacts:
		
		where = artefact['where']
		what  = artefact['what']
		name  = artefact['name']
		level = artefact['level']
		descr = artefact['description']
		
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
			
		g.node(what)
		g.node(name, name, style="filled", fillcolor=color)
		g.edge(packageName, what)
		g.edge(what, name)

	

if isinstance(artefacts, dict):
        artefacts = [artefacts]

generateGraph(artefacts)
g.render()
