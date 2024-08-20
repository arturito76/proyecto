from util.conexion import conexionbd

class AlmacenPrimaBD:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def listar_almacen_prima(self):
        cursor = self.conexion.cursor()
        sql = """SELECT cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado 
                 FROM almacen_prima ORDER BY cod_almacen_prima DESC"""
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def buscar_almacen_prima(self, codprima):
        cursor = self.conexion.cursor()
        sql = """SELECT cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado
                 FROM almacen_prima WHERE cod_almacen_prima = '{}'""".format(codprima)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def insertar_material(self, almacenprima):
        cursor = self.conexion.cursor()

        # Insertar en almacen_prima
        sql_insertar_almacen_prima = """INSERT INTO almacen_prima (cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado) 
                                        VALUES ('{}', '{}', '{}', '{}', '{}')""".format(
                                            almacenprima.cod_almacen_prima,
                                            almacenprima.fecha_ingreso,
                                            almacenprima.cod_material,
                                            almacenprima.cantidad_producto,
                                            almacenprima.cod_empleado
                                        )
        cursor.execute(sql_insertar_almacen_prima)

            # Actualizar la cantidad disponible en la tabla materiales
       
    # Verifica la cantidad actual
        sql_actualizar_materiales = """UPDATE materiales 
                                       SET cantidad_disponible = cantidad_disponible + {} 
                                       WHERE cod_material = '{}'""".format(
                                           almacenprima.cantidad_producto, 
                                           almacenprima.cod_material
                                       )
        cursor.execute(sql_actualizar_materiales)

        self.conexion.commit()
        cursor.close()


