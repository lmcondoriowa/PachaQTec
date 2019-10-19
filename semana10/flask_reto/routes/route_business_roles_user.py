from flask import request
from app.controllers.Business_roles_user import Business_roles_user

business_roles_user = Business_roles_user()

def route_business_roles_user(app):
    @app.route('/business_roles_users/all')
    def business_roles_users_all():
        return business_roles_user.all_business_roles_user(app)

    @app.route('/business_roles_users/find/<business_roles_user_id>')
    def business_roles_users_find(business_roles_user_id):
        return business_roles_user.find_business_roles_user(business_roles_user_id, app)

    @app.route('/business_roles_users/add', methods=['POST'])
    def business_roles_users_add():
        values = request.values
        business_roles_user.name = values.get('name')
        business_roles_user.state = values.get('state')
        return business_roles_user.add_business_roles_user(business_roles_user, app)

    @app.route('/business_roles_users/update', methods=['PUT'])
    def business_roles_users_udpate():
        values = request.values
        business_roles_user_id = values.get('business_roles_user_id')
        business_roles_user.name = values.get('name')
        business_roles_user.state = values.get('state')
        return business_roles_user.update_business_roles_user(business_roles_user, business_roles_user_id, app)

    @app.route('/business_roles_users/delete/<business_roles_user_id>', methods=['DELETE'])
    def business_roles_users_delete(business_roles_user_id):
        return business_roles_user.delete_business_roles_user(business_roles_user_id, app)