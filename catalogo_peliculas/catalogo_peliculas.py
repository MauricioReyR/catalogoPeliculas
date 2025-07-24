import tkinter as tk
from client.gui_app import Frame, barra_menu

import os
import sys

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al recurso, funciona para desarrollo y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y almacena los archivos allí
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    root = tk.Tk()                              #Esta crea una interfaz de Usuario
    root.title('Catalogo de Peliculas')         #Cambiar e titulo de la ventana    
    icon_path = resource_path('img/cp-logo.ico')
    root.iconbitmap(icon_path)
    #root.iconbitmap('img/cp-logo.ico')          #Colocar un Icono .ico
    root.resizable(0,0)

    barra_menu(root)                            #Se ejecuta barra de Menu
    #Se elimina el 1er objeto creado dela clase Frame y se coloca en la GUI_APP.py// se importa la clase Frame creada

    app = Frame(root = root)

    app.mainloop()             #Se utiliza para que al final se cierre a ventana

if __name__ == '__main__':
    main()
    
