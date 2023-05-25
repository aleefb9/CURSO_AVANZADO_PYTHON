from tkinter import *

# constantes
ANCHO = 600
ALTO = 400
POSX = 100
POSY = 100

def click():
    texto = "Hola, "+nombre.get()+" tienes "+str(edad.get())+" años"
    etiquetaResultado.configure(text=texto)

anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionx = "+"+str(POSX)
posiciony = "+"+str(POSY)
ventana = Tk()
ventana.title("Posicionamiento ventana")
# ventana.resizable(False, False) # Permtir cambiar tamaño a la ventana
ventana.config()
ventana.geometry(anchoAlto+posicionx+posiciony)
frame = Frame()
frame.pack()
frame.config()
# variables
nombre = StringVar()
edad = IntVar()
etiquetaNombre = Label(frame, text="Nombre", font=('Arial', 12))
etiquetaNombre.grid(column=1, row=2)
entradaNombre = Entry(frame, textvariable=nombre, width=50)
entradaNombre.grid(column=2,row=2)
etiquetaEdad = Label(frame, text="Edad", font=('Arial', 12))
etiquetaEdad.grid(column=1, row=3)
entradaEdad = Entry(frame, textvariable=edad, width=50)
entradaEdad.grid(column=2,row=3)
edad.set("16")

etiquetaResultado = Label(frame, text="Textos cambiante", font=("Arial", 12))
etiquetaResultado.grid(column=2, row=7)
boton = Button(frame, text="Pulsame", bg="red", fg="yellow", command=click)
boton.grid(column=2,row=5)
ventana.mainloop() # Refresca la ventana todo el rato

