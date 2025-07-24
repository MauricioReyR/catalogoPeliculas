#Este modulo va a contener la clase de conexion a la Base de Datos
import sqlite3
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ConexionDB:
    def __init__(self):
        self.base_datos = resource_path('database/peliculas.db')
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()