#En este se haran lasconsultas de la BD//hacer el CRUD
from model.conexion_db import ConexionDB   #Se importa la clase ConexionDB de conexiondb
from tkinter import messagebox          #Se importa para los mensajes de Alerta en Ventana Emergentes


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
    #Se agrega este codigo en un Try-Except, para quitar los errores de cuando la BD Existe /No existe
    try:
        conexion.cursor.execute(sql)    #Se usa el cursor creado para que ejecute el sql
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se Creo la Tabla Exitosamente en la Base de Datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La Tabla ya esta Creada en la Base de Datos'
        messagebox.showwarning(titulo, mensaje)
#Para eliminar una tabla se crea un nuevo metodo
def borrar_tabla():
    conexion = ConexionDB()

    #Se crea un codgo sql
    sql = 'DROP TABLE peliculas'

    #Para ejecutarel sql se realiza:
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La Tabla se Elimino Exitosamente en la Base de Datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'La Tabla No Existe en la Base de Datos'
        messagebox.showerror(titulo, mensaje)
    #Para probar este codig, seva al gui_app.py y se realiza en la barra de menu crear registro y se 
    #realiza lo que queda marcado en ese archivo.