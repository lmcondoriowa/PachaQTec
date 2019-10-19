from database.config import Conexion

conn = Conexion()
Model = conn.model()

class User(Model):
    __table__ = 'users'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['username', 'userpass', 'name', 'last_name', 'age']

    __casts__ = {
        'name': 'str',
        'last_name': 'str',
        'age': 'int'
    }