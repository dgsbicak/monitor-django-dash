
makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver 0.0.0.0:8000

test:
	python manage.py test -v 2

shell:
	python manage.py shell

removemigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

runcorn:
	gunicorn middleware.wsgi -b 0.0.0.0:8000 -w 8

collect:
	python manage.py collectstatic

up:
	docker-compose up -d
