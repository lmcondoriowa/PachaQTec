from flask import request
from app.classes.Grupo import Grupo

grupo = Grupo()

def route_grupo(app):
    @app.route('/grupos')
    def grupos_listar():
        return grupo.grupo_listar(app)

    @app.route('/grupos/add', methods=['POST'])
    def grupo_add():
        values = request.values
        grupo.idempleado = values.get('idempleado')
        grupo.idarea = values.get('idarea')
        grupo.idcargo = values.get('idcargo')
        grupo.idrol = values.get('idrol')
        return grupo.grupo_add(grupo, app)

    @app.route('/grupos/edit/<id>', methods=['PUT'])
    def grupo_edit(id):
        values = request.values
        grupo.idarea = values.get('idarea')
        grupo.idcargo = values.get('idcargo')
        grupo.idrol = values.get('idrol')
        return grupo.grupo_actualizar(id, grupo, app)

    @app.route('/grupos/delete/<id>', methods=['DELETE'])
    def grupos_delete(id):
        return grupo.grupo_eliminar(id, app)