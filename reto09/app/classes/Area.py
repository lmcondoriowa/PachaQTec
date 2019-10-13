from database.config import Conexion
from helper import helpers

class Area:
    def __init__(self, descripcion=None):
        self.descripcion = descripcion

    def area_add(self, area, app):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO area (descripcion)
                VALUES
                ('{area.descripcion}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agego el area : {area.descripcion}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def area_listar(self, app):
        listado_areas = []
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM area
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_areas.append({'descripcion' : fila[1]})

            message = 'Listado de Areas'
            print(message)
            return helpers.handler_response(app, 201, message, listado_areas)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def area_actualizar(self, idarea, area, app):  
        try:
            conn = Conexion()
            query = f'''
                UPDATE area
                SET descripcion='{area.descripcion}'
                WHERE id={idarea};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el area : {area.descripcion} '''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  

    def area_eliminar(self, idarea, app):  
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM area
                WHERE id={idarea};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el area con código: {idarea}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  