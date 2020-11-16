clean:
	rm -rf coverage/
	rm -rf logs/*
	rm -rf .pytest_cache
	rm test.db
	coverage erase

install:
	python3.8 -m pip install --upgrade -r requirements.txt

lint:
	python3.8 -m flake8 src/

test:
	python3.8 -m pytest --cov-report html:coverage --cov-report term-missing --cov=src ./ -vv
	@rm test.db
	@rm .coverage
	@rm -rf .pytest_cache/

testerrors:
	python3.8 -m pytest -rfs -vv
	@rm test.db

dev:
	python3.8 run.py

prod:
	python3.8 run.py --env production
