##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Personaje import *
from Parametros import *
from Sprites import *

##--------------------------------##

class Enemigo(Personaje):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def dibujar_en_pantalla(self, pantalla):
        # Dibuja al personaje en la pantalla
        pantalla.blit(self.imagen, (self.rect.x, self.rect.y)) 