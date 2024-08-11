class Producto:
    def __init__(self, cod_producto, nom_producto, fecha_produccion, cantidad_producto,cod_produccion):
        self.__cod_producto = cod_producto
        self.__nom_producto = nom_producto
        self.__fecha_produccion = fecha_produccion
        self.__cantidad_producto = cantidad_producto
        self.__cod_produccion=cod_produccion

    # Métodos get
    def get_cod_producto(self):
        return self.__cod_producto

    def get_nom_producto(self):
        return self.__nom_producto

    def get_fecha_produccion(self):
        return self.__fecha_produccion

    def get_cantidad_producto(self):
        return self.__cantidad_producto
    
    def get_cod_produccion(self):
        return self.__cod_produccion


        

    def set_cod_producto(self):
        self.__cod_producto = cod_producto

    def set_nom_producto(self):
        self.__nom_producto = nom_producto

    def set_fecha_produccion(self):
        self.__fecha_produccion = fecha_produccion

    def set_cantidad_producto(self):
        self.__cantidad_producto = cantidad_producto
    def set_cod_produccion(self):
        self.__cod_produccion=cod_produccion