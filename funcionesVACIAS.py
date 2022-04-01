from principal import *
from configuracion import *

import random
import math
palabrasYaUsadas = []


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente
    palabra = random.choice(lista)
    ejesX = [20, 280, 540]
    numeroPosInicial = random.randint(5,20)
    posicionInicial = [numeroPosInicial, numeroPosInicial, numeroPosInicial]
    ejeY = 40
    for letra in palabra:
        numero = random.randint(0,2)
        numeroPos = random.randint(30,60)
        if numero == 0:
            listaIzq.append(letra)
            posicionesIzq.append([ejesX[0] + posicionInicial [0], ejeY])
            posicionInicial[0] += numeroPos
        elif numero == 1:
            listaMedio.append(letra)
            posicionesMedio.append([ejesX[1] + posicionInicial [1], ejeY])
            posicionInicial[1] += numeroPos
        elif numero == 2:
            listaDer.append(letra)
            posicionesDer.append([ejesX[2] + posicionInicial [2], ejeY])
            posicionInicial[2] += numeroPos






def bajar(lista, posiciones):
    # hace bajar las letras y elimina las que tocan el piso
    largo = len(posiciones)
    largoLista = len(lista)
    azar = random.randint(1,10)
    for i in range (largo -1, -1, -1):
        posicion = posiciones[i]
        if posicion[1] <= 460:
            posicion[1] += 30 + azar
        else:
            lista.pop(i)
            posiciones.pop(i)


def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)
    cargarListas(lista,listaIzq,listaMedio,listaDer,posicionesIzq,posicionesMedio,posicionesDer)

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
    # una variable para poner espacio entre letras
    pass
         

def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata
    puntos = 0
    for letra in candidata:
        if letra in "aeiouAEIOU":
            puntos = puntos + 1
        elif letra in "bcdfghlmnoprstBCDFGHLMNOPRST":
            puntos = puntos + 2
        elif letra in "jkqwxyzJQWXYZ":
            puntos = puntos + 5
    return puntos   


def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    puntosCandidata = 0
    valida = esValida (lista,candidata,listaIzq,listaMedio,listaDerecha)
    if valida == True:
        puntosCandidata = Puntos(candidata)
        palabrasYaUsadas.append(candidata)
    else:
        puntosCandidata = 0
    return puntosCandidata
    



def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    #devuelve True si candidata cumple con los requisitos
    habilitadaIzq = True
    habilitadaMedio = True
    habilitadaDerecha = True
    candidataP = ""
    valida = False
    if candidata in lista:
        if candidata not in palabrasYaUsadas:
            for letra in candidata:
                if habilitadaIzq == True and letra in listaIzq:
                    candidataP += letra
                elif habilitadaMedio == True and letra in listaMedio:
                    habilitadoIzq = False
                    candidataP += letra
                elif habilitadaDerecha == True and letra in listaDerecha:
                    habilitadoMedio = False
                    candidataP += letra
        if candidataP == candidata:
            valida = True
        else:
            valida = False
    else:
        valida = False

    return valida

    