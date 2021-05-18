FROM python:3.8-alpine

ENV PYTHONBUFFERED 1

COPY . .

# Install Packages
RUN pip install --upgrade pip wheel setuptools
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt

# Remove redundant files
RUN find -type d -name __pycache__ -prune -exec rm -rf {} \;
RUN rm -rf ~/.cache/pip

EXPOSE 8000

WORKDIR /app
