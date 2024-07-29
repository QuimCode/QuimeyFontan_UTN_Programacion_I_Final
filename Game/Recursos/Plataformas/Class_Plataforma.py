# ##-------------MODULOS-------------##

# import pygame

# ##--------------------------------##

# from Game.Recursos.Parametros import *

# ##--------------------------------##

# class Plataformas(pygame.sprite.Sprite):

#     ajuste_top_default = 10
#     def __init__(self, x, y, ancho, alto, color):
#         super().__init__()

#         self.image = pygame.Surface((ancho, alto))
#         self.rect = pygame.Rect(x, y, ancho, alto)  # Define el rectángulo con las coordenadas x, y, ancho y alto
#         self.color = color
#         self.image.fill(self.color)

#     def dibujar_en_pantalla(self, pantalla):
#         pygame.draw.rect(pantalla, self.color, self.rect)

# class PlataformaBase(Plataformas):
#     def __init__(self, x, y, ancho, alto, color=BLANCO):
#         super().__init__(x, y, ancho, alto, color)

#     def repetir_imagen_a_lo_largo(self, longitud):
#         imagen_original = self.image.copy()
#         for x in range(self.rect.x, self.rect.x + longitud, imagen_original.get_width()):
#             self.rect.x = x
#             self.image.blit(imagen_original, (x, self.rect.y))

# class PlataformaVoladora(Plataformas):
#     def __init__(self, x, y, ancho, alto, color=BLANCO):
#         super().__init__(x, y, ancho, alto, color)

##-------------MODULOS-------------##
import pygame
pygame.init()
##--------------------------------##
from Game.Recursos.Parametros import *

##--------------------------------##
class Plataformas(pygame.sprite.Sprite):
    ajuste_top_default = 10
    
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, ancho, alto)

    def dibujar_en_pantalla(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)

class PlataformaBase(Plataformas):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def aplicar_tileset(self, tileset):
        tile_width = tileset.get_width()
        tile_height = tileset.get_height()
        for x in range(0, self.rect.width, tile_width):
            self.image.blit(tileset, (x, 0))

class PlataformaVoladora(Plataformas):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)

    def aplicar_tileset(self, tileset):
        tile_width = tileset.get_width()
        tile_height = tileset.get_height()
        for x in range(0, self.rect.width, tile_width):
            self.image.blit(tileset, (x, 0))

class PlataformaRoca(Plataformas):
    def __init__(self, x, y, ancho, alto, imagen_roca):
        super().__init__(x, y, ancho, alto)
        # Redimensionar la imagen de roca a las dimensiones especificadas
        self.image = pygame.transform.scale(imagen_roca, (ancho, alto))
        self.rect = self.image.get_rect(topleft=(x, y))
