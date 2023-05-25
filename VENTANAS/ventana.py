from tkinter import *

ventana = Tk()
ventana.title("Mi primera ventana con python")
# ventana.resizable(False, False) # Permtir cambiar tamaño a la ventana
ventana.geometry('640x360')
ventana.config(bg='cyan')
frame = Frame()
frame.pack(side='top')
frame.config(bg='yellow')
frame.config(width= '640', height='250')
ventana.mainloop() # Refresca la ventana todo el rato

