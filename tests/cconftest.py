#!/usr/bin/env python3

import pytest
import os 

@pytest.fixture(scope="module")
def smtp():
	return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

@pytest.fixture(scope="module")
def graph():
	return print(os.system("bin/generateGraph.py files/singleArtefact.json")) 

