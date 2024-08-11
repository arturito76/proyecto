class Pedido:
    def __init__(self, id_pedido, fecha_pedido, cantidad, fecha_entrega, nombre_producto):
        self.__id_pedido = id_pedido
        self.__fecha_pedido = fecha_pedido
        self.__cantidad = cantidad
        self.__fecha_entrega = fecha_entrega
        self.__nombre_producto = nombre_producto

    # Métodos get
    def get_id_pedido(self):
        return self.__id_pedido

    def get_fecha_pedido(self):
        return self.__fecha_pedido

    def get_cantidad(self):
        return self.__cantidad

    def get_fecha_entrega(self):
        return self.__fecha_entrega
    
    def get_nombre_producto(self):
        return self.__nombre_producto
    

    # Métodos set
    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_fecha_pedido(self, fecha_pedido):
        self.__fecha_pedido = fecha_pedido

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

    def set_nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto