from flask import request
from app.classes.Employee import Employee

employee = Employee()

def route_employee(app):
    @app.route('/')
    def hello_world():
        return 'Bienvenidos al Empresa'

    @app.route('/empleados')
    def empleados_listar():
        return employee.empleado_listar(app)

    @app.route('/empleados/add', methods=['POST'])
    def empleados_add():
        values = request.values
        employee.nombre = values.get('nombre')
        employee.apellido = values.get('apellido')
        return employee.empleado_add(employee, app)

    @app.route('/empleados/edit/<id>', methods=['PUT'])
    def empleados_edit(id):
        values = request.values
        employee.nombre = values.get('nombre')
        employee.apellido = values.get('apellido')
        return employee.empleado_actualizar(id, employee, app)

    @app.route('/empleados/delete/<id>', methods=['DELETE'])
    def empleados_delete(id):
        return employee.empleado_eliminar(id, app)