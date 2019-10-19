import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DATABASES = {
    'mysql': {
        'driver': os.getenv('DB_DRIVER'),
        'host': os.getenv('DB_SERVER'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'prefix': ''
    }
}