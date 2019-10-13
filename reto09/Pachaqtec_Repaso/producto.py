from conn.conection import Conexion

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def agregar_producto(self, producto):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO producto (nombre, precio) 
                VALUES 
                ('{producto.nombre}', {producto.precio})
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            print(f'Se agrego el producto : {producto.nombre}')
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def listar_producto(self, producto_id):
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM producto WHERE id = {producto_id}
            '''
            cursor = conn.ejecutar_sentencia(query)
            return cursor.fetchone()
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

    def listar_productos(self):
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM producto
            '''
            cursor = conn.ejecutar_sentencia(query)
            return cursor.fetchall()
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()