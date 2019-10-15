from database.config import Conexion
from helper import helpers

class Employee:
    def __init__(self, nombre=None, apellido=None):
        self.nombre = nombre
        self.apellido = apellido

    def empleado_add(self, employee, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            db.table('empleado').insert({
                'nombre': employee.nombre,
                'apellido': employee.apellido
            })
            message = f'''Se agego el empleado : {employee.nombre} {employee.apellido}'''
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            return helpers.handler_response(app, 500, f'{str(e)}')

    def empleado_update(self, employee, employeeid, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            update= db.table('empleado') \
                .where('id', employeeid) \
                .update({
                    'nombre': employee.nombre,
                    'apellido': employee.apellido
                })
            message = f'''No se actualizo el  employeeid : {employeeid} '''
            if update > 0:
                message = f'''Se actualizaron : {update} '''
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            return helpers.handler_response(app, 500, f'{str(e)}')

    def empleado_listar(self, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            empleados = db.table('empleado').get()
            result = {}
            if empleados:
                result = empleados.serialize()

            return helpers.handler_response(app, 201, 'Lista', result)
        except Exception as e:
            return helpers.handler_response(app, 500, f'{str(e)}')

    def empleado_find(self, idempleado, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            empleados = db.table('empleado')\
                .where([
                    ['id', '=', idempleado]
                ]).first()
            result = {}
            if empleados:
                result = empleados.serialize()
            return helpers.handler_response(app, 201, 'Lista', result)
        except Exception as e:
            return helpers.handler_response(app, 500, f'{str(e)}')

    def empleado_actualizar(self, idempleado, empleado, app):  
        try:
            conn = Conexion()
            query = f'''
                UPDATE empleado
                SET nombre='{empleado.nombre}',
                apellido='{empleado.apellido}'
                WHERE id={idempleado};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el empleado : {empleado.nombre} {empleado.apellido}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  

    def empleado_delete(self, idempleado, app):
        try:
            conn = Conexion()
            db = conn.initialize()
            delete = db.table('empleado')\
                .where([
                    ['id', '=', idempleado]
                ]).delete()
            message = f'''No se elimino el  employeeid : {idempleado} '''
            if delete > 0:
                message = f'''Se actualizaron : {delete} '''
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            return helpers.handler_response(app, 500, f'{str(e)}')