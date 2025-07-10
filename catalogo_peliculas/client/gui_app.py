#Archivo de Interfaz de Usuario
import tkinter as tk

#Se crea una nueva funcion para la bara de menu
def barra_menu(root):
    barra_menu = tk.Menu(root)      #Se crea un objeto de la clase tk.Menu
    root.config(menu = barra_menu, width = 300, height= 300)  #De esta manera seanclaa la barra de Menu/tamaño
    
    menu_inicio = tk.Menu(barra_menu, tearoff= 0)   #Se crea el 1er Menu,se ancla a barra_menu y se eliminan lineas
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)     #Se agrega de la forma

    #Se crea los campos internos de INICIO(En la barra de Nmenu_inicio.add_command(label= 'CREAR REGISTRO EN DB')avegacion)
    menu_inicio.add_command(label= 'Crear Registros en la DB') 
    menu_inicio.add_command(label= 'Eliminar registros en la DB')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)  #oton de salir en el menu/funcion de salida

    #Se crean los demas Menus
    barra_menu.add_cascade(label= 'Consultas')
    barra_menu.add_cascade(label= 'Configuracion')
    barra_menu.add_cascade(label= 'Ayuda')

#Se crea una Clase Frame
class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width= 480,height=320,)   #se hereda de la clase padre    
        self.root = root        #Se crea un atributo root que recibe el root
        self.pack()             #Se utiliza el metodo pack de Frame(Porla herencia)
        #self.config(bg= 'green')  #Se conguriran "detalles visuales color"

        self.campos_pelicula()      #Se ejecutan los campor de pelicula aca, para que lo pinte enla Ventana(Frame)

    #Se crea una funcion para los campos de la pelicula
    def campos_pelicula(self):          #Como es u metodo de la clase Frame lleva (self)
        #Label´s de cada campo
        self.labol_nombre = tk.Label(self, text= 'Nombre: ')            #Se crea un Objeto de la clase Label
        self.labol_nombre.config(font= ('Arial', 12,'bold'))            #Se configura tipos de letra
        self.labol_nombre.grid(row= 0,column= 0, padx= 10,pady= 10)   #Se posciciona en el Frame(Ventana)
        #Label Duracion
        self.labol_duracion = tk.Label(self, text= 'Duracion: ')
        self.labol_duracion.config(font= ('Arial', 12,'bold'))
        self.labol_duracion.grid(row= 1,column= 0, padx= 10,pady= 10)
        #Label Genero
        self.labol_genero = tk.Label(self, text= 'Genero: ')
        self.labol_genero.config(font= ('Arial', 12,'bold'))
        self.labol_genero.grid(row= 2,column= 0, padx= 10,pady= 10)  
        
        #Entry´s de cada uno de los campos (Campos de Entrada)
        self.entry_nombre = tk.Entry(self)          #Se crea un objeto tk.Entry
        self.entry_nombre.config(width= 50, state= 'disabled',font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_nombre.grid(row= 0, column= 1, padx= 10, pady= 10,columnspan= 2) #Se configura la ubicacion en la Ventana(Frame)
        #Entrada deDuracion
        self.entry_duracion = tk.Entry(self)          #Se crea un objeto tk.Entry
        self.entry_duracion.config(width= 50, state= 'disabled',font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_duracion.grid(row= 1, column= 1, padx= 10, pady= 10,columnspan= 2)

        self.entry_genero = tk.Entry(self)          #Se crea un objeto tk.Entry
        self.entry_genero.config(width= 50, state= 'disabled',font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_genero.grid(row= 2, column= 1, padx= 10, pady= 10,columnspan= 2)

        #Botones de 1ra parte
        self.boton_nuevo = tk.Button(self, text= 'Nuevo')          #Se crea un objetotipo Boton
        self.boton_nuevo.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#158645',
                                cursor= 'hand2', activebackground= '#35BD6f')
        self.boton_nuevo.grid(row=4,column=0, padx= 10, pady= 10)
        #Boton Guardar
        self.boton_guardar = tk.Button(self, text= 'Guardar')          
        self.boton_guardar.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#1658A2',
                                cursor= 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row=4,column=1, padx= 10, pady= 10)

        self.boton_cancelar = tk.Button(self, text= 'Cancelar')          
        self.boton_cancelar.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#BD152E',
                                cursor= 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row=4,column=2, padx= 10, pady= 10)