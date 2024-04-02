import pygame

from ..Sprites.ProyectilesSprites.ProyectilSpriteEnemigo import *
from ..Sprites.ProyectilesSprites.ProyectilSpriteJugador import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad_x, velocidad_y, ancho, alto):
        super().__init__()

        # Establecer la imagen predeterminada (cuadrado rojo)
        self.imagen = pygame.Surface((ancho, alto))
        self.imagen.fill((255, 0, 0))  # Relleno rojo
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Definir la velocidad en los ejes X e Y
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y

    def update(self):
        # Mover el proyectil en los ejes X e Y
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def dibujar(self, pantalla):
        # Dibujar el proyectil en la pantalla
        pantalla.blit(self.imagen, self.rect)

    def hacer_danio(self, objetivo):
        # Método abstracto para hacer daño a un objetivo
        pass


class ProyectilEnemigo(Proyectil):
    def __init__(self, x, y, velocidad_x, velocidad_y, ancho=100, alto=90):
        # Llama al constructor de la clase padre (Proyectil)
        super().__init__(x, y, velocidad_x, velocidad_y, ancho, alto)
        
        # Define las imágenes específicas para los proyectiles del enemigo
        self.sprites_disparo_derecha = estado_disparo_derecha()
        self.sprites_disparo_izquierda = estado_disparo_izquierda()

        # Establece la imagen inicial del proyectil (por ejemplo, hacia la derecha)
        self.imagen = self.sprites_disparo_derecha[0]

        # Inicializa el índice de animación
        self.indice_animacion = 0

    def actualizar_disparo(self):
        # Mueve el proyectil en los ejes X e Y
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Actualiza la imagen del proyectil para la animación
        self.animar()

    def animar_disparo(self):
        # Actualiza la imagen del proyectil para la animación
        if self.velocidad_x > 0:
            # Si el proyectil se mueve hacia la derecha, usa las imágenes de disparo hacia la derecha
            self.imagen = self.sprites_disparo_derecha[self.indice_animacion]
        else:
            # Si el proyectil se mueve hacia la izquierda, usa las imágenes de disparo hacia la izquierda
            self.imagen = self.sprites_disparo_izquierda[self.indice_animacion]

        # Incrementa el índice de animación para avanzar en la animación
        self.indice_animacion += 1

        # Reinicia el índice de animación si supera la cantidad de imágenes
        if self.indice_animacion >= len(self.sprites_disparo_derecha):
            self.indice_animacion = 0

    def hacer_daño_jugador(self, objetivo):
        # Implementa el método para hacer daño específico para los proyectiles del enemigo
        pass

class ProyectilJugador(Proyectil):
    def __init__(self, x, y, velocidad_x, velocidad_y, ancho=100, alto=90):
        # Llama al constructor de la clase padre (Proyectil)
        super().__init__(x, y, velocidad_x, velocidad_y, ancho, alto)
        
        # Define las imágenes específicas para los proyectiles del jugador
        self.sprites_disparo_derecha = estado_disparoJ_derecha()
        self.sprites_disparo_izquierda = estado_disparoJ_izquierda()

        # Establece la imagen inicial del proyectil (por ejemplo, hacia la derecha)
        self.imagen = self.sprites_disparo_derecha[0]

        # Inicializa el índice de animación
        self.indice_animacion = 0

    def actualizar(self):
        # Mueve el proyectil en los ejes X e Y
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Actualiza la imagen del proyectil para la animación
        self.animar()

    def animar(self):
        # Actualiza la imagen del proyectil para la animación
        if self.velocidad_x > 0:
            # Si el proyectil se mueve hacia la derecha, usa las imágenes de disparo hacia la derecha
            self.imagen = self.sprites_disparo_derecha[self.indice_animacion]
        else:
            # Si el proyectil se mueve hacia la izquierda, usa las imágenes de disparo hacia la izquierda
            self.imagen = self.sprites_disparo_izquierda[self.indice_animacion]

        # Incrementa el índice de animación para avanzar en la animación
        self.indice_animacion += 1

        # Reinicia el índice de animación si supera la cantidad de imágenes
        if self.indice_animacion >= len(self.sprites_disparo_derecha):
            self.indice_animacion = 0

    def hacer_danio_enemigo(self, objetivo):
        # Implementa el método para hacer daño específico para los proyectiles del jugador
        pass
