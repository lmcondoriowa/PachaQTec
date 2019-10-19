from flask import request
from app.controllers.Role import Role

role = Role()

def route_role(app):
    @app.route('/roles/all')
    def roles_all():
        return role.all_role(app)

    @app.route('/roles/find/<role_id>')
    def roles_find(role_id):
        return role.find_role(role_id, app)

    @app.route('/roles/add', methods=['POST'])
    def roles_add():
        values = request.values
        role.name = values.get('name')
        role.state = values.get('state')
        return role.add_role(role, app)

    @app.route('/roles/update', methods=['PUT'])
    def roles_udpate():
        values = request.values
        role_id = values.get('role_id')
        role.name = values.get('name')
        role.state = values.get('state')
        return role.update_role(role, role_id, app)

    @app.route('/roles/delete/<role_id>', methods=['DELETE'])
    def roles_delete(role_id):
        return role.delete_role(role_id, app)