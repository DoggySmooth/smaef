SHELL = /bin/sh


all: initialize test

initialize :
	python3 test.py files/aaa.plim
	python3 test.py files/aa.plim	

test: initialize
	/home/smoothz/.local/bin/pytest
	
