from PyQt5 import QtWidgets, uic
from dao.empleadodao import EmpleadoDAO
from controller.menuprincipal import menu_principal

class LoginController:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.ventana_login = uic.loadUi("view/login_menu_principal.ui")
        

        self.empleado_dao = EmpleadoDAO()

        
        self.ventana_login.iniciarsesion.clicked.connect(self.iniciar)

        
        self.ventana_login.show()
        self.app.exec()

    def iniciar(self):
        dni = self.ventana_login.dni.text()
        cod_empleado = self.ventana_login.id_empleado.text()

        if self.validar_login(dni, cod_empleado):
            self.ventana_login.close()
            
        else:
            self.ventana_login.respuesta_login.setText("DNI o código de empleado incorrectos.")
        self.frmmenuprincipal=menu_principal()
        self.frmmenuprincipal.ventana.show()
    
    def validar_login(self, dni, cod_empleado):
        return self.empleado_dao.validar_login(dni, cod_empleado)

    



