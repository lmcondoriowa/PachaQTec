from app.models.business import Business as BusinessModel
from helper import helper


class Business:
    def __init__(self, name=None, ruc=None, address=None):
        self.name = name
        self.ruc = ruc
        self.address = address

    def all_business(self, app):
        try:
            business = BusinessModel.get()
            result = {}
            if business:
                result = business.serialize()
            return helper.handler_response(app, 201, 'Lista de Empresas', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def find_business(self, business_id, app):
        try:
            business = BusinessModel.where('id', business_id).first()
            result = {}
            if business:
                result = business.serialize()
            return helper.handler_response(app, 201, f'Buscar user_id: {business_id}', result)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def add_business(self, business, app):
        try:
            BusinessModel.insert({
                'name': business.name,
                'ruc': business.ruc,
                'address': business.address
            })
            message = f'''Se agregó la empresa : {business.name} {business.ruc}'''
            print(message)
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def update_business(self, business, business_id, app):
        try:
            update = BusinessModel \
                .where( 'id', business_id) \
                .update({
                    'name': business.name,
                    'ruc': business.ruc,
                    'address': business.address
                })

            message = f'''No se encontró el business_id : {business_id}'''

            if update > 0:
                message = f'''Se actualizó el business_id : {business_id}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')

    def delete_business(self, business_id, app):
        try:
            delete = BusinessModel.where('id', business_id).delete()
            message = f'''No se encontró el business_id : {business_id}'''
            if delete:
                message = f'''Se eliminó el business_id : {business_id}'''
            return helper.handler_response(app, 201, f'Buscar business_id: {business_id}', message)
        except Exception as e:
            return helper.handler_response(app, 500, f'{str(e)}')