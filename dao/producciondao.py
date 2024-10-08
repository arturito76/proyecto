from util.conexion import conexionbd

class AlmacenProduccionBD:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def listar_almacen_produccion(self):
        try:
            with self.conexion.cursor() as cursor:
                sql = """SELECT cod_produccion, fecha_produccion, cantidad_produccion, cod_empleado, cod_material, cod_producto, cantidad_material
                         FROM produccion ORDER BY cod_produccion DESC"""
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return resultados
        except Exception as e:
            print(f"Error al listar producción: {e}")
            return []

    def buscar_almacen_produccion(self, codproducc):
        try:
            with self.conexion.cursor() as cursor:
                sql = """SELECT fecha_produccion, cantidad_produccion, cod_empleado, cod_material, cod_producto, cantidad_material
                         FROM produccion WHERE cod_produccion = '{}'""".format(codproducc)
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(f"Error al buscar producción: {e}")
            return None

    def insertar_produccion(self, almacenproduccion):
        try:
            with self.conexion.cursor() as cursor:
                # Verificar cantidad disponible
                sql_verificar = """SELECT cantidad_disponible FROM materiales WHERE cod_material = '{}'""".format(almacenproduccion.cod_material)
                cursor.execute(sql_verificar)
                resultado = cursor.fetchone()
                
                if resultado:
                    cantidad_disponible = resultado[0]
                    if cantidad_disponible < almacenproduccion.cantidad_material:
                        raise ValueError("Cantidad de material insuficiente para la producción.")
                
                # Insertar registro en la tabla de producción
                sql_insertar = """INSERT INTO produccion (cod_produccion, fecha_produccion, cantidad_produccion, cod_empleado, cod_material, cod_producto, cantidad_material) 
                                  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                                    almacenproduccion.cod_produccion, 
                                    almacenproduccion.fecha_produccion,
                                    almacenproduccion.cantidad_produccion,
                                    almacenproduccion.cod_empleado,
                                    almacenproduccion.cod_material,
                                    almacenproduccion.cod_producto,
                                    almacenproduccion.cantidad_material
                                )
                cursor.execute(sql_insertar)

                # Reducir la cantidad en la tabla de materiales
                sql_update = """UPDATE materiales 
                                SET cantidad_disponible = cantidad_disponible - {} 
                                WHERE cod_material = '{}'""".format(
                                    almacenproduccion.cantidad_material, 
                                    almacenproduccion.cod_material
                                )
                cursor.execute(sql_update)

                self.conexion.commit()
        except ValueError as ve:
            print(f"Error: {ve}")
            self.conexion.rollback()
            raise ve
        except Exception as e:
            print(f"Error al insertar producción: {e}")
            self.conexion.rollback()

   
