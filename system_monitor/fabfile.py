import os

from fabric.api import local, task
from fabric.decorators import runs_once

BASE_DIR = os.path.sep.join((os.path.dirname(__file__), ''))

@task
@runs_once
def makemigrate():
   local('python manage.py makemigrations')

@task
@runs_once
def migrate():
   local('python manage.py migrate')

@task
@runs_once
def shell():
   local('python manage.py shell')

@task
@runs_once
def runserver():
   local('python manage.py runserver')


