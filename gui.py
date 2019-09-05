import ahorcado as bknd

from tkinter import *
from tkinter.ttk import *



def ObtenerLetra(*args):
    limitar()
    l = letra.get()
    bknd.letras_utilizadas.append(l)  # Pone la letra como utilizada.
    
    if l in bknd.letras_utilizadas:
        txt_advertencia
        

def limitar():
    letra.set(letra.get().upper())
    if len(letra.get()) > 1:
        letra.set(letra.get()[1])
        # print('<DEBUG>letra = '+str(letra.get()))


def CerrarVentana():
    ventana.destroy()


bknd.InicioJuego()
ventana = Tk()


letra=StringVar()
letra.trace('w',ObtenerLetra)    #Entra a la función cada vez que se modifica el contenido del Entry box.

ent_letra = Entry(ventana, width=2, textvariable=letra)
ent_letra.place(x=200,y=200)





ventana.title("Ahorcado")
ventana.geometry('600x400')

txt_letra = Label(ventana, text='Letra:')
txt_letra.place(x=155,y=200)

txt_advertencia = Label(ventana, text='¡Letra ya utilizada!')  #Còmo cambiar el texto multiples veces?
txt_advertencia.place(x=220,y=200)

ventana.mainloop()
