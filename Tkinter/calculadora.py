import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        #atributos de clase
        self.expresion = ''
        #Caja de texto (input)
        self.entrada = None
        #Stringvar lo utilizamos para obtener el valor del input
        self.entradaTexto = tk.StringVar()
        #creamos los componentes
        self._creacionComponentes()

    #metodos de clase
    #crear los componentes
    def _creacionComponentes(self):
        #creamos un frame para la caja de texto
        entradaFrame = tk.Frame(self, width=400, height=50, background='grey')
        entradaFrame.pack(side=tk.TOP)
        #caja de texto
        entrada = tk.Entry(entradaFrame, font=('arial', 18, 'bold'), textvariable=self.entradaTexto, width=30,
                           justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        #agregamos un segundo frame para la parte inferior
        botonesFrame = tk.Frame(self, width=400, height=450, background='grey')
        botonesFrame.pack()

        #Primer renglon
        botonLimpiar = tk.Button(botonesFrame, text='C', width='32', height=3, bd=0, bg='#eee', cursor='hand2',
                                 command=self._eventoLimpiar)
        botonLimpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        #boton dividir
        tk.Button(botonesFrame, text='/', width=10, height=3, bd=0,
                  bg='#eee', cursor='hand2',
                  command=lambda: self._eventoClick('/')
                  ).grid(row=0, column=3, padx=1, pady=1)

        #botonDividir.grid(row=0, column=3, padx=1, pady=1)

        #Segundo Renglon
        botonSiete = tk.Button(botonesFrame, text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(7))
        botonSiete.grid(row=1, column=0, padx=1, pady=1)
        botonOcho = tk.Button(botonesFrame, text='8', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(8))
        botonOcho.grid(row=1, column=1, padx=1, pady=1)
        botonNueve = tk.Button(botonesFrame, text='9', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(9))
        botonNueve.grid(row=1, column=2, padx=1, pady=1)
        botonMultiplicar = tk.Button(botonesFrame, text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClick('*'))
        botonMultiplicar.grid(row=1, column=3, padx=1, pady=1)

        #Tercer Renglon
        botonCuatro = tk.Button(botonesFrame, text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(4))
        botonCuatro.grid(row=2, column=0, padx=1, pady=1)
        botonCinco = tk.Button(botonesFrame, text='5', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(5))
        botonCinco.grid(row=2, column=1, padx=1, pady=1)
        botonSeis = tk.Button(botonesFrame, text='6', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(6))
        botonSeis.grid(row=2, column=2, padx=1, pady=1)
        botonRestar = tk.Button(botonesFrame, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClick('-'))
        botonRestar.grid(row=2, column=3, padx=1, pady=1)

        #Cuarto Renglon

        botonUno = tk.Button(botonesFrame, text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(1))
        botonUno.grid(row=3, column=0, padx=1, pady=1)
        botonDos = tk.Button(botonesFrame, text='2', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(2))
        botonDos.grid(row=3, column=1, padx=1, pady=1)
        botonTres = tk.Button(botonesFrame, text='3', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(3))
        botonTres.grid(row=3, column=2, padx=1, pady=1)
        botonSumar = tk.Button(botonesFrame, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClick('+'))
        botonSumar.grid(row=3, column=3, padx=1, pady=1)

        #Quinto Renglon

        botonCero = tk.Button(botonesFrame, text='0', width=21, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._eventoClick(0))
        botonCero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        botonPunto = tk.Button(botonesFrame, text='.', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._eventoClick('.'))
        botonPunto.grid(row=4, column=2, padx=1, pady=1)
        botonEvaluar = tk.Button(botonesFrame, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=self._eventoEvaluar)
        botonEvaluar.grid(row=4, column=3, padx=1, pady=1)

    def _eventoEvaluar(self):
        #eval evalua la expresion str como una expresion aritmetica
        try:
            if self.expresion:
                resultado = eval(self.expresion)
                self.entradaTexto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entradaTexto.set('')
        finally:
            self.expresion = ''

    def _eventoLimpiar(self):
        self.expresion = ''
        self.entradaTexto.set(self.expresion)

    def _eventoClick(self, elemento):
        # Concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entradaTexto.set(self.expresion)








if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
