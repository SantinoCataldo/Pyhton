import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("test")

        self.boton1=tk.Button(self.ventana1, text="Hombre", command=self.hombre)
        self.boton1.grid(column=0, row=0)

        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.mujer)
        self.boton2.grid(column=1, row=0)

        self.ventana1.mainloop()


    def hombre(self):
        self.ventana1.title("Hombre")

    def mujer(self):
        self.ventana1.title("Mujer")      


aplicacion1=Aplicacion()
