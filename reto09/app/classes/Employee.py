from database.config import Conexion
from helper import helpers

class Employee:
    def __init__(self, nombre=None, apellido=None):
        self.nombre = nombre
        self.apellido = apellido

    def empleado_add(self, employee, app):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO empleado (nombre, apellido)
                VALUES
                ('{employee.nombre}', '{employee.apellido}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agego el empleado : {employee.nombre} {employee.apellido}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def empleado_listar(self, app):
        listado_empleados = []
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM empleado
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_empleados.append({'nombre' : fila[1], 'apellido': fila[2]})

            message = 'Listado de Empleados'
            print(message)
            return helpers.handler_response(app, 201, message, listado_empleados)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

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

    def empleado_eliminar(self, idempleado, app):  
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM empleado
                WHERE id={idempleado};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el empleado con código: {idempleado}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  