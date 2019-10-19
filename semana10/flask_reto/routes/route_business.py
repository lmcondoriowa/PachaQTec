from flask import request
from app.controllers.Business import Business

business = Business()

def route_business(app):    
    @app.route('/business/all')
    def business_all():
        return business.all_business(app)

    @app.route('/business/find/<business_id>')
    def business_find(business_id):
        return business.find_business(business_id, app)

    @app.route('/business/add', methods=['POST'])
    def business_add():
        values = request.values
        business.name = values.get('name')
        business.ruc = values.get('ruc')
        business.address = values.get('address')
        return business.add_business(business, app)

    @app.route('/business/update', methods=['PUT'])
    def business_udpate():
        values = request.values
        business_id = values.get('business_id')
        business.name = values.get('name')
        business.last_name = values.get('last_name')
        business.age = values.get('age')
        return business.update_business(business, business_id, app)

    @app.route('/business/delete/<business_id>', methods=['DELETE'])
    def business_delete(business_id):
        return business.delete_business(business_id, app)