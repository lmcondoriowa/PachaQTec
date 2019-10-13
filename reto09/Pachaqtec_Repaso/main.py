from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle


mi_producto = Producto('', '')
mi_factura = Factura('', '', '')
mi_factura_detalle = FacturaDetalle('', '', '')

while True:
    empezar = str(input('¿Vas añadir una factura? (S/N) : '))
    if empezar == 'S':
        nro_factura = str(input('Cod de la factura : '))
        print('Ahora elige los productos a agregar')
        print('##### Listado de Productos #####')
        for producto in mi_producto.listar_productos():
            print(f'id: {producto[0]} | nombre: {producto[1]} | precio: {producto[2]}')

        productos = []
        cantidadList = []

        while True:
            producto_id = int(input('Agrega el id del producto : '))
            cantidad = int(input('Agrega la cantidad del producto : '))
            productos.append(producto_id)
            cantidadList.append(cantidad)
            if str(input('¿Agregaras más productos? (S/N) : ')) == 'N':
                break

        mi_factura.nro_factura = nro_factura
        costosList = []
        for index, producto in enumerate(productos):
            get_producto = mi_producto.listar_producto(producto)
            costosList.append(get_producto[2] * cantidadList[index])

        mi_factura.sub_total = sum(costosList)
        igv = round(mi_factura.sub_total * 0.18, 2)
        mi_factura.total = round(mi_factura.sub_total + igv, 2)

        last_row = mi_factura.agregar_factura(mi_factura)

        for index, producto in enumerate(productos):
            mi_factura_detalle.factura_id = last_row
            mi_factura_detalle.producto_id = producto
            mi_factura_detalle.cantidad = cantidadList[index]
            mi_factura_detalle.agregar_factura_detalle(mi_factura_detalle)

        print('Terminado')
        break
    else:
        print('Finalizado')
        break