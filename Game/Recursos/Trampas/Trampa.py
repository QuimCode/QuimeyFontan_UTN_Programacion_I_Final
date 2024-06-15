import pygame
import random

from Game.Parametros import *
from ..Sprites.TrampaSprites import estado_ataque


class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho=10, alto=10):
        super().__init__()
        # Crear el sprite de la trampa
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect.x = x
        self.rect.y = y
        self.ancho = ancho
        self.alto = alto

        self.animacion_trampa = estado_ataque()
        self.indice_animacion = 0
        self.velocidad_animacion = 200  # Ajusta la velocidad de la animación (en milisegundos)
        self.tiempo_animacion = pygame.time.get_ticks()  # Guarda el tiempo actual para la animación

        # Temporizador para activar la trampa periódicamente
        self.tiempo_ultima_activacion = pygame.time.get_ticks()
        self.intervalo_activacion = 5000  # Intervalo de activación en milisegundos (5 segundos)

        # Definir otras características de la trampa, como el daño que inflige
        self.daño = 20

    def dibujar_trampa(self, pantalla):
        # Dibujar la trampa en la superficie especificada
        pygame.draw.rect(pantalla,ROJO, self.rect, 2)
        pantalla.blit(self.image, self.rect)

    def actualizar(self, jugador):
        # Actualizar la animación de la trampa
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_animacion > self.velocidad_animacion:
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion_trampa)
            self.image = self.animacion_trampa[self.indice_animacion]
            self.tiempo_animacion = tiempo_actual

        # Verificar si es el momento de activar la trampa
        if tiempo_actual - self.tiempo_ultima_activacion > self.intervalo_activacion:
            # self.activar_trampa(jugador)
            self.tiempo_ultima_activacion = tiempo_actual

    # def activar_trampa(self, jugador):
    #     jugador.salud -= 10
