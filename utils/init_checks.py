from django.db import connection
from time import sleep
from utils.logger import logger



def check_db_connection():
    try:
        connection.ensure_connection()
    except Exception as e:
        logger.error("Error during connecting to the database : {}".format(e))
        sleep(1)
        return False
    else:
        logger.info("Database connection has established.")
        return True