import bin.generateGraph as graph
import json

def test_graph():

	output = open("files/test.txt")
	output = output.read().strip()
	
	j = json.load(open("output/aaa/aaa.json"))

	artefacts = j['analysis']['data']['art']
	
	if isinstance(artefacts, dict):
		artefacts = [artefacts]

	g = graph.generateGraph(artefacts)
	g = str(g).strip()
	
	assert g == output

