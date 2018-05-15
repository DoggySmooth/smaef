#content of test_graph.

import os, json, graphviz as gv
from generateGraph import generateGraph

def test_openFile():
    with  open("../res/outs/outGraphSingle.txt") as content:
        expected = content.read()
    j = json.load(open("files/singleArtefact.json"))
    artefacts = j['analisis']['artefacts']['artefact']
    if isinstance(artefacts, dict):
        artefacts = [artefacts]

    print(expected)
    print(generateGraph(artefacts))
    assert expected.strip() == str(generateGraph(artefacts)).strip() 

#def test_rightExt(graph):
#    response, msg = smtp.noop()
#    assert response == 250
#    assert 0  # for demo purposes

#def test_singleArtefact(graph):
#    response, msg = smtp.ehlo()
#    assert response == 250
#    assert b"smtp.gmail.com" in msg
#    assert 0  # for demo purposes

#def test_multipleArtefact(graph):
#    response, msg = smtp.noop()
#    assert response == 250
#    assert 0  # for demo purposes
