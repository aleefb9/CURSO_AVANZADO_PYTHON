from tkinter import *

def click():
    texto = "Hola, "+entrada.get()
    etiqueta.configure(text=texto)



ventana = Tk()
ventana.title("Widgets Basicos")
# ventana.resizable(False, False) # Permtir cambiar tamaño a la ventana
ventana.geometry('650x400')
frame = Frame()
frame.pack()
frame.config()
frame.config(width= '640', height='350')
etiqueta = Label(frame, text="Etiqueta", font=("Arial", 25))
etiqueta.grid(column=1, row=2)
entrada = Entry(frame, width=50)
entrada.grid(column=2, row=2)
buton = Button(frame, text="Pulsame", bg="red", fg="yellow", command=click)
buton.grid(column=1, row=4)
ventana.mainloop() # Refresca la ventana todo el rato

