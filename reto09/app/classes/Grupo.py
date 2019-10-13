from database.config import Conexion
from helper import helpers

class Grupo:
    def __init__(self, idempleado=None, idarea=None, idcargo=None, idrol=None):
        self.idempleado = idempleado
        self.idarea = idarea
        self.idcargo = idcargo
        self.idrol = idrol

    def grupo_add(self, grupo, app):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO grupo (idempleado, idarea, idcargo, idrol)
                VALUES
                ({grupo.idempleado}, {grupo.idarea}, {grupo.idcargo}, {grupo.idrol})
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agego el grupo : {grupo.idempleado} {grupo.idarea} {grupo.idcargo} {grupo.idrol}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def grupo_listar(self, app):
        listado_grupos = []
        try:
            conn = Conexion()
            query = f'''
                SELECT empleado.nombre, empleado.apellido,
                    area.descripcion, cargo.descripcion, rol.descripcion
                FROM grupo
                INNER JOIN empleado
                ON (grupo.idempleado = empleado.id)
                INNER JOIN area
                ON (grupo.idarea = area.id)
                INNER JOIN cargo
                ON (grupo.idcargo = cargo.id)
                INNER JOIN rol
                ON (grupo.idrol = rol.id)
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_grupos.append({'nombre' : fila[0], 'apellido': fila[1], 'area': fila[2], 'cargo': fila[3], 'rol': fila[4]})

            message = 'Listado de Agrupacion'
            print(message)
            return helpers.handler_response(app, 201, message, listado_grupos)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def grupo_actualizar(self, idgrupo, grupo, app):  
        try:
            conn = Conexion()
            query = f'''
                UPDATE grupo
                SET 
                idarea='{grupo.idarea}',
                idcargo='{grupo.idcargo}',
                idrol='{grupo.idrol}',
                WHERE id={idgrupo};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se actualizó el grupo con los siguientes datos : {grupo.idempleado} {grupo.idarea} {grupo.idcargo} {grupo.idrol}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            conn.rollback()
            return helpers.handler_response(app, 500, e)
        finally:
            conn.cerrar_conexion()  

    def grupo_eliminar(self, idgrupo, app):  
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM grupo
                WHERE id={idgrupo};
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se eliminó el grupo con código: {idgrupo}'''
            print(message)
            return helpers.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()  