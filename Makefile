.PHONY: enigma

serve:
	pipenv run python enigma serve

docker:
	docker build -t enigma:latest .

docker-quick-run:
	-docker stop enigma && docker rm enigma
	docker run -it --name enigma -p 8080:8080 enigma:latest

setup:
	pipenv install