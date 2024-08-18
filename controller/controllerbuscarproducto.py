from PyQt5 import QtWidgets, uic
from dao.buscarproducto import ProductoDAO
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime

class productoController:
    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.objproductodao = ProductoDAO()
        self.ventana = uic.loadUi("view/buscarproducto.ui")

       

        # Configuración inicial de la tabla
        
        self.ventana.resultadoproducto.setColumnWidth(0, 150)
        self.ventana.resultadoproducto.setColumnWidth(1, 200)
        self.ventana.resultadoproducto.setColumnWidth(2, 200)
        self.ventana.resultadoproducto.setColumnWidth(3, 100)

        # Conectar señales a los métodos
        self.ventana.buscarproducto.clicked.connect(self.buscarproducto)
        self.ventana.regresarproducto.clicked.connect(self.regresarproductoonclicked)

        # Mostrar la ventana
        #self.ventana.show()
        #app.exec()
    def regresarproductoonclicked(self):
        self.ventana.close()
        from controller.almacenstock import AlmacenStockController
        
        self.frmalmacenstock= AlmacenStockController()
        self.frmalmacenstock.ventana.show()


    def buscarproducto(self):
        try:
            cod_producto = self.ventana.codproducto.text()
            objproducto = self.objproductodao.buscar_producto(cod_producto)

            # Limpiar tabla antes de mostrar resultados
            self.ventana.resultadoproducto.setRowCount(0)

            if objproducto:
                fecha_ingreso = objproducto[1]
                if isinstance(fecha_ingreso, datetime):
                    fecha_ingreso_str = fecha_ingreso.strftime('%d-%m-%Y')
                else:
                    fecha_ingreso_str = str(fecha_ingreso)

                # Agregar fila a la tabla
                row_position = self.ventana.resultadoproducto.rowCount()
                self.ventana.resultadoproducto.insertRow(row_position)
                self.ventana.resultadoproducto.setItem(row_position, 0, QTableWidgetItem(objproducto[0]))
                self.ventana.resultadoproducto.setItem(row_position, 1, QTableWidgetItem(fecha_ingreso_str))
                self.ventana.resultadoproducto.setItem(row_position, 2, QTableWidgetItem(objproducto[2]))
                self.ventana.resultadoproducto.setItem(row_position, 3, QTableWidgetItem(str(objproducto[3])))
            else:
                QtWidgets.QMessageBox.warning(self.ventana, "Advertencia", "El producto no se encontró.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")



    
