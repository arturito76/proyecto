from PyQt5 import QtWidgets, uic
from controller.almacenproduccion import AlmacenProduccionController
from controller.almacenprima import almacenprimaController
from  controller.almacenstock import AlmacenStockController


class menu_principal:
    def __init__(self):
        #self.app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/menu_principal.ui")

        self.ventana.produccion.clicked.connect(self.produccion)
        self.ventana.prima.clicked.connect(self.prima)
        self.ventana.stock.clicked.connect(self.stock)
        


        #self.ventana.show()
        #self.app.exec()

    def produccion(self):
        self.ventana.close()
        self.frmproduccion=AlmacenProduccionController()
        self.frmproduccion.ventana.show()

    def stock(self):
        self.ventana.close()
        self.frmstock=AlmacenStockController()
        self.frmstock.ventana.show()

        
    def prima(self):
        self.ventana.close()
        self.frmprima= almacenprimaController()
        self.frmprima.ventana.show()
    def registros(self):
        self.ventana.close()
        self.frmproduccion=AlmacenProduccionController()
        self.frmproduccion.ventana.show()
