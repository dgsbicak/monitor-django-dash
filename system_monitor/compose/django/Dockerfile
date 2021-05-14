FROM python:3.8-alpine

ENV PYTHONBUFFERED 1

RUN mkdir /static
RUN mkdir -p /src/app

WORKDIR /src/app

COPY . .

# Install Packages
RUN pip install --upgrade pip wheel setuptools
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install --no-cache-dir -r requirements.txt

# Remove redundant files
RUN find -type d -name __pycache__ -prune -exec -rm -rf {} \;
RUN rm -rf ~/.cache/pip



EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --no-input; gunicorn system_monitor.wsgi -b 0.0.0.0:8000 -w 4"]
