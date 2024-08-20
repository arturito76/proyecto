from util.conexion import conexionbd

class ProductoDAO:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def buscar_producto(self, codproducto):
        cursor = self.conexion.cursor()
        sql = "SELECT cod_producto, fecha_produccion, nom_producto, cantidad_producto FROM producto WHERE cod_producto = '{}'".format(codproducto)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def actualizar_producto(self, cod_producto, nueva_cantidad):

        cursor = self.conexion.cursor()
        sql = "UPDATE producto SET cantidad_producto = '{}' WHERE cod_producto = '{}'".format(
        nueva_cantidad, cod_producto)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()






