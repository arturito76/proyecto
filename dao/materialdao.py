from util.conexion import conexionbd

class almacenprimabd:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def listar_almacen_prima(self):
        cursor = self.conexion.cursor()
        sql = "SELECT cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado FROM almacen_prima ORDER BY cod_almacen_prima DESC"
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
        
        # Insertar en almacen_prima
        sql_insertar_almacen_prima = """INSERT INTO almacen_prima (cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado) 
                                        VALUES (%s, %s, %s, %s, %s)"""
        valores_almacen_prima = (almacenprima.cod_almacen_prima, almacenprima.fecha_ingreso,
                                 almacenprima.cod_material, almacenprima.cantidad_producto,
                                 almacenprima.cod_empleado)
        cursor.execute(sql_insertar_almacen_prima, valores_almacen_prima)

        # Actualizar la cantidad disponible en la tabla materiales va a interactuar con la tabla de materiales :)
        sql_actualizar_materiales = """UPDATE materiales 
                                       SET cantidad_disponible = cantidad_disponible + %s 
                                       WHERE cod_material = %s"""
        valores_materiales = (almacenprima.cantidad_producto, almacenprima.cod_material)
        cursor.execute(sql_actualizar_materiales, valores_materiales)

        self.conexion.commit()
        cursor.close()

