from flask import request
from app.classes.Area import Area

area = Area()

def route_area(app):
    @app.route('/areas')
    def areas_listar():
        return area.area_listar(app)

    @app.route('/areas/add', methods=['POST'])
    def areas_add():
        values = request.values
        area.descripcion = values.get('descripcion')
        return area.area_add(area, app)

    @app.route('/areas/edit/<id>', methods=['PUT'])
    def areas_edit(id):
        values = request.values
        area.descripcion = values.get('descripcion')
        return area.area_actualizar(id, area, app)

    @app.route('/area/delete/<id>', methods=['DELETE'])
    def areas_delete(id):
        return area.area_eliminar(id, app)