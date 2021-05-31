import environ

from monitor_api.models import User
from utils import logger

env = environ.Env()
env.read_env(".env/.app")

def run():
    try:
        su = User.objects.create_superuser(
            username=env('APP_DEFAULT_USER_NAME'),
            password=env('APP_DEFAULT_USER_PASS'),
            email=env('APP_DEFAULT_USER_EMAIL'),
        )
        su.save()
        logger.info("User created: '%s'" % env('APP_DEFAULT_USER_NAME'))
    except Exception as e:
        logger.error(f"Error occured during creating a superuser: {e}")