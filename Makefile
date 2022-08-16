clean:
#	rm -rf ./venv
	rm -rf __pycache__

venv:
	python -m venv ./venv

run:
	python app/main.py

lint:
	@isort --check app

isort-fix:
	@isort app

autopep-fix:
	@autopep8 --in-place --recursive ./app

autoflake-fix:
	@autoflake8 --in-place --recursive ./app

lint-fix:
	@make autopep-fix --no-print-directory
	@make autoflake-fix --no-print-directory
	@make isort-fix --no-print-directory

requirements-dev:
	@pip install -r requirements/dev.txt

requirements-test:
	@pip install -r requirements/test.txt