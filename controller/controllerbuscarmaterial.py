from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from dao.buscarmaterialdao import buscarmaterialdao

class controllerbuscarmaterial:
    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.objbuscarmaterial = buscarmaterialdao()
        self.ventana = uic.loadUi("view/BUSCARMATERIAL.ui")

        # Configuración de las columnas de la tabla
        self.ventana.resultadomaterial.setColumnWidth(0, 200)
        self.ventana.resultadomaterial.setColumnWidth(1, 200)
        self.ventana.resultadomaterial.setColumnWidth(2, 200)
        self.ventana.resultadomaterial.setColumnWidth(3, 200)
        self.ventana.resultadomaterial.setColumnWidth(4, 200)
        self.ventana.resultadomaterial.setColumnWidth(5, 200)

        # Conectar el botón de búsqueda a la función correspondiente
        self.ventana.buscarmaterial.clicked.connect(self.buscarmaterialonclicked)
        self.ventana.regresar.clicked.connect(self.regresaronclicked)

        #self.ventana.show()
        #app.exec()

    def regresaronclicked(self):
        self.ventana.close()
        from controller.almacenprima import almacenprimaController
        self.frmalmacenprima= almacenprimaController()
        self.frmalmacenprima.ventana.show()



    def buscarmaterialonclicked(self):
        cod_material = self.ventana.codmaterialtext.text()
        resultado = self.objbuscarmaterial.buscar_material(cod_material)

        # Limpiar la tabla antes de mostrar los resultados
        self.ventana.resultadomaterial.setRowCount(0)

        if resultado:
            # Si se encuentra el material, agregarlo a la tabla
            row_position = self.ventana.resultadomaterial.rowCount()
            self.ventana.resultadomaterial.insertRow(row_position)

            self.ventana.resultadomaterial.setItem(row_position, 0, QTableWidgetItem(resultado[0]))
            self.ventana.resultadomaterial.setItem(row_position, 1, QTableWidgetItem(resultado[1]))
            self.ventana.resultadomaterial.setItem(row_position, 2, QTableWidgetItem(resultado[2]))
            self.ventana.resultadomaterial.setItem(row_position, 3, QTableWidgetItem(str(resultado[3])))
            self.ventana.resultadomaterial.setItem(row_position, 4, QTableWidgetItem(resultado[4]))
            self.ventana.resultadomaterial.setItem(row_position, 5, QTableWidgetItem(str(resultado[5])))
        else:
            # Si no se encuentra el material, mostrar un mensaje de advertencia
            QtWidgets.QMessageBox.warning(self.ventana, "Advertencia", "El material no se encontró.")


        







