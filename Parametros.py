##-------------MODULOS-------------##

import pygame
import sys
import random
import math
import os
from os import listdir
from os.path import isfile, join

pygame.init()

##---------------------------------##

VELOCIDAD_ANIMACION = 5

# COLORES
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

#DIMENSIONES
ANCHO = (1600)
ALTO = (790)


#INFORMACION DE PANTALLA // CODIGO VIEJO

# info = pygame.display.Info()
# tamaño_monitor = (info.current_w, info.current_h)
# tamaño_deseado = (int(tamaño_monitor[0] * 1), int(tamaño_monitor[1] * 0.95))

# Función para obtener los bordes como rectángulos
# def obtener_bordes(ancho_pantalla, alto_pantalla):
#     borde_izquierdo = pygame.Rect(0, 0, 1, alto_pantalla)
#     borde_derecho = pygame.Rect(ancho_pantalla - 1, 0, 1, alto_pantalla)
#     borde_superior = pygame.Rect(0, 0, ancho_pantalla, 1)
#     borde_inferior = pygame.Rect(0, alto_pantalla - 1, ancho_pantalla, 1)
#     return [borde_izquierdo, borde_derecho, borde_superior, borde_inferior]