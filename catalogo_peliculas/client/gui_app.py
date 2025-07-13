#Archivo de Interfaz de Usuario
import tkinter as tk
from tkinter import ttk         #Se importa la libreria que nos ayuda con las tablas
from model.pelicula_dao import crear_tabla, borrar_tabla #Se importa desdeel modelo la cracion y borrado de tabas (sql)
from model.pelicula_dao import Pelicula, guardar, listar    #Se importa de model.pelicula,, la clase pelicula

#Se crea una nueva funcion para la bara de menu
def barra_menu(root):
    barra_menu = tk.Menu(root)      #Se crea un objeto de la clase tk.Menu
    root.config(menu = barra_menu, width = 300, height= 300)  #De esta manera seanclaa la barra de Menu/tamaño
    
    menu_inicio = tk.Menu(barra_menu, tearoff= 0)   #Se crea el 1er Menu,se ancla a barra_menu y se eliminan lineas
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)     #Se agrega de la forma

    #Se crea los campos internos de INICIO
    # (En la barra de Menu_inicio.add_command(label= 'CREAR REGISTRO EN DB')Navegacion)
    # Se utiliza el modelo de Creacion y Borrado de tablas, para cambiar Crear Registros en la DB y Eliminar registros en la DB
    menu_inicio.add_command(label= 'Crear Registros en la DB', command= crear_tabla) #Se crea tabla cuando se cree un registro nuevo en la barra de Navegación
    menu_inicio.add_command(label= 'Eliminar registros en la DB', command= borrar_tabla)    #Se elimina una tabla cuando se toque en la Barra de Navegacion
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

        self.campos_pelicula()      #Se ejecutan los campos de pelicula aca, para que lo pinte enla Ventana(Frame)
        self.deshabilitar_campos()  #Se ejecuta este método de deshabilitar los campos
        self.tabla_peliculas()      #Se ejecuta aca paraque la tabla de Peliculas se muestre en la Ventan(Frame)


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
        self.mi_nombre = tk.StringVar()             #Se Crea un Objeto Strinvar(), para Enviar y/o recibir textos
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)  #Se crea un objeto tk.Entry/// Se toma textvariable, para pasar el objeto Stringvar() creado arriba
        self.entry_nombre.config(width= 50,font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_nombre.grid(row= 0, column= 1, padx= 10, pady= 10,columnspan= 2) #Se configura la ubicacion en la Ventana(Frame)
        #Entrada de Duracion
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable= self.mi_duracion)     #Se crea un objeto tk.Entry
        self.entry_duracion.config(width= 50,font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_duracion.grid(row= 1, column= 1, padx= 10, pady= 10,columnspan= 2)
        #Entrada de Genero
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)          #Se crea un objeto tk.Entry
        self.entry_genero.config(width= 50,font= ('Arial', 12)) #configuración de los espacio de Entrada de datos
        self.entry_genero.grid(row= 2, column= 1, padx= 10, pady= 10,columnspan= 2)

        #BOTON NUEVO de 1ra parte
        self.boton_nuevo = tk.Button(self, text= 'Nuevo', command= self.habilitar_campos)  #Se crea un objetotipo Boton//Se agrega atributo command para que cuando se oprima En Boton Nuevo, se ejecute la funcion Habilitar Campos
        self.boton_nuevo.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#158645',
                                cursor= 'hand2', activebackground= '#35BD6f')
        self.boton_nuevo.grid(row=3,column=0, padx= 10, pady= 10)
        #Boton Guardar
        self.boton_guardar = tk.Button(self, text= 'Guardar', command= self.guardar_datos) #Se coloca command, para que se cargueel metodoGuardas datos al oprimir el boton         
        self.boton_guardar.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#1658A2',
                                cursor= 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row=3,column=1, padx= 10, pady= 10)
        #Boton Cancelar
        self.boton_cancelar = tk.Button(self, text= 'Cancelar',command= self.deshabilitar_campos)   #Se utiliza con el metodo Deshabilitar campos          
        self.boton_cancelar.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#BD152E',
                                cursor= 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row=3,column=2, padx= 10, pady= 10)

    #Creacion de metodo para habilitar campos(Boton Nuevo)
    def habilitar_campos(self):
        #Se envian campos vacios, para que por medio del metodo SET cuando se habiliten sean campos vacios
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state = 'normal')
        self.entry_duracion.config(state = 'normal')
        self.entry_genero.config(state = 'normal')
        #Habilitar los Botones Guardar y Cancelar
        self.boton_guardar.config(state = 'normal')
        self.boton_cancelar.config(state = 'normal')

    #Creacion de metodo para Deshabilitar campos  //Se ejecuta en el Frame
    def deshabilitar_campos(self):
        #Se envian campos vacios, para que por medio del metodo SET cuando se oprima Cancelar o Guardar se envien los campos
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state = 'disabled')
        self.entry_duracion.config(state = 'disabled')
        self.entry_genero.config(state = 'disabled')
        #Deshabilitar los Botones Guardar y Cancelar
        self.boton_guardar.config(state = 'disabled')
        self.boton_cancelar.config(state = 'disabled')
    
    #Se crea un objeto de la clase Pelicula, y ese objeto se le envia a la funcion guardar
    def guardar_datos(self):
        #Se crea un objeto de la clase Pelicula
        pelicula = Pelicula(
            self.mi_nombre.get(),        #Se obtiene la info de el Entry Nombre
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )

        #Se crea el registro del objeto pelicula
        guardar(pelicula)
        #Se actualiza la tablae el Frame
        self.tabla_peliculas()

        self.deshabilitar_campos()

    #Diseñar la tabla para mostrar datos en el Frame(Ventana)
    def tabla_peliculas(self):
        #Recuperala lista de peliculas, para mostrarla e el Frame
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()  #Se invierte la tabla


        self.tabla = ttk.Treeview(self, column = ('Nombre', 'Duracion','Genero'))   #Nombre de Columnas
        self.tabla.grid(row=4,column= 0,columnspan= 4, padx= 10, pady= 10)      #Ubicacion en la grilla
        
        self.tabla.heading('#0', text= 'ID')
        self.tabla.heading('#1', text= 'NOMBRE')
        self.tabla.heading('#2', text= 'DURACION')
        self.tabla.heading('#3', text= 'GENERO')

        #Iterar la lista de Peliculas
        for p in self.lista_peliculas:
            self.tabla.insert('',0,text=p[0], values= (p[1],p[2],p[3]))
        #INSERCION DE DATOS DE PRUEBA
        #self.tabla.insert('',0,text= '1', values= ('Los Vengadores', '2.35','Acción')) 

        #BOTON EDITAR
        self.boton_editar = tk.Button(self, text= 'Editar')  #Se crea un objetotipo Boton
        self.boton_editar.config(width= 20, font= ('Arial', 12,'bold'),
                                fg= '#DAD5D6', bg= '#158645',cursor= 'hand2', activebackground= '#35BD6f')
        self.boton_editar.grid(row=5,column=0, padx= 10, pady= 10)

        #BOTON ELIMINAR
        self.boton_eliminar = tk.Button(self, text= 'Eliminar')             
        self.boton_eliminar.config(width= 20, font= ('Arial', 12,'bold'),fg= '#DAD5D6', bg= '#BD152E',
                                cursor= 'hand2', activebackground= '#E15370')
        self.boton_eliminar.grid(row=5,column=1, padx= 10, pady= 10)
