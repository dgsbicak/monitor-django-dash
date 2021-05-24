from .logger import *
from .checker import *
from .init_checks import *


for n in range(5):
    if check_db_connection():
        break
    