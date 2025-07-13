#Este modulo va a contener la clase de conexion a la Base de Datos
import sqlite3      #Paquete que se utiliza para bases de Datos de SQLITE

#Se crea la CLASE COnexion
class ConexionDB:
    #Se crea el constructor de la clase ConexionDB
    def __init__(self):
        #Se coloca como atributo el nombre de la Base de Datos
        self.base_datos = 'database/peliculas.db'   #Se crea (SI NO existe) la base de Datos llamada peliculas, en la carpeta Database
        self.conexion = sqlite3.connect(self.base_datos)       #Se crea un atributo que crea la Conexion
        self.cursor = self.conexion.cursor()    #Se crea un cursor, Que sirve para escribir y/o modificar la BD
           

    def cerrar(self):
        self.conexion.commit()      #Se realizaun Commit de lomodificado en la BD
        self.conexion.close()       #Se cierra la conexion con la BD