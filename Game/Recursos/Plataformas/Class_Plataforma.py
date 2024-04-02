##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Game.Parametros import *

##--------------------------------##

class Plataformas(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color):
        super().__init__()

        self.image = pygame.Surface((ancho, alto))
        self.rect = pygame.Rect(x, y, ancho, alto)  # Define el rectángulo con las coordenadas x, y, ancho y alto
        self.color = color
        self.image.fill(self.color)

    def dibujar_en_pantalla(self, pantalla, offset_x=0):
        pygame.draw.rect(pantalla, ROJO, self.rect.move(-offset_x, 0), 10)  # Dibuja el rectángulo de la plataforma
        pantalla.blit(self.image, (self.rect.x - offset_x, self.rect.y))

class PlataformaBase(Plataformas):
    def __init__(self, x, y, ancho, alto, color=BLANCO):
        super().__init__(x, y, ancho, alto, color)

    def repetir_imagen_a_lo_largo(self, longitud):
        imagen_original = self.image.copy()
        for x in range(self.rect.x, self.rect.x + longitud, imagen_original.get_width()):
            self.rect.x = x
            self.image.blit(imagen_original, (x, self.rect.y))

class PlataformaVoladora(Plataformas):
    def __init__(self, x, y, ancho, alto, color=BLANCO):
        super().__init__(x, y, ancho, alto, color)
        # self.image = pygame.image.load("ruta_imagen_voladora.png").convert()