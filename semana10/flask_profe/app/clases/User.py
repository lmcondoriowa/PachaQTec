from database.config import Conexion
from helper import helper


class User:
    def __init__(self, name=None, last_name=None, age=None):
        self.name = name
        self.last_name = last_name
        self.age = age

    def all_user(self, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            users = db.table('users').get()
            result = {}
            if users:
                result = users.serialize()
            return helper.handler_response(app, 201, 'Lista de Usuarios', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_user(self, user_id, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            users = db.table('users').where('id', user_id).first()
            result = {}
            if users:
                result = users.serialize()
            return helper.handler_response(app, 201, f'Buscar useri_id: {user_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def add_user(self, user, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            db.table('users').insert({
                'name': user.name,
                'last_name': user.last_name,
                'age': user.age
            })
            message = f'''Se agregó el usuario : {user.name} {user.last_name}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_user(self, user, user_id, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            update = db.table('users') \
                .where( 'id', user_id) \
                .update({
                    'name': user.name,
                    'last_name': user.last_name,
                    'age': user.age
                })

            message = f'''No se encontró el user_id : {user_id}'''

            if update > 0:
                message = f'''Se actualizó el user_id : {user_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_user(self, user_id, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            delete = db.table('users').where('id', user_id).delete()
            message = f'''No se encontró el user_id : {user_id}'''
            if delete:
                message = f'''Se eliminó el user_id : {user_id}'''
            return helper.handler_response(app, 201, f'Buscar user i_id: {user_id}', message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')