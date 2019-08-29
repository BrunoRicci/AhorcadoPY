import ahorcado as bknd

from tkinter import *
from tkinter.ttk import *


def CerrarVentana():
    ventana.destroy()

ventana = Tk()







ventana.title("Ahorcado")
ventana.geometry('600x400')

txt_letra = Label(ventana, text='Letra:')
txt_letra.place(x=5,y=10)



