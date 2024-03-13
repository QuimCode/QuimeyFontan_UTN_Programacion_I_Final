##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Personajes.Personaje import *
from Parametros import *
from Sprites import *

import random  # Importamos la librería random para generar movimientos aleatorios
from moviepy.editor import VideoFileClip

##--------------------------------##


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        # Crear el sprite del enemigo
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(ROJO)  # Color del enemigo (puedes cambiarlo según tu diseño)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ancho = ancho
        self.alto = alto

        # Estadísticas
        self.vida = 100
        self.escudo = 100
        self.energia = 100
        self.proyectiles = 3
        self.daño_ligero = 20
        self.daño_pesado = 40
        self.daño_proyectil = 50

        # Velocidades iniciales
        self.velocidad_X = 0
        self.velocidad_Y = 0

        # self.sprites_quieto = estado_quieto_enemigo()  # Agregar el sprite de estado quieto del enemigo
        self.indice_animacion = 0
        self.estado_quieto = True  # Bandera de estado para indicar si el enemigo está en estado quieto

    def actualizar_personaje(self, limites=None):
        # Generar movimientos aleatorios
        if random.randint(1, 100) == 1:  # Cambiar el número para ajustar la frecuencia de cambios de dirección
            self.velocidad_X = random.choice([-5, 5])  # Moverse a la izquierda o derecha aleatoriamente

        # Actualizar la posición del enemigo según la velocidad
        self.rect.x += self.velocidad_X

        # Aplicar límites si se proporcionan
        if limites:
            self.aplicar_limites(limites)

        # Lógica para determinar si el enemigo está en estado quieto
        if self.velocidad_X == 0 and self.velocidad_Y == 0:
            self.estado_quieto = True
        else:
            self.estado_quieto = False

        # Actualizar el índice de sprite según el estado del enemigo
        if self.estado_quieto:
            animaciones = self.sprites_quieto
        else:
            pass

    def aplicar_limites(self, limites):
        # Aplicar límites para evitar que el enemigo se escape de la ventana
        self.rect.x = max(limites[0], min(self.rect.x, limites[1] - self.rect.width))
        self.rect.y = max(limites[2], min(self.rect.y, limites[3] - self.rect.height))

    def dibujar_en_pantalla(self, pantalla):
        # Dibujar al enemigo en la pantalla
        pygame.draw.rect(pantalla, ROJO, self.rect)  # Dibujar un rectángulo rojo como representación del enemigo

    def ataque_ligero(self, personaje):
        daño_ligero = self.daño_ligero
        daño_ligero - personaje.vida
