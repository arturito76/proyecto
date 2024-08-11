class materiales:
    def __init__(self, cod_material, nombre, unidad_medida, cantidad_disponible, cod_empleado, precio_unitario):
        self.__cod_material = cod_material
        self.__nombre = nombre
        self.__unidad_medida = unidad_medida
        self.__cantidad_disponible = cantidad_disponible
        self.__cod_empleado = cod_empleado
        self.__precio_unitario = precio_unitario
    

    def get_cod_material(self):
        return self.__cod_material
    
    def get_nombre(self):
        return self.__nombre
    
    def get_unidad_medida(self):
        return self.__unidad_medida
    
    def get_cantidad_disponible(self):
        return self.__cantidad_disponible
    
    def get_cod_empleado(self):
        return self.__cod_empleado
    
    def get_precio_unitario(self):
        return self.__precio_unitario
    


    def set_cod_material(self, cod_material):
        self.__cod_material = cod_material

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_unidad_medida(self, unidad_medida):
        self.__unidad_medida = unidad_medida

    def set_cantidad_disponible(self, cantidad_disponible):
        self.__cantidad_disponible = cantidad_disponible

    def set_cod_empleado(self, cod_empleado):
        self.__cod_empleado = cod_empleado

    def set_precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario
        