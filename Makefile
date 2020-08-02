.PHONY: enigma

app:
	python3 enigma

cmd: 
	python3 enigma/cmd.py

setup:
	pip3 install -r requirements.txt