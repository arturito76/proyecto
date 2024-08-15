from util.conexion import conexionbd

class ProductoDAO:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def buscar_producto(self, codproducto):
        cursor = self.conexion.cursor()
        sql ="SELECT cod_producto, fecha_produccion, nom_producto, cantidad_producto FROM producto WHERE cod_producto = '{}'".format(codproducto)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result


