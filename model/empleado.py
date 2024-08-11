class Empleado:
    def __init__(self, cod_empleado, nombres, apellidos,dni,telefono,direccion,salario, fecha_nacimiento,):
        self.__cod_empleado = cod_empleado
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__telefono=telefono
        self.__direccion=direccion
        self.__salario=salario
        self.__fecha_nacimiento=fecha_nacimiento

    # Métodos get
    def get_cod_empleado(self):
        return self.__cod_empleado

    def get_nombres(self):
        return self.__nombres

    def get_apellidos(self):
        return self.__apellidos

    def get_dni(self):
        return self.__dni

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion
    
    def get_salario(self): 
        return self.__salario
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento



    # Métodos set
    def set_cod_empleado(self, cod_empleado):
        self.__cod_empleado = cod_empleado

    def set_nombres(self, nombres):
        self.__nombres = nombres

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_dni(self, dni):
        self.__dni = dni

    def set_telefono(self):
        self.__telefono=telefono

    def set_direccion(self):
        self.__direccion=direccion

    def set_salario(self):
        self.__salario=salario
    
    def set_fecha_nacimiento(self):
        self.__fecha_nacimiento=fecha_nacimiento