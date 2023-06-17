import sys
import tkinter as tk


class Aplicacion:
    def __init__(self):
        
        self.ventana1 = tk.Tk()

        self.label1 = tk.Label(self.ventana1, text="Ingrese valor 1: ")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        self.label2 = tk.Label(self.ventana1, text="Ingrese valor 1: ")
        self.label2.grid(column=0, row=1)
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)

        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Medida Seleccionada", command=self.sumar)
        opciones1.add_command(label="Finalizar Programa", command=self.terminar)
        menubar1.add_cascade(label="Tamaño", menu=opciones1)
        self.ventana1.mainloop()

  

    def sumar(self):
        suma=(self.dato1.get()) +'x'+ (self.dato2.get())
        self.ventana1.geometry(suma)

    def terminar(self):
        sys.exit(0)


aplicacion1 = Aplicacion()