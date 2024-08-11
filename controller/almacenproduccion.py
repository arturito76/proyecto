from PyQt5 import QtWidgets, uic
from dao.producciondao import almacenproduccionbd
from model.produccion import Produccionmodel
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime

class AlmacenProduccionController:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.objalmacenproducciondao = almacenproduccionbd()
        self.ventana = uic.loadUi("view/produccionregistrar.ui")

        # Configuración de la tabla de producción
        self.ventana.tablaproduccion.setColumnWidth(0, 50)
        self.ventana.tablaproduccion.setColumnWidth(1, 250)
        self.ventana.tablaproduccion.setColumnWidth(2, 120)
        self.ventana.tablaproduccion.setColumnWidth(3, 100)
        self.ventana.tablaproduccion.setColumnWidth(4, 100)
        self.ventana.tablaproduccion.setColumnWidth(5, 100)  # Corregido el índice de la columna

        # Conexión de eventos
        self.ventana.registrarproduccion.clicked.connect(self.registrarproducciononclicked)
        self.ventana.cancelarprod.clicked.connect(self.cancelarprodonclicked)
        self.ventana.tablaproduccion.cellClicked.connect(self.tablaproduccioncellClick)

        # Mostrar ventana y listar la producción
        self.ventana.show()
        self.listar_almacen_produccion()
        app.exec()

    def tablaproduccioncellClick(self, fila, columna):
        try:
            cod_produccion = self.ventana.tablaproduccion.item(fila, 0).text()
            self.ventana.codpro.setText(cod_produccion)
            self.ventana.codpro.setEnabled(False)

            objproduccion = self.objalmacenproducciondao.buscar_almacen_produccion(cod_produccion)

            fecha_produccion = objproduccion[0]  # Corregido el índice de la fecha
            if isinstance(fecha_produccion, datetime):
                fecha_produccion_str = fecha_produccion.strftime('%d-%m-%Y')
            else:
                fecha_produccion_str = str(fecha_produccion)

            self.ventana.fechapro.setText(fecha_produccion_str)
            self.ventana.cantidadpro.setText(str(objproduccion[1]))
            self.ventana.codemple.setText(str(objproduccion[2]))
            self.ventana.codmaterial.setText(str(objproduccion[3]))
            self.ventana.codproducto.setText(str(objproduccion[4]))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def cancelarprodonclicked(self):
        try:
            self.ventana.codpro.clear()
            self.ventana.codpro.setEnabled(True)
            self.ventana.codmaterial.clear()
            self.ventana.fechapro.clear()
            self.ventana.cantidadpro.clear()
            self.ventana.codemple.clear()
            self.ventana.codproducto.clear()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def registrarproducciononclicked(self):
        try:
            cod_produccion = self.ventana.codpro.text()
            fecha_produccion = self.ventana.fechapro.text()
            cantidad_produccion = self.ventana.cantidadpro.text()
            cod_empleado = self.ventana.codemple.text()
            cod_material = self.ventana.codmaterial.text()
            cod_producto = self.ventana.codproducto.text()

            nuevoproduccion = Produccionmodel(cod_produccion, fecha_produccion, cantidad_produccion, cod_empleado, cod_material, cod_producto)

            if self.ventana.codpro.isEnabled():
                self.objalmacenproducciondao.insertar_produccion(nuevoproduccion)
            else:
                self.objalmacenproducciondao.actualizar_almacen_produccion(nuevoproduccion)

            self.listar_almacen_produccion()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def listar_almacen_produccion(self):
        try:
            listpro = self.objalmacenproducciondao.listar_almacen_produccion()
            cantidad = len(listpro)

            self.ventana.tablaproduccion.setRowCount(cantidad)

            for fila, produccion in enumerate(listpro):
                self.ventana.tablaproduccion.setItem(fila, 0, QTableWidgetItem(produccion[0]))
                self.ventana.tablaproduccion.setItem(fila, 1, QTableWidgetItem(str(produccion[1])))
                self.ventana.tablaproduccion.setItem(fila, 2, QTableWidgetItem(str(produccion[2])))
                self.ventana.tablaproduccion.setItem(fila, 3, QTableWidgetItem(str(produccion[3])))
                self.ventana.tablaproduccion.setItem(fila, 4, QTableWidgetItem(produccion[4]))
                self.ventana.tablaproduccion.setItem(fila, 5, QTableWidgetItem(produccion[5]))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")



