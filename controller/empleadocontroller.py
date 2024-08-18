from PyQt5 import QtWidgets, uic
from dao.empleadodao import EmpleadoDAO
from controller.menuprincipal import menu_principal#importamos el modulo de menu principal al momento de haber validado los datos

class LoginController:
    def __init__(self):
        self.app = QtWidgets.QApplication([])#crea una instancia desde la aplicacion qt
        self.ventana_login = uic.loadUi("view/login_menu_principal.ui")#indicamos el formulario que se va a mostrar 
        self.empleado_dao = EmpleadoDAO()#crea una instancia con el dao donde manejaremos los datos de la base de dstos
        #configuramos el botonn de iniciar sesion 
        self.ventana_login.iniciarsesion.clicked.connect(self.iniciar)

        
        self.ventana_login.show()#se inicia la aplicacion
        self.app.exec()#se inicia el bucle de eventos dentro de la aplicacion

    def iniciar(self):#la funcion del boton iniciar sesion
        dni = self.ventana_login.dni.text()#asignamos que el dni es de text en tdesigner
        cod_empleado = self.ventana_login.id_empleado.text()#lo mismo aca en id_empleado

        if self.validar_login(dni, cod_empleado):#creamos una condicion si los datos son correctos o no!
            self.ventana_login.close()#en caso se cumpla la ventana actual se cierra
            self.frmmenuprincipal=menu_principal()#crea la instancia con la clase menu principal
            self.frmmenuprincipal.ventana.show()#luego abre la de menu principal y carga el formulario
            
        else:
            self.ventana_login.respuesta_login.setText("DNI o código de empleado incorrectos.")# al no ser validos mostrara un sms de error
        
    
    def validar_login(self, dni, cod_empleado):
        return self.empleado_dao.validar_login(dni, cod_empleado)

    



