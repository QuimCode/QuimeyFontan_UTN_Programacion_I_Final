import pygame
import random

from ..Sprites.TrampaSprites import estado_ataque


class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho=10, alto=10):
        super().__init__()
        # Crear el sprite de la trampa
        self.image = pygame.Surface((ancho, alto))
        self.image.fill((255, 0, 0))  # Color rojo para la trampa
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Animaciones de la trampa
        self.animacion_trampa = estado_ataque()
        self.indice_animacion = 0
        self.velocidad_animacion = 15  # Ajusta la velocidad de la animación
        self.tiempo_animacion = pygame.time.get_ticks()  # Guarda el tiempo actual para la animación

        # Temporizador para activar la trampa periódicamente
        self.tiempo_ultima_activacion = pygame.time.get_ticks()
        self.intervalo_activacion = 5000  # Intervalo de activación en milisegundos (5 segundos)

        # Definir otras características de la trampa, como el daño que inflige
        self.damage = 20

    def dibujar_trampa(self, surface):
        # Dibujar la trampa en la superficie especificada
        surface.blit(self.image, self.rect)

    def actualizar(self, jugador):
        # Actualizar la animación de la trampa
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_animacion > self.velocidad_animacion:
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion_trampa)
            self.image = self.animacion_trampa[self.indice_animacion]
            self.tiempo_animacion = tiempo_actual

        # Verificar si es el momento de activar la trampa
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultima_activacion > self.intervalo_activacion:
            self.activar_trampa(jugador)
            self.tiempo_ultima_activacion = tiempo_actual

    def activar_trampa(self, jugador):
        jugador.vida -= 10
