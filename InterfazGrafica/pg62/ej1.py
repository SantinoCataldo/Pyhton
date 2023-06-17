import tkinter as tk

class Aplicacion:
    def __init__(self):

        self.ventana1 = tk.Tk()
        self.label1 = tk.Label(self.ventana1, text="Ingrese nombre: ")
        self.label1.grid(column=0, row=0)
        self.nombre = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=30, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)

        self.label2 = tk.Label(self.ventana1, text="Ingrese Pais: ")
        self.label2.grid(column=0, row=2)
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=3)
        self.listbox1.insert(0,"Argentna")
        self.listbox1.insert(1,"Uruguay")
        self.listbox1.insert(2,"Paraguay")
        self.listbox1.insert(3,"Bolivia")
        self.listbox1.insert(4,"Peru")
        self.listbox1.insert(5,"Brasil")

        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=4)
        self.label3=tk.Label(self.ventana1, text="si")
        self.label3.grid(column=0, row=5)
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label3.configure(text= "Nombre: " + self.nombre.get() + " || Pais: " + self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()       