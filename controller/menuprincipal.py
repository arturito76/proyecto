from PyQt5 import QtWidgets, uic





class menu_principal:
    def __init__(self):
        #self.app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/menu_principal.ui")

        self.ventana.produccion.clicked.connect(self.produccion)
        self.ventana.prima.clicked.connect(self.prima)
        self.ventana.stock.clicked.connect(self.stock)
        self.ventana.registros.clicked.connect(self.reporteonclicked)
        


        #self.ventana.show()
        #self.app.exec()
    
    def produccion(self):
        self.ventana.close()
        from controller.almacenproduccion import AlmacenProduccionController
        
        self.frmproduccion=AlmacenProduccionController()
        self.frmproduccion.ventana.show()

    def stock(self):
        self.ventana.close()
        from  controller.almacenstock import AlmacenStockController
        
        self.frmstock=AlmacenStockController()
        self.frmstock.ventana.show()

        
    def prima(self):
        self.ventana.close()
        from controller.almacenprima import almacenprimaController
        
        self.frmprima= almacenprimaController()
        self.frmprima.ventana.show()
    def reporteonclicked(self):
        self.ventana.close()
        from controller.reportecontroller import ControllerReporteMaterial
        self.frmreporte=ControllerReporteMaterial()
        self.frmreporte.ventana.show()
