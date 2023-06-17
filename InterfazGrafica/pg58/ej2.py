import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Test")

        self.boton1=tk.Button(self.ventana1, text="1", command=self.uno)
        self.boton1.grid(column=0, row=0)

        self.boton2=tk.Button(self.ventana1, text="2", command=self.dos)
        self.boton2.grid(column=1, row=0)

        self.boton3=tk.Button(self.ventana1, text="3", command=self.tres)
        self.boton3.grid(column=2, row=0)

        self.boton4=tk.Button(self.ventana1, text="4", command=self.cuatro)
        self.boton4.grid(column=3, row=0)

        self.boton5=tk.Button(self.ventana1, text="5", command=self.cinco)
        self.boton5.grid(column=4, row=0)

        self.datos=""
        self.label1=tk.Label(self.ventana1, text=self.datos)
        self.label1.grid(column=0, row=1)

        self.ventana1.mainloop()


    def uno(self):
        self.datos+="1"
        self.label1.configure(text=self.datos)

    def dos(self):
        self.datos+="2"
        self.label1.configure(text=self.datos)

    def tres(self):
        self.datos+="3"
        self.label1.configure(text=self.datos)
          
    def cuatro(self):
        self.datos+="4"
        self.label1.configure(text=self.datos)
           
    def cinco(self):
        self.datos+="5"
        self.label1.configure(text=self.datos)
           

aplicacion1=Aplicacion()