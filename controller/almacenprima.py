from PyQt5 import QtWidgets, uic
from dao.materialdao import almacenprimabd
from model.Almacenprima import AlmacenPrimamode
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from datetime import datetime

class almacenprimaController:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.objalmacenprimadao = almacenprimabd()
        self.ventana = uic.loadUi("view/almacenprima.ui")

        
        self.ventana.tableprima.setColumnWidth(0, 50)
        self.ventana.tableprima.setColumnWidth(1, 250)
        self.ventana.tableprima.setColumnWidth(2, 120)
        self.ventana.tableprima.setColumnWidth(3, 100)
        self.ventana.tableprima.setColumnWidth(4, 100)

       
        self.ventana.registrar.clicked.connect(self.registraronclicked)
        self.ventana.cancelar.clicked.connect(self.cancelaronclicked)
        self.ventana.tableprima.cellClicked.connect(self.tableprimacellClick)

        self.ventana.show()
        self.listar_almacen_prima()
        app.exec()

    def tableprimacellClick(self, fila):
        try:
            codprima = self.ventana.tableprima.item(fila, 0).text()
            self.ventana.codprima.setText(codprima)
            self.ventana.codprima.setEnabled(False)
            objprima = self.objalmacenprimadao.buscar_almacen_prima(codprima)
            
            
            fecha_ingreso = objprima[1]
            if isinstance(fecha_ingreso, datetime):
                fecha_ingreso_str = fecha_ingreso.strftime('%d-%m-%Y')  
            else:
                fecha_ingreso_str = str(fecha_ingreso)  

            self.ventana.feingreso.setText(fecha_ingreso_str)
            self.ventana.codmaterial.setText(str(objprima[2]))
            self.ventana.canprod.setText(str(objprima[3]))
            self.ventana.codemple.setText(str(objprima[4]))
        except Exception as e:
            
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def cancelaronclicked(self):
        try:
            self.ventana.codprima.setText("")
            self.ventana.codprima.setEnabled(True)
            self.ventana.feingreso.setText("")
            self.ventana.codmaterial.setText("")
            self.ventana.canprod.setText("")
            self.ventana.codemple.setText("")
        except Exception as e:
            
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def registraronclicked(self):
        try:
            cod_almacen_prima = self.ventana.codprima.text()
            fecha_ingreso = self.ventana.feingreso.text()
            cod_material = self.ventana.codmaterial.text()
            cantidad_producto = self.ventana.canprod.text()
            cod_empleado = self.ventana.codemple.text()

            
            nuevoprima = AlmacenPrimamode(cod_almacen_prima, fecha_ingreso, cod_material, cantidad_producto, cod_empleado)

            if self.ventana.codprima.isEnabled():
                self.objalmacenprimadao.insertar_material(nuevoprima)
                QtWidgets.QMessageBox.information(self.ventana, "Éxito", "Registro de material insertado correctamente.")
            

            self.listar_almacen_prima()
        except Exception as e:
            
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def listar_almacen_prima(self):
        try:
            listalmacen = self.objalmacenprimadao.listar_almacen_prima()
            cantidad = len(listalmacen)

           
            self.ventana.tableprima.setRowCount(cantidad)

            fila = 0
            for almacen in listalmacen:
                self.ventana.tableprima.setItem(fila, 0, QTableWidgetItem(almacen[0]))
                self.ventana.tableprima.setItem(fila, 1, QTableWidgetItem(str(almacen[1])))
                self.ventana.tableprima.setItem(fila, 2, QTableWidgetItem(almacen[2]))
                self.ventana.tableprima.setItem(fila, 3, QTableWidgetItem(str(almacen[3])))
                self.ventana.tableprima.setItem(fila, 4, QTableWidgetItem(almacen[4]))
                fila += 1
        except Exception as e:
            
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

