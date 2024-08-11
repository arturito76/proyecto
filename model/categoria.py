class Categoria:
    def __init__(self, codproducto, tamaño, color, fecha_entrega, nombre):
        self.__codproducto = codproducto
        self.__tamaño = tamaño
        self.__color = color
        self.__fecha_entrega = fecha_entrega
        self.__nombre = nombre

    def get_codproducto(self):
        return self.__codproducto
    
    def get_tamaño(self):
        return self.__tamaño
    
    def get_color(self):
        return self.__color
    
    def get_fecha_entrega(self):
        return self.__fecha_entrega
    
    def get_nombre(self):
        return self.__nombre
    

    def set_codproducto(self, codproducto):
        self.__codproducto = codproducto

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def set_color(self, color):
        self.__color = color

    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    
    

