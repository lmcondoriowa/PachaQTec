from app.models.business_roles_user import Business_roles_user as Business_roles_userModel
from helper import helper


class Business_roles_user:
    def __init__(self, business_id=None, users_id=None, roles_id=None):
        self.business_id = business_id
        self.users_id = users_id
        self.roles_id = roles_id

    def all_business_roles_user(self, app):
        try:
            business_roles_users = Business_roles_userModel.get()
            result = {}
            if business_roles_users:
                result = business_roles_user.serialize()
            return helper.handler_response(app, 201, 'Lista de Pivot', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_business_roles_user(self, business_roles_user_id, app):
        try:
            business_roles_users = Business_roles_userModel.where('id', business_roles_user_id).first()
            result = {}
            if business_roles_users:
                result = business_roles_users.serialize()
            return helper.handler_response(app, 201, f'Buscar role_id: {business_roles_user_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def add_business_roles_user(self, business_roles_user, app):
        try:
            Business_roles_userModel.insert({
                'business_id': business_roles_user.business_id,
                'users_id': business_roles_user.users_id,
                'roles_id': business_roles_user.roles_id
            })
            message = f'''Se agregó el business_roles_user : {business_roles_user.business_id} {business_roles_user.users_id}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_business_roles_user(self, business_roles_user, business_roles_user_id, app):
        try:
            update = Business_roles_userModel \
                .where( 'id', business_roles_user_id) \
                .update({
                    'business_id': business_roles_user.business_id,
                    'users_id': business_roles_user.users_id,
                    'roles_id': business_roles_user.roles_id
                })

            message = f'''No se encontró el robusiness_roles_user_id : {business_roles_user_id}'''

            if update > 0:
                message = f'''Se actualizó el business_roles_user_id : {business_roles_user_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_business_roles_user(self, business_roles_user_id, app):
        try:
            delete = Business_roles_userModel.where('id', business_roles_user_id).delete()
            message = f'''No se encontró el business_roles_user_id : {business_roles_user_id}'''
            if delete:
                message = f'''Se eliminó el business_roles_user_id : {business_roles_user_id}'''
            return helper.handler_response(app, 201, f'Buscar business_roles_user id: {business_roles_user_id}', message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')
