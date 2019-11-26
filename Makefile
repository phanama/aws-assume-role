lint:
	autopep8 -irv aws_assume_role/
	autopep8 -irv tests/

test:
	python3 -m unittest tests/*.py
