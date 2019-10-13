import pymysql


class Conexion:
    def __init__(self, server="localhost", usuario="root", clave="", base_datos="facturacion"):
        self.db = pymysql.connect(server, usuario, clave, base_datos)
        self.cursor = self.db.cursor()

    def ejecutar_sentencia(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def cerrar_conexion(self):
        self.db.close()

    def commit(self):
        self.db.commit()
        return

    def rollback(self):
        self.db.rollback()
        return
