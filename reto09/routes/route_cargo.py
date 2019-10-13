from flask import request
from app.classes.Cargo import Cargo

cargo = Cargo()

def route_cargo(app):
    @app.route('/cargos')
    def cargos_listar():
        return cargo.cargo_listar(app)

    @app.route('/cargos/add', methods=['POST'])
    def cargos_add():
        values = request.values
        cargo.descripcion = values.get('descripcion')
        return cargo.cargo_add(cargo, app)

    @app.route('/cargos/edit/<id>', methods=['PUT'])
    def cargos_edit(id):
        values = request.values
        cargo.descripcion = values.get('descripcion')
        return cargo.cargo_actualizar(id, cargo, app)

    @app.route('/cargos/delete/<id>', methods=['DELETE'])
    def cargos_delete(id):
        return cargo.cargo_eliminar(id, app)