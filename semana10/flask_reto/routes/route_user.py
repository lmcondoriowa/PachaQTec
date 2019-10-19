from flask import request
from app.controllers.User import User

user = User()

def route_user(app):
    @app.route('/users/all')
    def users_all():
        return user.all_user(app)

    @app.route('/users/find/<user_id>')
    def users_find(user_id):
        return user.find_user(user_id, app)

    @app.route('/users/add', methods=['POST'])
    def users_add():
        values = request.values
        user.name = values.get('name')
        user.last_name = values.get('last_name')
        user.age = values.get('age')
        return user.add_user(user, app)

    @app.route('/users/update', methods=['PUT'])
    def users_udpate():
        values = request.values
        user_id = values.get('user_id')
        user.name = values.get('name')
        user.last_name = values.get('last_name')
        user.age = values.get('age')
        return user.update_user(user, user_id, app)

    @app.route('/users/delete/<user_id>', methods=['DELETE'])
    def users_delete(user_id):
        return user.delete_user(user_id, app)