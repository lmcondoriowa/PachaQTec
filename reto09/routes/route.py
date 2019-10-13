from routes import route_employee, route_area, route_cargo, route_grupo


def routes(app):
    route_employee.route_employee(app)
    route_area.route_area(app)
    route_cargo.route_cargo(app)
    route_grupo.route_grupo(app)

