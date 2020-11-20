

init:
	apt update -y
	apt install -y python3
	apt install -y python3-setuptools
	apt install -y python3-pip
	pip3 install -r requirements.txt

test: init
	python3 -c "import test;test.main()"  

benchmark: init
	python3 -c "import cProfile;cProfile.run('import test;test.main()');"  

run: test
	python3 main.py 