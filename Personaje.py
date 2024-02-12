##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Parametros import *
from Sprites import *

##--------------------------------##

instancia_sprite = estado_quieto(), estado_izquierda(), estado_derecha(), estado_saltando()

class Personaje:
    def __init__(self, x, y, ancho, alto) -> None:
        # Composición
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

        # Cargar sprites para diferentes estados
        self.sprites_quieto = estado_quieto()
        self.sprites_izquierda = estado_izquierda()
        self.sprites_derecha = estado_derecha()
        self.sprites_saltando = estado_saltando()
        self.sprites_ataque_der = estado_ataque_ligero_derecha()
        self.sprites_ataque_izq = estado_ataque_ligero_izquierda()
        self.imagen = estado_quieto()[0]

        # Inicializar índice de sprite y temporizador
        self.indice_animacion = 0
        self.contador_animacion = 0
        self.tiempo_sprite = 0
        self.velocidad_animacion = 100  # ajusta esto para cambiar la velocidad de la animación

        # Velocidades iniciales
        self.velocidad_X = 0
        self.velocidad_Y = 0
        self.gravedad = -10
        self.velocidad_salto = 12

        # Estados del Personaje
        self.saltando = False
        self.atacando = False
        self.moviendose_quieto = True
        self.movimidose_derecha = False
        self.movimiendose_izquierda = False

        # Estadísticas
        self.vida = 100
        self.energia = 100
        self.proyectiles = 3
        self.daño_ligero = 20
        self.daño_pesado = 40
        self.daño_proyectil = 50

    def movimiento_detener(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = True
        self.movimidose_derecha = False
        self.movimiendose_izquierda = False

        self.velocidad_X = 0
        self.velocidad_Y = 0  

    def movimiento_izquierda(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = False
        self.movimidose_derecha = False
        self.movimiendose_izquierda = True

        self.velocidad_X = -5
        self.velocidad_Y = 0

    def movimiento_derecha(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = False
        self.movimidose_derecha = True
        self.movimiendose_izquierda = False

        self.velocidad_X = 5
        self.velocidad_Y = 0

    def movimiento_salto(self):
        if not self.saltando:
            self.velocidad_salto = 10
            self.saltando = True

        if self.velocidad_salto >= -10:
            self.velocidad_Y = - (self.velocidad_salto * abs(self.velocidad_salto) * 0.6)
            self.velocidad_salto -= 1
        else:
            self.velocidad_salto = 10 
            self.saltando = False

    def provocar_daño_ligero(self):
        self.atacando = True
        self.saltando = False
        self.moviendose_quieto = False
        self.movimidose_derecha = False
        self.movimiendose_izquierda = False

    def provocar_daño_pesado(self):
        pass

    def aplicar_gravedad(self):
        self.velocidad_Y -= self.gravedad
        self.rect.y += self.velocidad_Y

    def aplicar_colisionar(self, plataformas):
        colisiones = pygame.sprite.spritecollide(self, plataformas, False)

        for plataforma in colisiones:
            if self.velocidad_Y > 0:
                print("Colisión desde arriba")
                self.velocidad_Y = 0
                self.rect.y = plataforma.rect.top - self.rect.height
                self.saltando = False
            elif self.velocidad_Y < 0:
                print("Colisión desde abajo")
                self.velocidad_Y = 0
                self.rect.y = plataforma.rect.bottom
                self.saltando = False

            # Manejar colisiones laterales
            if self.velocidad_X > 0:
                print("Colisión en el lado derecho")
                self.velocidad_X = 0
                self.rect.x = plataforma.rect.left
            elif self.velocidad_X < 0:
                print("Colisión en el lado izquierdo")
                self.velocidad_X = 0
                self.rect.x = plataforma.rect.right


    def aplicar_limites(self, limites):
        # Aplicar límites para evitar que el personaje se escape de la ventana
        self.rect.x = max(limites[0], min(self.rect.x, limites[1] - self.rect.width))
        self.rect.y = max(limites[2], min(self.rect.y, limites[3] - self.rect.height))

    def actualizar_personaje(self, limites=None):
        # Actualizar la posición del personaje según la velocidad
        self.rect.x += self.velocidad_X
        self.aplicar_gravedad()

        # Actualizar el índice de sprite según el tiempo transcurrido
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION:
            self.contador_animacion = 0
            self.indice_animacion += 1

            # Obtén la imagen actual según el estado del personaje


            if self.moviendose_quieto:
                animaciones = self.sprites_quieto
            elif self.saltando:
                animaciones = self.sprites_saltando
            elif self.movimiendose_izquierda:
                animaciones = self.sprites_izquierda
            elif self.movimiento_derecha:
                animaciones = self.sprites_derecha
            elif self.atacando:
                animaciones = self.sprites_ataque_der
            else:
                animaciones = [self.imagen]  # Lista con una sola imagen por defecto

            # if self.atacando:
            #     animaciones = self.sprites_ataque_der
            # # elif self.provocar_daño_ligero:
            # #     animaciones = self.sprites_ataque_izq
            # else:
            #     animaciones = [self.imagen]  # Lista con una sola imagen por defecto

            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            self.imagen = animaciones[self.indice_animacion]

        # Aplicar límites si se proporcionan
        if limites:
            self.aplicar_limites(limites)

    def dibujar_en_pantalla(self, pantalla, offset_x=0):
        padding = 2
        # Dibuja al personaje en la pantalla
        pygame.draw.rect(pantalla, (0, 0, 0), (self.rect.x + offset_x - padding, self.rect.y - padding, self.rect.width + padding * 2, self.rect.height + padding * 2), 2)
        pantalla.blit(self.imagen, (self.rect.x + offset_x, self.rect.y)) 
        # pygame.draw.rect(pantalla, (255, 255, 255), (self.rect.x + offset_x, self.rect.y, self.rect.width, self.rect.height))

    def get_posicion_x(self):
        return self.rect.x
