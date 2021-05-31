

import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Waits for database to be available.'

    def add_arguments(self, parser):
        parser.add_argument('--nsleep', type=int, default=1, help="Sleep for 'n' seconds before each try")

    def handle(self, *args, **kwargs):
        """ Handle the command """
        self.stdout.write('Waiting for database...')
        db_conn = None
        for n in range(5):
            try:
                connection.ensure_connection()
                db_conn = True
                break
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(f'Database is unavailable. Retry:{n}, waiting {kwargs["nsleep"]} second...')
                )
                time.sleep(kwargs["nsleep"])
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Database Error: {str(e)}"))

        if db_conn:
            self.stdout.write(self.style.SUCCESS('Database is available!'))
        else:
            self.stdout.write(self.style.ERROR('Database is not available!'))