from PyQt5 import QtWidgets, uic
from dao.stockdao import AlmacenStockBD
from model.almacenStock import AlmacenStockMode  # Asegúrate de que este es el nombre correcto
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime

class AlmacenStockController:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.objalmacenstockdao = AlmacenStockBD()  # Usa la clase correcta aquí
        self.ventana = uic.loadUi("view/registrarstock.ui")

        # Configuración de la tabla de stock
        self.ventana.tablastock.setColumnWidth(0, 50)
        self.ventana.tablastock.setColumnWidth(1, 250)
        self.ventana.tablastock.setColumnWidth(2, 120)
        self.ventana.tablastock.setColumnWidth(3, 100)
        self.ventana.tablastock.setColumnWidth(4, 100)
        self.ventana.tablastock.setColumnWidth(5, 100)

        # Conexión de eventos
        self.ventana.agregarstock.clicked.connect(self.agregarstockonclicked)
        self.ventana.cancelarstock.clicked.connect(self.cancelarstockclicked)
        self.ventana.tablastock.cellClicked.connect(self.tablastockcellClick)

        # Mostrar ventana y listar el stock
        self.ventana.show()
        self.listar_almacen_stock()
        app.exec()

    def tablastockcellClick(self, fila, columna):
        try:
            cod_almacen_stock = self.ventana.tablastock.item(fila, 0).text()
            self.ventana.codstock.setText(cod_almacen_stock)
            self.ventana.codstock.setEnabled(False)

            objstock = self.objalmacenstockdao.buscar_almacen_stock(cod_almacen_stock)

            fecha_stock = objstock[0]  # Corregido el índice de la fecha
            if isinstance(fecha_stock, datetime):
                fecha_stock_str = fecha_stock.strftime('%d-%m-%Y')
            else:
                fecha_stock_str = str(fecha_stock)

            self.ventana.fechastock.setText(fecha_stock_str)
            self.ventana.cantidadstock.setText(str(objstock[1]))
            self.ventana.nombrestock.setText(str(objstock[2]))
            self.ventana.codemple.setText(str(objstock[3]))
            self.ventana.codproductostock.setText(str(objstock[4]))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def cancelarstockclicked(self):
        try:
            self.ventana.codstock.clear()
            self.ventana.codstock.setEnabled(True)
            self.ventana.fechastock.clear()
            self.ventana.cantidadstock.clear()
            self.ventana.nombrestock.clear()
            self.ventana.codemple.clear()
            self.ventana.codproductostock.clear()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def agregarstockonclicked(self):
        try:
            cod_almacen_stock = self.ventana.codstock.text()
            fecha_ingreso = self.ventana.fechastock.text()
            cantidad_producto = self.ventana.cantidadstock.text()
            nombre_producto = self.ventana.nombrestock.text()
            cod_empleado = self.ventana.codemple.text()
            cod_producto = self.ventana.codproductostock.text()

            nuevo_stock = AlmacenStockMode(cod_almacen_stock, fecha_ingreso, cantidad_producto, nombre_producto, cod_empleado, cod_producto)

            if self.ventana.codstock.isEnabled():
                self.objalmacenstockdao.insertar_almacen_stock(nuevo_stock)
            else:
                self.objalmacenstockdao.actualizar_almacen_stock(nuevo_stock)

            self.listar_almacen_stock()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")

    def listar_almacen_stock(self):
        try:
            liststock = self.objalmacenstockdao.listar_almacen_stock()
            cantidad = len(liststock)

            self.ventana.tablastock.setRowCount(cantidad)

            for fila, stock in enumerate(liststock):
                self.ventana.tablastock.setItem(fila, 0, QTableWidgetItem(stock[0]))
                self.ventana.tablastock.setItem(fila, 1, QTableWidgetItem(str(stock[1])))
                self.ventana.tablastock.setItem(fila, 2, QTableWidgetItem(str(stock[2])))
                self.ventana.tablastock.setItem(fila, 3, QTableWidgetItem(str(stock[3])))
                self.ventana.tablastock.setItem(fila, 4, QTableWidgetItem(str(stock[4])))
                self.ventana.tablastock.setItem(fila, 5, QTableWidgetItem(str(stock[5])))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", f"Se ha producido un error: {e}")
