import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()                              #Esta crea una interfaz de Usuario
    root.title('Catalogo de Peliculas')         #Cambiar e titulo de la ventana    
    root.iconbitmap('img/cp-logo.ico')          #Colocar un Icono .ico
    root.resizable(0,0)

    barra_menu(root)                            #Se ejecuta barra de Menu
    #Se elimina el 1er objeto creado dela clase Frame y se coloca en la GUI_APP.py// se importa la clase Frame creada

    app = Frame(root = root)

    app.mainloop()             #Se utiliza para que al final se cierre a ventana

if __name__ == '__main__':
    main()
    
