# archivo: controller/controller_reporte_material.py
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from dao.reportedao import ReporteMaterialDAO

class ControllerReporteMaterial:
    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.obj_reporte_material = ReporteMaterialDAO()
        self.ventana = uic.loadUi("view/reporte.ui")  # Cambia el nombre según tu archivo .ui

        # Configuración de las columnas de la tabla
        self.ventana.resultadomaterial.setColumnWidth(0, 200)
        self.ventana.resultadomaterial.setColumnWidth(1, 200)
        self.ventana.resultadomaterial.setColumnWidth(2, 200)
        self.ventana.resultadomaterial.setColumnWidth(3, 200)
        self.ventana.resultadomaterial.setColumnWidth(4, 200)
        self.ventana.resultadomaterial.setColumnWidth(5, 200)
        self.ventana.resultadomaterial.setColumnWidth(6, 200)

        # Configurar el QComboBox con los códigos de materiales
        for i in range(1, 10):
            self.ventana.comboBox.addItem(f"M00{i}")

        # Conectar el botón para generar el reporte
        self.ventana.generarReporte.clicked.connect(self.generar_reporte)
        self.ventana.regresar.clicked.connect(self.regresaroncliked)
        #self.ventana.show()
        #app.exec()
    def regresaroncliked(self):
        self.ventana.close()
        from controller.menuprincipal import menu_principal
        self.frmmenuprincipal=menu_principal()
        self.frmmenuprincipal.ventana.show()
    def generar_reporte(self):
        codigo_material = self.ventana.comboBox.currentText()

        resultados = self.obj_reporte_material.generar_reporte(codigo_material)

        # Limpiar la tabla antes de mostrar los resultados
        self.ventana.resultadomaterial.setRowCount(0)

        if resultados:
            # Si se encuentran resultados, agregarlos a la tabla
            self.ventana.resultadomaterial.setRowCount(len(resultados))
            for row_idx, row_data in enumerate(resultados):
                for col_idx, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ventana.resultadomaterial.setItem(row_idx, col_idx, item)
        else:
            # Si no se encuentran resultados, mostrar un mensaje de advertencia
            QtWidgets.QMessageBox.warning(self.ventana, "Advertencia", "No se encontraron resultados para el material seleccionado.")


