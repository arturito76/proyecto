from util.conexion import conexionbd

class AlmacenStockBD:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def listar_almacen_stock(self):
        with self.conexion.cursor() as cursor:
            sql = """SELECT cod_almacen_stock, fecha_ingreso, cantidad_producto, nombre_producto, cod_empleado, cod_producto 
                     FROM almacen_stock"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def buscar_almacen_stock(self, codalmacenstock):
        with self.conexion.cursor() as cursor:
            sql = """SELECT fecha_ingreso, cantidad_producto, nombre_producto, cod_empleado, cod_producto
                     FROM almacen_stock WHERE cod_almacen_stock = %s"""
            cursor.execute(sql, (codalmacenstock,))
            result = cursor.fetchone()
            return result

    def insertar_almacen_stock(self, almacenstock):
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO almacen_stock (cod_almacen_stock, fecha_ingreso, cantidad_producto, nombre_producto, cod_empleado, cod_producto) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            valores = (almacenstock.cod_almacen_stock, 
                       almacenstock.fecha_ingreso,
                       almacenstock.cantidad_producto,
                       almacenstock.nombre_producto,
                       almacenstock.cod_empleado,
                       almacenstock.cod_producto)
            cursor.execute(sql, valores)
            self.conexion.commit()

    def actualizar_almacen_stock(self, almacenstock):
        with self.conexion.cursor() as cursor:
            sql = """UPDATE almacen_stock SET fecha_ingreso = %s, cantidad_producto = %s, nombre_producto = %s, cod_empleado = %s, cod_producto = %s
                     WHERE cod_almacen_stock = %s"""
            valores = (
                       almacenstock.fecha_ingreso,
                       almacenstock.cantidad_producto,
                       almacenstock.nombre_producto,
                       almacenstock.cod_empleado,
                       almacenstock.cod_producto,
                       almacenstock.cod_almacen_stock)
            cursor.execute(sql, valores)
            self.conexion.commit()

