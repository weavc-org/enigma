.PHONY: enigma

web:
	python3 enigma --web

setup:
	pipenv shell
	pipenv install