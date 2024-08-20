import sys
from PyQt5 import QtWidgets, uic
import mysql.connector

# Clase para manejar la conexión a la base de datos
class conexionbd:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='siinventario',
            user='root',
            password='Arturo76@'
        )

    def getconexionbd(self):
        return self.conexion

# Clase para generar reportes
class ReporteAlmacenPrima:
    def __init__(self, tableWidget, comboBox):
        self.tableWidget = tableWidget
        self.comboBox = comboBox
        self.conexion = conexionbd().getconexionbd()

    def generar_reporte(self):
        filtro = self.comboBox.currentText()
        try:
            with self.conexion.cursor() as cursor:
                if filtro == "Material Específico":
                    # Reporte filtrado por material específico
                    sql = """
                    SELECT 
                        ap.cod_material,
                        m.nombre,
                        m.cantidad_disponible,
                        m.unidad_medida,
                        MAX(ap.fecha_ingreso) AS fecha_ingreso,
                        m.precio_unitario,
                        (SUM(ap.cantidad_producto) * m.precio_unitario) AS valor_total,
                        COUNT(*) AS cantidad_registros
                    FROM 
                        almacen_prima ap
                    JOIN 
                        materiales m ON ap.cod_material = m.cod_material
                    GROUP BY 
                        ap.cod_material, m.nombre, m.cantidad_disponible, m.unidad_medida, m.precio_unitario
                    ORDER BY 
                        fecha_ingreso DESC;
                    """
                    cursor.execute(sql)
                    
                elif filtro == "Todos los Materiales":
                    # Reporte con todas las fechas de los materiales registrados
                    sql = """
                    SELECT 
                        ap.cod_material,
                        m.nombre,
                        m.cantidad_disponible,
                        m.unidad_medida,
                        ap.fecha_ingreso,
                        m.precio_unitario,
                        (ap.cantidad_producto * m.precio_unitario) AS valor_total,
                        COUNT(*) AS cantidad_registros
                    FROM 
                        almacen_prima ap
                    JOIN 
                        materiales m ON ap.cod_material = m.cod_material
                    GROUP BY 
                        ap.cod_material, m.nombre, m.cantidad_disponible, m.unidad_medida, ap.fecha_ingreso, m.precio_unitario
                    ORDER BY 
                        ap.fecha_ingreso DESC;
                    """
                    cursor.execute(sql)
                    
                else:
                    print("Selección no válida")
                    return

                resultados = cursor.fetchall()

                # Limpia la tabla antes de insertar los nuevos datos
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(len(resultados[0]) if resultados else 0)
                
                # Configura los encabezados de la tabla
                self.tableWidget.setHorizontalHeaderLabels([
                    "Cod Material", "Nombre", "Cantidad Disponible", "Unidad Medida", "Fecha Ingreso",
                    "Precio Unitario", "Valor Total", "Cantidad Registros"
                ])
                
                for row_number, row_data in enumerate(resultados):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except Exception as e:
            print(f"Error al generar el reporte: {e}")
        finally:
            self.conexion.close()

# Código para ejecutar el reporte en una aplicación PyQt
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('view/reporte.ui', self)  # Cargar el archivo .ui
        self.reporte = ReporteAlmacenPrima(self.tableWidget, self.comboBox)  # Asume que 'tableWidget' y 'comboBox' son los nombres en tu archivo .ui
        self.pushButton.clicked.connect(self.reporte.generar_reporte)  # Conecta el botón al método de generar reporte
        
        # Opciones del ComboBox
        self.comboBox.addItem("Todos los Materiales")
        self.comboBox.addItem("Material Específico")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

