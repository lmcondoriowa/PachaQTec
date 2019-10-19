from app.models.role import Role as RoleModel
from helper import helper


class Role:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def all_role(self, app):
        try:
            roles = RoleModel.get()
            result = {}
            if roles:
                result = roles.serialize()
            return helper.handler_response(app, 201, 'Lista de Roles', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_role(self, role_id, app):
        try:
            roles = RoleModel.where('id', role_id).first()
            result = {}
            if roles:
                result = roles.serialize()
            return helper.handler_response(app, 201, f'Buscar role_id: {role_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def add_role(self, role, app):
        try:
            RoleModel.insert({
                'name': role.name,
                'state': role.state
            })
            message = f'''Se agregó el role : {role.name} {role.state}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_role(self, role, role_id, app):
        try:
            update = RoleModel \
                .where( 'id', role_id) \
                .update({
                    'name': role.name,
                    'state': role.state
                })

            message = f'''No se encontró el role_id : {role_id}'''

            if update > 0:
                message = f'''Se actualizó el role_id : {role_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_role(self, role_id, app):
        try:
            delete = RoleModel.where('id', role_id).delete()
            message = f'''No se encontró el role_id : {role_id}'''
            if delete:
                message = f'''Se eliminó el role_id : {role_id}'''
            return helper.handler_response(app, 201, f'Buscar role i_id: {role_id}', message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')