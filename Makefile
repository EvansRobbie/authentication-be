.PHONY: runserver
runserver:
	poetry run py manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run py manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run py manage.py migrate