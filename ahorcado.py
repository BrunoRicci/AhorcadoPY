import random
import gui

_INTENTOS_MAXIMOS = 5



palabras = ['arbol']
letras_utilizadas=[]




def InicioJuego():
    letras_utilizadas=[]    #Resetea a ninguna.

    f = open("palabras.txt", "r")
    for p in f:
        p = p[:-1]
        palabras.append(p)



    # f = open("palabras.txt", "w")
    # f.write("uno\n")bnm
    f.close()





def ObtenerLetra(*args):
    limitar()
    l = letra.get()
    letras_utilizadas.append(l)  # Pone la letra como utilizada.


def limitar():
    letra.set(letra.get().upper())
    if len(letra.get()) > 1:
        letra.set(letra.get()[1])
    # print('<DEBUG>letra = '+str(letra.get()))


def mostrar(g):
    for l in g:
        print(l, end=" ")
    print("")



palinc = random.choice(palabras)
guiones = "_" * len(palinc)

mostrar(palinc)

mostrar(guiones)


guiones = ["_"] * len(palinc)
while True:
    n = 0
    letra = input()
    
    for i,l in enumerate(palinc):
        if l == letra:
            guiones[i] = letra
        
    mostrar(guiones)
        
    if "_" not in guiones:
        break
    
    
  
