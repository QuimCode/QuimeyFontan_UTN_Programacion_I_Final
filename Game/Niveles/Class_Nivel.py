##-------------MODULOS-------------##

import pygame
import sys
from os import listdir
from os.path import isfile, join

##-------------ARCHIVOS-------------##

from Game.Parametros import *
from ..Personajes.Personaje import *
# from Enemigo import *
from ..Recursos.Sprites.Sprites import *
from ..Recursos.Plataformas.Class_Plataforma import *


##---------------------------------##

class Nivel:
    def __init__(self, numero) -> None:
        pygame.init()
        pygame.joystick.init()

        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        fondo_original = pygame.image.load(fondos_nivel.get(numero))
        self.fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO)).convert()
        self.camara_X = 0

        self.jugador = Personaje(900, 750, 100, 100)

        # Instanciar los enemigos para este nivel
        self.enemigos = pygame.sprite.Group()  # Grupo para almacenar los enemigos

        # Agregar enemigos al grupo
        for enemigo in enemigos_nivel.get(numero, []):
            self.enemigos.add(enemigo)  # Agrega cada enemigo individualmente

        self.plataformas = pygame.sprite.Group()
        self.plataformas.add(plataformas_nivel[numero])

        # Variables para control del tiempo
        self.reloj = pygame.time.Clock()
        self.tiempo_anterior = pygame.time.get_ticks()
        self.tiempo = 0

        self.puntaje = 0

        # Inicialización de la fuente
        self.fuente = pygame.font.Font(None, 36)

    def dibujar_texto_de_niveles(self, superficie):
            # Definición de posiciones de texto (en relación con la cámara)
            texto_posiciones = {
                "Vida": (450, 50),
                "Escudo": (600, 50),
                "Proyectil": (800, 50),
                "Tiempo": (1000, 50),
                "Puntaje": (1200, 50),
                # "Jugador": (100, 50)  # Agregamos la posición del texto del jugador
            }

            # Actualizar textos
            textos = {
                "Vida": f"Vida: {self.jugador.vida}",
                "Escudo": f"Escudo: {self.jugador.escudo}",
                "Proyectil": f"Proyectil: {self.jugador.proyectiles}",
                "Tiempo": f"Tiempo: {self.tiempo}",
                "Puntaje": f"Puntaje: {self.puntaje}",
                # "Jugador": f"Jugador: {self.jugador_nombre}"  # Agregamos el nombre del jugador
            }

            for texto, posicion in texto_posiciones.items():
                # Renderizar el texto en la superficie
                texto_surface = self.fuente.render(textos[texto], True, BLANCO)
                # Obtener el rectángulo del texto y establecer su posición
                texto_rect = texto_surface.get_rect(topleft=posicion)
                # Dibujar el texto en la ventana
                self.ventana.blit(texto_surface, texto_rect)

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
        self.enemigos.update()
        self.plataformas.update() 

        self.jugador.aplicar_colisionar(self.plataformas, self.enemigos)

    def dibujar_nivel(self):
        self.ventana.fill(NEGRO)
        for x in range(0, 8000, self.fondo.get_width()):
            for y in range(0, ALTO, self.fondo.get_height()):
                self.ventana.blit(self.fondo, (x - self.camara_X, y))
        # Dibuja solo las plataformas que están dentro de la pantalla visible
        for plataforma in self.plataformas:
            if self.camara_X <= plataforma.rect.right and plataforma.rect.left <= self.camara_X + ANCHO:
                self.ventana.blit(plataforma.image, (plataforma.rect.x - self.camara_X, plataforma.rect.y))

        # Dibujar los enemigos con la misma lógica de la cámara
        for enemigo in self.enemigos:
            if self.camara_X <= enemigo.rect.right and enemigo.rect.left <= self.camara_X + ANCHO:
                self.ventana.blit(enemigo.image, (enemigo.rect.x - self.camara_X, enemigo.rect.y))

        self.jugador.dibujar_en_pantalla(self.ventana, offset_x=-self.camara_X)
        self.dibujar_texto_de_niveles(self.ventana)


#-------------LISTA/DICCIONARIO PLATAFORMAS-------------#

plataformas_nivel = {
    1: [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO), Plataformas(799,0,6500,100,NEGRO), Plataformas(800,100,6500,10,ROJO)],
    2: [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO)],
    3:  [ Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
        Plataformas(1800, 730, 100, 200, NEGRO)],
}

enemigos_nivel = {
    1: [Enemigo(1100, 720, 100, 100), Enemigo(2100, 710, 100, 100), Enemigo(3100, 710, 100, 100), Enemigo(4100, 710, 100, 100), Enemigo(5100, 710, 100, 100)]
}

fondos_nivel = {
    1: "Game\Recursos\Mapas_Fondos\Free Pixel Art Forest\Preview\Background.png",
    2: "Game\Recursos\Mapas_Fondos\Free Pixel Art Hill\PREVIEWS\Hills Free (update 3.0).png",
    3: "Game\\Recursos\\Mapas_Fondos\\Glacial-mountains-parallax-background_vnitti\\background_glacial_mountains.png"
}

# from Class_Menu import nombre_jugador_global

# class Datos:
#     def __init__(self):
#         # Acceder al nombre del jugador global desde Class_Menu
#         self.nombre_jugador = nombre_jugador_global

#     def obtener_nombre_jugador(self):
#         return self.nombre_jugador

#     def establecer_nombre_jugador(self, nombre):
#         self.nombre_jugador = nombre

#     # Métodos para guardar y recuperar datos aquí