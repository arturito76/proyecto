from PyQt5 import QtWidgets, uic
from dao.empleadodao import EmpleadoDAO
from model.empleado import Empleado
from controller.almacenproduccion import AlmacenProduccionController

class LoginController:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.ventana_login = uic.loadUi("view/login_menu_principal.ui")
        self.ventana_produccion = None  # Placeholder for production window

        # Instancia del DAO
        self.empleado_dao = EmpleadoDAO()

        # Conexión de eventos
        self.ventana_login.iniciarsesion.clicked.connect(self.handle_login)

        # Mostrar ventana de login
        self.ventana_login.show()
        self.app.exec()

    def handle_login(self):
        dni = self.ventana_login.dni.text()
        cod_empleado = self.ventana_login.id_empleado.text()

        if self.validar_login(dni, cod_empleado):
            self.ventana_login.close()
            self.mostrar_ventana_produccion()
        else:
            self.ventana_login.respuesta_login.setText("DNI o código de empleado incorrectos.")

    def validar_login(self, dni, cod_empleado):
        return self.empleado_dao.validar_login(dni, cod_empleado)

    def mostrar_ventana_produccion(self):
        # Cargar y mostrar la ventana de producción
        if self.ventana_produccion is None:
            self.ventana_produccion = uic.loadUi("view/produccionregistrar.ui")
        
        self.ventana_produccion.show()




