#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;

if [ -z "$( psql -U "$POSTGRES_USER" -lqtA | cut -d\| -f1 | grep -Fx "$APP_DB_NAME" )" ]
then
  echo "Database '$POSTGRES_DB' doesn't exist, creating a new one."
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
    CREATE DATABASE $APP_DB_NAME;
    GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
    ALTER USER $APP_DB_USER CREATEDB;
EOSQL
else
  echo "Database '$POSTGRES_DB' already exists."
fi