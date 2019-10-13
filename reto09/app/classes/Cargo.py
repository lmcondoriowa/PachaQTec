from database.config import Conexion
from helper import helpers

class Cargo:
    def __init__(self, descripcion=None):
        self.descripcion = descripcion

    def cargo_add(self, cargo, app):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO cargo (descripcion)
                VALUES
                ('{cargo.descripcion}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agego el cargo : {cargo.descripcion}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def cargo_listar(self, app):
        listado_cargos = []
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM cargo
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_cargos.append({'descripcion' : fila[1]})

            message = 'Listado de Areas'
            print(message)
            return helpers.handler_response(app, 201, message, listado_cargos)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def cargo_actualizar(self, idcargo, cargo, app):  
        try:
            conn = Conexion()
            query = f'''
                UPDATE cargo
                SET descripcion='{cargo.descripcion}'
                WHERE id={idcargo};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el area : {cargo.descripcion} '''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  

    def cargo_eliminar(self, idcargo, app):  
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM cargo
                WHERE id={idcargo};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el cargo con código: {idarea}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  