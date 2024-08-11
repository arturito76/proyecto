import mysql.connector
class conexionbd():

    def __init__(self):
        self.conexion=mysql.connector.connect(host='localhost', database='siinventario',user='root', password='Arturo76@')

    def getconexionbd(self):
        return self.conexion