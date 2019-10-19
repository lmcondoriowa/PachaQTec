import os
from orator import DatabaseManager, Model
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Conexion:
    def __init__(self):
        self.default = os.getenv('DB_DEFAULT')
        self.driver = os.getenv('DB_DRIVER')
        self.host = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.prefix = os.getenv('DB_PREFIX')

    def initialize(self):
        config = {
            'default': self.default,
            'mysql': {
                'driver': self.driver,
                'host': self.host,
                'database': self.database,
                'user': self.user,
                'password': self.password,
                'prefix': self.prefix
            }
        }

        try:
            db = DatabaseManager(config)
            return db
        except Exception as e:
            print(f'Error : {str(e)}')

    def model(self):
        conn = self.initialize()
        Model.set_connection_resolver(conn)
        return Model
