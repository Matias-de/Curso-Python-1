import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext
from time import sleep


class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.iconbitmap('argentina.ico')
        self.title('Componentes')
        self._crearTabs()

    def _crearTabs(self):
        #creamos un tab control, usamos clase Notebook
        controlTabulador = ttk.Notebook(self)
        #agregamos un marco o frame para agregar dentro del tab
        #y organizar los elementos del tab
        tabulador1 = ttk.Frame(controlTabulador)
        #agregamos el tabulador al control de tabuladores
        controlTabulador.add(tabulador1, text='Tabulador 1')
        #mostramos el tabulador
        controlTabulador.pack(fill='both')
        #creamos los componentes del tabulador1
        self._crearComponentesTab1(tabulador1)
        #creamos un segundo tabulador
        tabulador2 = tk.LabelFrame(controlTabulador, text='Contenido')
        controlTabulador.add(tabulador2, text='Tabulador 2')
        #creamos los componentes del segundo tabulador
        self._crearComponentesTab2(tabulador2)
        #crear un tercer tabulador
        tabulador3 = ttk.Frame(controlTabulador)
        controlTabulador.add(tabulador3, text='Tabulador 3')
        #creamos lo componentes del tercer tabulador
        self._crearComponentesTab3(tabulador3)
        #creamos un cuarto tabulador
        tabulador4 = ttk.Labelframe(controlTabulador, text='Imagen')
        controlTabulador.add(tabulador4, text='Tabulador 4')
        #creamos los componentes del cuarto tabulador
        self._crearComponentesTab4(tabulador4)
        #creamos un quinto tabulador
        tabulador5 = ttk.Labelframe(controlTabulador, text='Barra de progreso')
        controlTabulador.add(tabulador5, text='Tabulador 5')
        #creamos los componentes del quinto tabulador
        self._crearComponentesTab5(tabulador5)

    def _crearComponentesTab1(self, tabulador):
        #agregar una etiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador, text='Nombre:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        #agregamos un boton
        def enviar():
            messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

        boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def _crearComponentesTab2(self, tabulador):
        contenido = 'Este es mi texto con el contenido'
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        #mostramos el componente
        scroll.grid(row=0, column=0)

    def _crearComponentesTab3(self, tabulador):
        #creamos una lista usando data list comprehensions
        datos = [x + 1 for x in range(100, 200)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        #seleccionar un elemento por default a mostrar
        combobox.current(5 - 1)

        #agregar un boton para saber que opcion selecciono el usuario
        def mostrarValor():
            messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')

        boton1 = ttk.Button(tabulador, text='Mostrar valor Seleccionado', command=mostrarValor)
        boton1.grid(row=0, column=1)

    def _crearComponentesTab4(self, tabulador):
        imagen = tk.PhotoImage(file='python-logo.png')

        def mostrarTitulo():
            messagebox.showinfo('Mas info imagen', f'Nombre Imagen: {imagen.cget("file")}')

        botonImagen = ttk.Button(tabulador, image=imagen, command=mostrarTitulo)
        botonImagen.grid(row=0, column=0)

    def _crearComponentesTab5(self, tabulador):
        #creamos el componente de barra de progreso
        barraProgreso = ttk.Progressbar(tabulador, orient='horizontal', length=500)
        barraProgreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        #metodos para controlar los eventos de la barra de progreso
        def ejecutarBarra():
            barraProgreso['maximum'] = 100
            for valor in range(101):
                # mandamos a esperar un poco antes de continuar la ejecucion de la barra
                sleep(0.05)
                #incrementamos nuestra barra de progreso
                barraProgreso['value'] = valor
                #actualizamos nuestra barra de progreso
                barraProgreso.update()
            barraProgreso['value'] = 0

        def ejecutarCiclo():
            barraProgreso.start()

        def detener():
            barraProgreso.stop()

        def detenerDespues():
            esperarMs = 1000
            self.after(esperarMs, barraProgreso.stop())

        #botones para controlar lso eventos de una barra de progreso
        botonInicio = ttk.Button(tabulador, text='Ejecutar Barra de Progreso', command=ejecutarBarra)
        botonInicio.grid(row=1, column=0)
        botonCiclo = ttk.Button(tabulador, text='Ejecutar Ciclo', command=ejecutarCiclo)
        botonCiclo.grid(row=1, column=1)
        botonDetener = ttk.Button(tabulador, text='Detener Ejecucion', command=detener)
        botonDetener.grid(row=1, column=2)
        botonDespues = ttk.Button(tabulador, text='Detener Ejecucion despues', command=detenerDespues)
        botonDespues.grid(row=1, column=3)


if __name__ == '__main__':
    componentesVentana = ComponentesVentana()
    componentesVentana.mainloop()
