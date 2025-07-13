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

#Se crea una tabla Pelicula,que es igual ala que esta en la tabla
class Pelicula:
    def __init__(self,nombre,duracion,genero):
        #Se construye un constructor
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    #Crear el estado del Objeto anterior
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion},{self.genero}]'
    
#Se crea una funcion que ingresa o Guarda los datos
def guardar(pelicula):
    conexion = ConexionDB()

    #Se hace un sql que ingresa los datos
    sql = f"""iNSERT INTO peliculas (nombre, duracion,genero) 
    VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""

    #Se usa el Cursor para ingresar los datos
    #Se mete este codigo en un try-Except paraque no de el error de NO creacion de la BD
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla Peliculas NO esta Creada en la BD'
        messagebox.showerror(titulo,mensaje)

    #CON ESTO SE VA A GUARDAR DATOS Y SE REALIZA

#Se hace un fncion para LISTAR
def listar():
    conexion = ConexionDB()     #Se hace la conexion

    lista_peliculas = []

    sql = 'SELECT * FROM peliculas'

    #Se manejan los Errores
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()      #Metodo para retornar toda la lista de pelicuals
        conexion.cerrar()
    except:
        titulo = ('Conexion alRegistro')
        mensaje= ('Esta Tabla No Existe en la Base de Datos')
        messagebox.showwarning(titulo, mensaje)

    #retorna la lista_peliculas
    return lista_peliculas

    #Para mostrar la tabla, setrabaja el codigo en el Frame en tabla de peliculas se agrega:
