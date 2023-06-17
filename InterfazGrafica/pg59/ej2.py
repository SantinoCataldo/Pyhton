import tkinter as tk

class Aplicacion:
    def __init__(self):

        self.ventana1 = tk.Tk()
        self.label1 = tk.Label(self.ventana1, text="Ingrese nombre: ")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        self.label2 = tk.Label(self.ventana1, text="Ingrese clave: ")
        self.label2.grid(column=0, row=1)
        self.dato2 = tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)

        self.boton1= tk.Button(self.ventana1, text="ingresar", command=(self.ingresar))
        self.boton1.grid(column=1, row=2)
        self.label3=tk.Label(self.ventana1, text="")
        self.label3.grid(column=1, row=3)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.dato1.get()=="Juan" and self.dato2.get()== "abc123":
            self.label3.configure(text="Correcto")
        else:
            self.label3.configure(text="Incorrecto")

aplicacion1=Aplicacion()