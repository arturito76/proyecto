class Empleado:
    def __init__(self, cod_empleado, nombres, apellidos,dni,telefono,direccion,salario, fecha_nacimiento,):
        self._cod_empleado = cod_empleado
        self._nombres = nombres
        self._apellidos = apellidos
        self._dni = dni
        self._direccion=direccion
        self._salario=salario
        self._fecha_nacimiento=fecha_nacimiento
        self.cod_cargo=cod_cargo
