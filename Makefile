JAR_PATH = ./target
PORT = 8080

init:
	sudo apt update -y
	sudo apt install -y python3.8
	sudo apt install -y python3-pip
	pip3 install -r requirements.txt

test: init
	python3 -c "import test;test.main()"  

benchmark: init
	python3 -c "import cProfile;cProfile.run('import factoriel;factoriel.main()');"  

run: test
	kill $$(lsof -t -i:${PORT}) | true
	python3 main.py &