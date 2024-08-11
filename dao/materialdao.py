from util.conexion import conexionbd

class almacenprimabd:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def listar_almacen_prima(self):
        cursor = self.conexion.cursor()
        sql = "SELECT cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado FROM almacen_prima"
        cursor.execute(sql)
        return cursor.fetchall()

    def buscar_almacen_prima(self, codprima):
        cursor = self.conexion.cursor()
        sql = """SELECT cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado
                 FROM almacen_prima WHERE cod_almacen_prima = %s"""
        cursor.execute(sql, (codprima,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insertar_material(self, almacenprima):
        cursor = self.conexion.cursor()
        sql = """INSERT INTO almacen_prima (cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (almacenprima.cod_almacen_prima, almacenprima.fecha_ingreso,
                   almacenprima.cod_material, almacenprima.cantidad_producto,
                   almacenprima.cod_empleado)
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()

    def actualizar_almacen_prima(self, almacenprima):
        cursor = self.conexion.cursor()
        sql = """UPDATE almacen_prima SET fecha_ingreso = %s, cod_material = %s, cantidad_producto = %s, cod_empleado = %s
                 WHERE cod_almacen_prima = %s"""
        valores = (almacenprima.fecha_ingreso, almacenprima.cod_material,
                   almacenprima.cantidad_producto, almacenprima.cod_empleado,
                   almacenprima.cod_almacen_prima)
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()