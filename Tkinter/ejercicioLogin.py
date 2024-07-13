import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        #modificar el tamaño de la ventana (pixeles)
        self.geometry('300x130')
        #cambiamos el nombre
        self.title('Login')
        #configuramos el icono de la aplicacion
        self.iconbitmap('argentina.ico')
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self._crearComponentes()

        #definir el metodo crear componentes

    def _crearComponentes(self):
        etiquetaUsuario = ttk.Label(self, text='Usuario:')
        etiquetaUsuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        etiquetaContra = ttk.Label(self, text='Contraseña:')
        etiquetaContra.grid(row=1, column=0, sticky=tk.E, pady=5, padx=5)
        self.entradaUsuario = ttk.Entry(self)
        self.entradaUsuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.entradaContra = ttk.Entry(self, show='*')
        self.entradaContra.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        boton1 = ttk.Button(self, text='Login', command=self._loggCommand)
        boton1.grid(row=3, column=0, columnspan=2, pady=10)

    def _loggCommand(self):
        messagebox.showinfo('Datos Login',
                            f'Usuario: {self.entradaUsuario.get()}, Contraseña: {self.entradaContra.get()}')


if __name__ == '__main__':
    loginVentana = Login()
    loginVentana.mainloop()
