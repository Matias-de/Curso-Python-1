#GUI = Graphical User Interface
#Tkinter
import tkinter as tk
#componentes del tkinter:
from tkinter import ttk

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
ventana.title('Manejo de Grid')
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


entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER) #, state='disabled', #, show='*')
entrada1.grid(row=0, column=0)
#insert agrega un texto
entrada1.insert(0, 'Ingresa un texto')
entrada1.insert(tk.END, '.')
entrada1.config(state='readonly')




ventana.mainloop()
