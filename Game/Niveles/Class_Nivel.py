##-------------MODULOS-------------##

import pygame
import sys
from os import listdir
from os.path import isfile, join

##-------------ARCHIVOS-------------##

from Game.Parametros import *
from ..Personajes.Personaje import Personaje, lista_proyectiles
from ..Personajes.Enemigo import Enemigo, EnemigoVolador, EnemigoMago
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

        self.jugador = Personaje(10, 650, 100, 100)



        # Instanciar los enemigos para este nivel
        self.grupo_proyectiles_jugador = pygame.sprite.Group()

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

    def manejador_eventos_nivel(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    self.jugador.movimiento_izquierda()
                elif event.key == pygame.K_d:
                    self.jugador.movimiento_derecha()
                elif event.key == pygame.K_w and not self.jugador.saltando:
                    self.jugador.movimiento_salto()
                elif event.key == pygame.K_s:
                    self.jugador.disparar_proyectil()
                elif event.key == pygame.K_k:
                    self.jugador.provocar_daño_ligero()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.jugador.movimiento_detener()

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

            if len(lista_proyectiles) > 0:
                print("Lista de proyectiles Nivel:", lista_proyectiles)
                print("Número de proyectiles en la lista Nivel:", len(lista_proyectiles))

    def dibujar_nivel(self):
        self.ventana.fill(NEGRO)
        for x in range(0, 8000, self.fondo.get_width()):
            for y in range(0, ALTO, self.fondo.get_height()):
                self.ventana.blit(self.fondo, (x, y))

        # Dibuja al jugador y otros elementos dependientes de la cámara
        self.jugador.dibujar_en_pantalla(self.ventana)
        self.dibujar_texto_de_niveles(self.ventana)

        # Dibuja solo las plataformas que están dentro de la pantalla visible
        for plataforma in self.plataformas:
            self.ventana.blit(plataforma.image, plataforma.rect)

        # Dibuja todos los enemigos sin importar su posición relativa a la cámara
        for enemigo in self.enemigos:
            enemigo.dibujar_en_pantalla(self.ventana)

        self.grupo_proyectiles_jugador.draw(self.ventana)



    def actualizar_nivel(self):
        limites_ventana = [0, ANCHO, 0, ALTO]

        self.manejador_eventos_nivel()
        self.jugador.actualizar_personaje(limites_ventana)
        self.jugador.aplicar_colisionar(self.plataformas, self.enemigos)
        self.plataformas.update()
        self.enemigos.update()
        self.grupo_proyectiles_jugador.update() 

        # Actualizar los enemigos individualmente
        for enemigo in self.enemigos:
            # Verifica si el sprite es de la clase Enemigo
            if isinstance(enemigo, Enemigo):
                # Llama al método actualizar_enemigo si está disponible
                if hasattr(enemigo, 'actualizar_enemigo'):
                    enemigo.actualizar_enemigo(limites_ventana)








#-------------LISTA/DICCIONARIO PLATAFORMAS-------------#

plataformas_nivel = {
    1: [],
    2: [ ],
    3:  [ ],
}



enemigos_nivel = {
    1: [Enemigo(1100, 720), Enemigo(2100, 710), Enemigo(3100, 710), Enemigo(4100, 710), Enemigo(5100, 710), EnemigoVolador(400, 650), EnemigoMago(100, 650, "izquierda"), EnemigoMago(600, 650, "derecha")]
}

fondos_nivel = {
    1: "Game\Recursos\Mapas_Fondos\Free Pixel Art Forest\Preview\Back1920.png",
    2: "Game\Recursos\Mapas_Fondos\Free Pixel Art Hill\PREVIEWS\Hills1920.png",
    3: "Game\Recursos\Mapas_Fondos\Glacial-mountains-parallax-background_vnitti\HillsFrozen1920.png"
}


# [ Plataformas(1, 0, 845, 1000, NEGRO) Plataformas(6000, 0, 1000, 1000, NEGRO), Plataformas(1800, 630, 100, 100, NEGRO) Plataformas(799,0,6500,100,NEGRO)
# Plataformas(1200, 520, 200, 30, AZUL),Plataformas(4200, 520, 200, 30, AZUL), Plataformas(4100, 560, 200, 30, AZUL), 
#         Plataformas(800,100,6500,10,ROJO), PlataformaBase(795, 795, 6000, 100, ROJO),
#         Plataformas(1022, 654, 200, 30, VERDE)

# Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
#         Plataformas(1800, 730, 100, 200, NEGRO)

# Plataformas(1, 0, 845, 1000, NEGRO), Plataformas(1200, 520, 200, 30, AZUL), Plataformas(6000, 0, 1000, 1000, NEGRO),
#         Plataformas(1800, 730, 100, 200, NEGRO)


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


    # def dibujar_nivel(self):
    #     self.ventana.fill(NEGRO)
    #     for x in range(0, 8000, self.fondo.get_width()):
    #         for y in range(0, ALTO, self.fondo.get_height()):
    #             self.ventana.blit(self.fondo, (x - self.camara_X, y))
        
    #     # Dibujar plataformas estáticas
    #     for plataforma in self.plataformas:
    #         self.ventana.blit(plataforma.image, plataforma.rect)

    #     # Dibujar enemigos
    #     for enemigo in self.enemigos:
    #         self.ventana.blit(enemigo.image, enemigo.rect)

    #     # Dibujar jugador
    #     self.ventana.blit(self.jugador.imagen, self.jugador.rect)

    #     # Otros elementos del HUD
    #     self.dibujar_texto_de_niveles(self.ventana)


    # def dibujar_nivel(self):
    #     self.ventana.fill(NEGRO)
    #     for x in range(0, 8000, self.fondo.get_width()):
    #         for y in range(0, ALTO, self.fondo.get_height()):
    #             self.ventana.blit(self.fondo, (x - self.camara_X, y))
        
    #     # Dibuja todas las plataformas sin importar su posición relativa a la cámara
    #     for plataforma in self.plataformas:
    #         self.ventana.blit(plataforma.image, (plataforma.rect.x - self.camara_X, plataforma.rect.y))

    #     # Dibuja todos los enemigos sin importar su posición relativa a la cámara
    #     for enemigo in self.enemigos:
    #         enemigo.dibujar_en_pantalla(self.ventana, offset_x=-self.camara_X)

    #     # Dibuja al jugador y otros elementos dependientes de la cámara
    #     self.jugador.dibujar_en_pantalla(self.ventana, offset_x=-self.camara_X)
    #     self.dibujar_texto_de_niveles(self.ventana)



            # Captura del clic del ratón
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # 1 para el clic izquierdo
            #         # Obtener las coordenadas del mouse en relación con la pantalla
            #         mouse_x_screen, mouse_y_screen = pygame.mouse.get_pos()
            #         # Ajustar las coordenadas del mouse para tener en cuenta la posición de la cámara
            #         mouse_x_world = mouse_x_screen + self.camara_X
            #         mouse_y_world = mouse_y_screen
            #         print(f"Posición del ratón - X: {mouse_x_world}")
            #         print(f"Posición del ratón - Y: {mouse_y_world}")