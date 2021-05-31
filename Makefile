
migrations:
	docker-compose run --rm web python manage.py makemigrations
migrate:
	docker-compose run --rm web python manage.py migrate
runserver:
	docker-compose run --rm web python manage.py runserver 0.0.0.0:8000
runcorn:
	docker-compose run --rm web gunicorn middleware.wsgi -b 0.0.0.0:8000 -w $(nproc)
test:
	docker-compose run --rm web python manage.py test -v 2
dbcheck:
	docker-compose run --rm web python manage.py check --database default
shell:
	docker-compose run --rm web python manage.py shell
collect:
	docker-compose run --rm web  python manage.py collectstatic
up:
	docker-compose up -d
down:
	docker-compose down
restart:
	docker-compose restart
resweb:
	docker-compose restart web
log:
	docker-compose logs -f --tail 100
logweb:
	docker-compose logs -f --tail 100 web
