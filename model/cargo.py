from model.empleado import Empleado

class Cargo(Empleado):
    def __init__(self, cod_empleado, nombres, apellidos, dni, telefono, direccion, salario, fecha_nacimiento, cod_cargo, nombre_cargo):
        super().__init__(cod_empleado, nombres, apellidos, dni, telefono, direccion, salario, fecha_nacimiento)
        self.__cod_cargo = cod_cargo
        self.__nombre_cargo = nombre_cargo

    def get_cod_cargo(self):
        return self.__cod_cargo
    
    def get_nombre_cargo(self):
        return self.__nombre_cargo
    
    def set_cod_cargo(self, cod_cargo):
        self.__cod_cargo = cod_cargo

    def set_nombre_cargo(self, nombre_cargo):
        self.__nombre_cargo = nombre_cargo

        