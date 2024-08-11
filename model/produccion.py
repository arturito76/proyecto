from model.producto import Producto

class Produccionmodel:
    def __init__(self, cod_produccion,fecha_produccion, cantidad_produccion,cod_empleado,cod_material,cod_producto ):
        self.cod_produccion = cod_produccion
        self.fecha_produccion=fecha_produccion
        self.cantidad_produccion=cantidad_produccion
        self.cod_empleado = cod_empleado
        self.cod_material=cod_material
        self.cod_producto=cod_producto
