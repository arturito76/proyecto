from util.conexion import conexionbd

class EmpleadoDAO:
    def __init__(self):
        self.conexion = conexionbd().getconexionbd()

    def validar_login(self, dni, cod_empleado):
        try:
            with self.conexion.cursor() as cursor:
                sql = "SELECT * FROM empleado WHERE dni = '{}' AND cod_empleado = '{}'".format(dni, cod_empleado)
                cursor.execute(sql)
                result = cursor.fetchone()
                return result is not None
        except Exception as e:
            print(f"Error al validar login: {e}")
            return False

