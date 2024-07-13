#GUI = Graphical User Interface
#Tkinter
import sys
import tkinter as tk
#componentes del tkinter:
from tkinter import ttk, messagebox, Menu

#creamos un objeto usando la clase Tk
#ventana = tk.Tk()
#modificar el tamaño de la ventana (pixeles)
#ventana.geometry('600x400')
#cambiamos el nombre
#ventana.title('Hola Mundo')
#configuramos el icono de la aplicacion
#ventana.iconbitmap('argentina.ico')


#creamos un boton(widget), el objeto padre es la ventana
#creamos un metodo evento click


#def eventoClick():
#   boton1.config(text='Boton presionado')
#  print('Ejecucion del evento click')
# boton2 = ttk.Button(ventana, text='Nuevo Boton')
#boton2.pack()


#boton1 = ttk.Button(ventana, text='Dar click aqui', command=eventoClick)
#utilizar el pack layout manager para mostrar el boton de la ventana
#boton1.pack()

#iniciamos la ventana (esta linea la ejecutamos al final)
#si la ejecutamos antes, no se muestran los cambios
#ventana.mainloop()

#-------------------------USO DE GRID---------------------------


#creamos un objeto usando la clase Tk
ventana = tk.Tk()
#modificar el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
#cambiamos el nombre
ventana.title('Manejo de componentes')
#configuramos el icono de la aplicacion
ventana.iconbitmap('argentina.ico')

#configurar el grid
#ventana.rowconfigure(0, weight=2)
#ventana.rowconfigure(1, weight=10)
#ventana.columnconfigure(0, weight=1)
#ventana.columnconfigure(1, weight=5)


#definimos los botones y eventos
#def evento1():
#   boton1.config(text='Boton 1 presionado')


#def evento2():
#   boton2.config(text='Boton 2 presionado')

#def evento4():
#   boton4.config(text='Boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')


#N (arriba), E(derecha), S(abajo), W(izquierda)
#boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
#boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)
#boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
#boton2.grid(row=1, column=0, sticky='NSWE')  #NSWE==ocupan todo el espacio que tienen disponibles

#boton3
#boton3 = ttk.Button(ventana, text='Boton 3')
#boton3.grid(row=0, column=1, sticky='NSWE')

#boton4
#boton4 = tk.Button(ventana, text='Boton 4', command=evento4) #configurable solo cuando se use el paquete de tk, y no el ttk
#boton4.grid(row=1, column=1, sticky='NSWE')


#-----------------------COMPONENTE ENTRY-----------------------------------

#width es la cantidad de caracteres que ocupa la caja de texto

#definimos una variable que podemos modificar despues (set), leer (get)
#entradaVar1 = tk.StringVar(value='Valor por defecto')
entrada1 = ttk.Entry(ventana, width=30)  #,textvariable=entradaVar1)  #justify=tk.CENTER)  #, state='disabled', #, show='*')
entrada1.grid(row=0, column=0)
#etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, columnspan=2)


#insert agrega un texto
#entrada1.insert(0, 'Ingresa un texto')
#entrada1.insert(tk.END, '.')


#entrada1.config(state='readonly')

#creamos un boton

def enviar():
    #print(entrada1.get())
    #boton1.config(text=entrada1.get())
    #elminar el contenido
    #entrada1.delete(0, tk.END)
    #seleccionar el texto de la caja
    #entrada1.select_range(0, tk.END)
    #para hacer efectiva la seleccion
    #entrada1.focus()

    #recuperamos la info a partir de la variable asociada a la caja de texto
    #boton1.config(text=entradaVar1.get())
    #modificacion utilizamos la variable de texto y el metodo set
    #entradaVar1.set('Cambio...')
    #recuperamos la informacion
    #modificamos el texto del label
    etiqueta1.config(text=entrada1.get())
    #message box
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')
        #messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
        #messagebox.showwarning('Mensaje de alerta', mensaje1 + ' alerta')


def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos..')
    sys.exit()


def crearMenu():
    #configurar el menu principal
    menuPrincipal = Menu(ventana)
    #tearoff = False para evitar que se separe el menu de la interfaz
    subMenuArchivo = Menu(menuPrincipal, tearoff=0)
    #subMgregamos una nueva opcion al menu de archivo
    subMenuArchivo.add_command(label='Nuevo')
    #agregar un separador
    subMenuArchivo.add_separator()
    #agregamos la opcion de salir
    subMenuArchivo.add_command(label='Salir', command=salir)
    #agregamos el submenu al menu principal
    menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
    #submenu de ayuda
    subMenuAyuda = Menu(menuPrincipal, tearoff=0)
    subMenuAyuda.add_command(label='Acerca de')
    menuPrincipal.add_cascade(menu=subMenuAyuda, label='Ayuda')

    #mostramos el menu en la ventana principal
    ventana.config(menu=menuPrincipal)


boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crearMenu()
ventana.mainloop()
