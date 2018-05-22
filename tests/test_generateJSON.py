import json

def test_validate():

	with open("output/aa/aa.json") as f:
		json.loads(f.read())
