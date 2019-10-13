from conn.conection import Conexion


class FacturaDetalle:
    def __init__(self, factura_id, producto_id, cantidad):
        self.factura_id = factura_id
        self.producto_id = producto_id
        self.cantidad = cantidad

    def agregar_factura_detalle(self, factura_detalle):
        try:
            conn = Conexion()
            query = f'''
                INSERT INTO factura_detalle (factura_id, producto_id, cantidad)
                VALUES 
                ({factura_detalle.factura_id}, {factura_detalle.producto_id}, {factura_detalle.cantidad})
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            print(f'Se agrego el detalle de la factura : {factura_detalle.factura_id}')
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()