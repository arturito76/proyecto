# archivo: dao/reporte_material_dao.py
from util.conexion import conexionbd

class ReporteMaterialDAO:
    def __init__(self):
        self.conexionbd = conexionbd().getconexionbd()

    def generar_reporte(self, codigo_material):
        cursor = self.conexionbd.cursor()
        sql = """
            SELECT 
                m.Cod_material,
                m.nombre,
                m.unidad_medida,
                ROUND(SUM(m.cantidad_disponible)) AS cantidad_producto,
                m.precio_unitario,
                ROUND(SUM(m.cantidad_disponible * m.precio_unitario)) AS precio_total,
                COUNT(m.Cod_material) AS cantidad_registros
            FROM 
                materiales m
            JOIN 
                almacen_prima ap ON m.Cod_material = ap.Cod_material
            WHERE
                m.Cod_material = %s
            GROUP BY 
                m.Cod_material, m.nombre, m.unidad_medida, m.precio_unitario
        """
        cursor.execute(sql, (codigo_material,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
