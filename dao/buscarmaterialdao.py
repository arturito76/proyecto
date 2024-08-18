from util.conexion import conexionbd

class buscarmaterialdao:
    def __init__(self):
        self.conexionbd= conexionbd().getconexionbd()

    def buscar_material(self,codmaterial):
        cursor= self.conexionbd.cursor()
        sql= "SELECT  cod_material, nombre, unidad_medida, cantidad_disponible, cod_empleado, precio_unitario FROM materiales WHERE cod_material = '{}'".format(codmaterial)
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    



        