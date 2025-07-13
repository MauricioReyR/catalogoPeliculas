#En este se haran lasconsultas de la BD//hacer el CRUD
from model.conexion_db import ConexionDB   #Se importa la clase ConexionDB de conexiondb


#Se crea una funcion para Crearlas tablas
def crear_tabla():
    conexion = ConexionDB()    #Crea un objeto de esta clase quecrea la conexión

    #Se crea un codigo sql, para ejecutar dentro de la BD, EN ESTE CASO PARA SQLITE
    sql = """
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT) 
    )"""
    #Para ejecutar el sql anterior se realiza:
    conexion.cursor.execute(sql)    #Se usa el cursor creado paraqueejecute el sql
    conexion.cerrar()

#Para eliminar una tabla se crea un nuevo metodo
def borrar_tabla():
    conexion = ConexionDB()

    #Se crea un codgo sql
    sql = 'DROP TABLE peliculas'

    #Para ejecutarel sql se realiza:
    conexion.cursor.execute(sql)
    conexion.cerrar()

    #Para probar este codig, seva al gui_app.py y se realiza en la barra de menu crear registro y se 
    #realiza lo que queda marcado en ese archivo.