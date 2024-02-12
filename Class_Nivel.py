##-------------MODULOS-------------##

import pygame
import sys
from os import listdir
from os.path import isfile, join

##-------------ARCHIVOS-------------##

from Parametros import *
from Personaje import *
from Enemigo import *
from Sprites import *
from Class_Plataforma import *

##---------------------------------##

class Nivel:
    def __init__(self, numero) -> None:
        pygame.init()
        pygame.joystick.init()

        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        fondo_original = pygame.image.load(fondos_nivel.get(numero))
        self.fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO)).convert()
        self.camara_X = 0

        self.jugador = Personaje(900, 10, 100, 100)
        self.pj_enemigo = Enemigo(1100, 10, 100, 100)
        self.plataformas = pygame.sprite.Group()
        self.plataformas.add(plataformas_nivel[numero])

        # Variables para control del tiempo
        self.reloj = pygame.time.Clock()
        self.tiempo_anterior = pygame.time.get_ticks()



    def manejador_eventos_nivel(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            # Captura del clic del ratón
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 para el clic izquierdo
                    mouse_x = pygame.mouse.get_pos()
                    mouse_y = pygame.mouse.get_pos()
                    print(f"Posición del ratón - X: {mouse_x}")
                    print(f"Posición del ratón - Y: {mouse_y}")

            #-----------MOVIMIENTO-----------#

            # Toma de presion de teclas y asignacion de metodos de movimiento de la clase Personaje instanciada en la variable jugador # 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.jugador.movimiento_izquierda()
                elif event.key == pygame.K_d:
                    self.jugador.movimiento_derecha()
                elif event.key == pygame.K_w and not self.jugador.saltando:
                    self.jugador.movimiento_salto()
                elif event.key == pygame.K_s:
                    self.jugador.provocar_daño_ligero()
                # elif event.key == pygame.K_k:
                #     self.jugador.provocar_daño_pesado()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.jugador.movimiento_detener()
            #-----------MOVIMIENTO-----------#


    
    def imprimir_posicion_personaje(self):
        posicion_x = self.jugador.get_posicion_x()
        print(f"Posición del personaje - X: {posicion_x}")

    def actualizar_nivel(self):
        limites_ventana = [850, 6000, 0, ALTO]
        self.camara_X = self.jugador.rect.x - (ANCHO // 2) 
        self.jugador.actualizar_personaje(limites_ventana)
        self.pj_enemigo.actualizar_personaje(limites_ventana)

        self.plataformas.update() 
        self.jugador.aplicar_colisionar(self.plataformas)

    def dibujar_nivel(self):
        self.ventana.fill(NEGRO)
        for x in range(0, 8000, self.fondo.get_width()):
            for y in range(0, ALTO, self.fondo.get_height()):
                self.ventana.blit(self.fondo, (x - self.camara_X, y))
        # Dibuja solo las plataformas que están dentro de la pantalla visible
        for plataforma in self.plataformas:
            if self.camara_X <= plataforma.rect.right and plataforma.rect.left <= self.camara_X + ANCHO:
                self.ventana.blit(plataforma.image, (plataforma.rect.x - self.camara_X, plataforma.rect.y))

        self.jugador.dibujar_en_pantalla(self.ventana, offset_x=-self.camara_X)
        self.pj_enemigo.dibujar_en_pantalla(self.ventana)
#-------------LISTA/DICCIONARIO PLATAFORMAS-------------#

plataformas_nivel = {
    1: [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO)],
    2: [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO)],
    3:  [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO)]
}

# capas_mapa = {
#     "Capa1": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/1.png").convert_alpha(),
#     "Capa2": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/2.png").convert_alpha(),
#     "Capa3": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/3.png").convert_alpha(),
#     "Capa4": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/4.png").convert_alpha(),
#     "Capa5": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/5.png").convert_alpha(),
#     "Capa6": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/6.png").convert_alpha(),
#     "Capa7": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/7.png").convert_alpha(),
#     "Capa8": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/8.png").convert_alpha(),
#     "Capa9": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/9.png").convert_alpha(),
#     "Capa10": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/10.png").convert_alpha(),
#     "Capa11": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/11.png").convert_alpha(),
#     "Capa12": pygame.image.load("Mapas_Fondos/Free Pixel Art Winter Forest/PNG/12.png").convert_alpha()
# }


fondos_nivel = {
    1: "Mapas_Fondos/Free Pixel Art Forest/Preview/Background.png",
    2: "Mapas_Fondos/Free Pixel Art Hill/PREVIEWS/Hills Free (update 3.0).png",
    3: "Mapas_Fondos/Glacial-mountains-parallax-background_vnitti/background_glacial_mountains.png"
}

