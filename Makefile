.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser
