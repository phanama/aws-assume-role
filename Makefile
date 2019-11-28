lint:
	autopep8 -irv aws_assume_role/
	autopep8 -irv tests/
	autopep8 -irv setup.py

test:
	python3 -m unittest tests/*.py

build:
	rm -rf dist/*
	python3 setup.py sdist bdist_wheel

release:
	twine upload dist/*
