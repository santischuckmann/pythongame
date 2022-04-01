import pygame, sys
import os, random, sys, math
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

COLOR_FONDO = (100,20,10)
 
mainClock = pygame.time.Clock()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 600),0,32)
fuenteMenu = pygame.font.SysFont(None, 35)
imagenDeFondo = pygame.image.load("fondoMenu.png")
 
def escribirTexto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
COLOR_FONDO = (100,150,180)
COLOR_FONDO_ORIGINAL = (100,150,180)
 
def main_menu():
    click = False
    while True:
        
        screen.fill((0,0,0))
        screen.blit(imagenDeFondo, (0,0))
        
        pygame.draw.rect(screen, (0,0,0), (170, 15, 480, 35))
        escribirTexto('ARMAR PALABRAS ENCOLUMNADAS', fuenteMenu, (250, 250, 250), screen, 190, 20)
 
        mx, my = pygame.mouse.get_pos()

        
        posicionBotonUno = pygame.Rect(240, 100, 320, 50)
        posicionBotonDos = pygame.Rect(240, 200, 320, 50)
        if posicionBotonUno.collidepoint((mx, my)):
            if click:
                game()
        if posicionBotonDos.collidepoint((mx, my)):
            if click:
                personalizarFondo()
        pygame.draw.rect(screen, (100,150,180), posicionBotonUno)
        pygame.draw.rect(screen, (100,150,180), posicionBotonDos)
        escribirTexto("INICIAR EL JUEGO", fuenteMenu, (255,255,255), screen, 295, 115)
        escribirTexto("PERSONALIZAR FONDO", fuenteMenu, (255,255,255), screen, 255, 216)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []
        sonidoPuntos = pygame.mixer.Sound("marcar.mp3")
        
        pygame.mixer.init()
        pygame.mixer.music.load("musica.mp3") 
        pygame.mixer.music.play(-1,0.0)

        archivo = open("lemario.txt","r")
        for linea in archivo.readlines():
            lista.append(linea[0:-1])

        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 2

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    palabrasYaUsadas = []
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer)
                        sonidoPuntos.play()
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

            pygame.display.flip()

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
 
def personalizarFondo():
    global COLOR_FONDO
    global COLOR_FONDO_ORIGINAL
    click = False
    running = True
    while running:
        screen.fill((0,0,0))

        COLOR_FONDO_ORIGINAL = (100,150,180)
        fuenteVolver = pygame.font.SysFont(None, 25)
        mx, my = pygame.mouse.get_pos()

        coloresRGBFondo = [(200,150,180), (10,50,210), (130,200,10), (130,10,230), (150,130,130)]

        escribirTexto('ELEGÍ UN FONDO', fuenteMenu, (255, 255, 255), screen, 300, 20)
        primerColor = pygame.Rect(30, 100, 120, 400)
        if primerColor.collidepoint((mx, my)):
            if click:
                COLOR_FONDO = coloresRGBFondo[0]
        segundoColor = pygame.Rect(180, 100, 120, 400)
        if segundoColor.collidepoint((mx, my)):
            if click:
                COLOR_FONDO = coloresRGBFondo[1]
        tercerColor = pygame.Rect(330, 100, 120, 400)
        if tercerColor.collidepoint((mx, my)):
            if click:
                COLOR_FONDO = coloresRGBFondo[2]
        cuartoColor = pygame.Rect(480, 100, 120, 400)
        if cuartoColor.collidepoint((mx, my)):
            if click:
                COLOR_FONDO = coloresRGBFondo[3]
        quintoColor = pygame.Rect(630, 100, 120, 400)
        if quintoColor.collidepoint((mx, my)):
            if click:
                COLOR_FONDO = coloresRGBFondo[4]
        posicionVolver = pygame.Rect(615, 15, 180, 35)
        if posicionVolver.collidepoint((mx,my)):
            if click:
                main_menu()

        pygame.draw.rect(screen, (200,150,180), primerColor)
        pygame.draw.rect(screen, (10,50,210), segundoColor)
        pygame.draw.rect(screen, (130,200,10), tercerColor)
        pygame.draw.rect(screen, (130,10,230), cuartoColor)
        pygame.draw.rect(screen, (150,130,130), quintoColor)

        pygame.draw.rect(screen, (150,130,130), posicionVolver)
        escribirTexto('VOLVER AL MENÚ', fuenteVolver, (255, 255, 255), screen, 630, 20)
        
    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                COLOR_FONDO = (100,150,180)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()