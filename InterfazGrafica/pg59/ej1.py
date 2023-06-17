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

        self.boton1= tk.Button(self.ventana1, text="sumar", command=(self.sumar))
        self.boton1.grid(column=1, row=2)
        self.label3=tk.Label(self.ventana1, text="Resultado: ")
        self.label3.grid(column=1, row=3)
        self.ventana1.mainloop()

    def sumar(self):
        suma=int(self.dato1.get()) + int(self.dato2.get())
        self.label3.configure(text=suma)

aplicacion1=Aplicacion()