from conn.conection import Conexion


class Factura:
    def __init__(self, nro_factura, sub_total, total):
        self.nro_factura = nro_factura
        self.sub_total = sub_total
        self.total = total

    def agregar_factura(self, factura):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO factura (nro_factura, sub_total, total) 
                VALUES 
                ('{factura.nro_factura}', {factura.sub_total}, {factura.total})
            '''
            cursor = conn.ejecutar_sentencia(query)
            factura_id = cursor.lastrowid
            conn.commit()
            return factura_id
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()