from database.config import Conexion

conn = Conexion()
Model = conn.model()

class Business(Model):
    __table__ = 'business'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'

    __fillable__ = ['name', 'ruc', 'address']

    __casts__ = {
        'name': 'str',
        'ruc': 'str',
        'address': 'str'
    }