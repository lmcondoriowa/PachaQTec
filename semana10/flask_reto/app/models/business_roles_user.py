from database.config import Conexion

conn = Conexion()
Model = conn.model()

class Business_roles_user(Model):
    __table__ = 'roles'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'mysql'
    __hidden__ = ['created_at', 'updated_at']
    __fillable__ = ['business_id', 'users_id', 'roles_id']

    __casts__ = {
        'business_id': 'int',
        'users_id': 'int',
        'roles_id': 'int'
    }