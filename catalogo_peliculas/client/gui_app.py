#Archivo de Interfaz de Usuario
import tkinter as tk

#Se crea una Clase Frame
class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width= 480,height=320,)   #se hereda de la clase padre    
        self.root = root        #Se crea un atributo root que recibe el root
        self.pack()             #Se utiliza el metodo pack de Frame(Porla herencia)
        self.config(bg= 'green')  #Se conguriran "detalles visuales color"
