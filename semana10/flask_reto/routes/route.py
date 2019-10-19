from routes import route_business, route_user, route_role, route_business_roles_user

def routes(app):
    @app.route('/')
    def hello_world():
        return '<h1>Hola pachaqtec</h1>'

    route_business.route_business(app)
    route_user.route_user(app)
    route_role.route_role(app)
    route_business_roles_user.route_business_roles_user(app)


