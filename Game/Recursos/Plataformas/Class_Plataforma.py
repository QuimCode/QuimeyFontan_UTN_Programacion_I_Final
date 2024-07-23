##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Game.Recursos.Parametros import *

##--------------------------------##

class Plataformas(pygame.sprite.Sprite):

    ajuste_top_default = 10
    def __init__(self, x, y, ancho, alto, color):
        super().__init__()

        self.image = pygame.Surface((ancho, alto))
        self.rect = pygame.Rect(x, y, ancho, alto)  # Define el rectángulo con las coordenadas x, y, ancho y alto
        self.color = color
        self.image.fill(self.color)

    def dibujar_en_pantalla(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)

class PlataformaBase(Plataformas):
    def __init__(self, x, y, ancho, alto, color=BLANCO):
        super().__init__(x, y, ancho, alto, color)

    def repetir_imagen_a_lo_largo(self, longitud):
        imagen_original = self.image.copy()
        for x in range(self.rect.x, self.rect.x + longitud, imagen_original.get_width()):
            self.rect.x = x
            self.image.blit(imagen_original, (x, self.rect.y))

# class PlataformaMovil(Plataformas):
#     def __init__(self, x, y, ancho, alto, color, velocidad):
#         super().__init__(x, y, ancho, alto, color)
#         self.velocidad = velocidad
#         self.direccion = 1  # 1 significa derecha, -1 significa izquierda

#     def actualizar(self):
#         self.rect.x += self.velocidad * self.direccion
#         # Invertir la dirección si la plataforma alcanza los límites de la pantalla
#         if self.rect.left <= 0 or self.rect.right >= pygame.display.get_surface().get_width():
#             self.direccion *= -1

#     def dibujar_en_pantalla(self, pantalla, offset_x=0, padding=10):
#         # Actualizar la posición antes de dibujar
#         self.actualizar()
#         super().dibujar_en_pantalla(pantalla, offset_x, padding)

class PlataformaVoladora(Plataformas):
    def __init__(self, x, y, ancho, alto, color=BLANCO):
        super().__init__(x, y, ancho, alto, color)
        # self.image = pygame.image.load("ruta_imagen_voladora.png").convert()