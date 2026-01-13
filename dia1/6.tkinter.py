from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f"HOLA, {nombre}!")
    messagebox.showinfo("Saludo",f"Hola, {nombre}")
# creamos un objeto de la clase TK
app = Tk()
#titulo de la ventana
app.title("mi primera aplicacion con tkinter")
#dimensiones de la ventana
app.geometry("400x100")

#crear un objeto frame
Frame = Frame(app)
Frame.grid(row=0,column=0,padx=20,pady=20)

#crear una etiqueta (label) dentro del frame
lb_nombre = Label(Frame,text="Nombre :")
lb_nombre.grid(row=0,column=0)
#crear una caja de texto (entry) dentro del frame
txt_nombre = Entry(Frame)
txt_nombre.grid(row=0,column=1)
#crear un boton (button) dentro del frame
btn_saludar = Button(Frame,text="Saludar", command=saludar)
btn_saludar.grid(row=1,column=0,columnspan=2)

#mostramos la ventana
app.mainloop()