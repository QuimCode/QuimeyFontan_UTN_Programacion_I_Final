import pygame
import random
from ..Recursos.Proyectiles.Proyectil import ProyectilEnemigo
from ..Recursos.Sprites.Enemy_Sprites import *
from ..Recursos.Sprites.EneVoladorSpri import *
from ..Recursos.Sprites.EneMagoSpri import *

from Game.Parametros import *
from ..Recursos.Sprites.Sprites import *

lista_proyectiles = []

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho = 100, alto = 90):
        super().__init__()
        # Crear el sprite del enemigo
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect.x = x
        self.rect.y = y
        self.ancho = ancho
        self.alto = alto

        # Estadísticas
        self.vida_enemigo = 100
        self.escudo_enemigo = 100
        self.energia_enemigo = 100
        self.proyectiles_enemigo = 3
        self.daño_ligero_enemigo = 20
        self.daño_pesado_enemigo = 40
        self.daño_proyectil_enemigo = 50

        # Velocidades iniciales
        self.velocidad_X = 0
        self.velocidad_Y = 0

        self.gravedad = 1  # Ajusta la gravedad según la necesidad del juego

        self.indice_animacion = 0
        self.contador_animacion = 0
        self.velocidad_animacion = 8  # Ajusta esto para cambiar la velocidad de la animación

        # Definir las animaciones del enemigo
        self.sprites_quieto = estado_quieto_enemigo()
        self.sprites_izquierda = estado_izquierda_enemigo()
        self.sprites_derecha = estado_derecha_enemigo()
        self.sprite_ataque = estado_ataque_enemigo()
        self.image = self.sprites_quieto[0]

        # Bandera para la dirección actual del enemigo
        self.direccion = 'derecha'  # Inicialmente el enemigo mira hacia la derecha



    def actualizar_enemigo(self, limites=None):
        self.velocidad_Y += self.gravedad

        # Generar movimientos aleatorios en ambas direcciones X e Y
        movimiento_aleatorio = random.randint(1, 100)
        if movimiento_aleatorio == 1:  
            self.velocidad_X = random.choice([-5, 5])  
            self.velocidad_Y = random.choice([-15, -10])
        elif movimiento_aleatorio == 2:  # Probabilidad menor para que se queden quietos
            self.velocidad_X = 0
            self.velocidad_Y = 0

        if self.velocidad_X < 0:
            self.direccion = 'izquierda'
        elif self.velocidad_X > 0:
            self.direccion = 'derecha'
        else:
            self.direccion = 'quieto'

        # Definir las animaciones según la dirección actual del enemigo
        if self.direccion == "derecha":
            animaciones = self.sprites_derecha
        elif self.direccion == "izquierda":
            animaciones = self.sprites_izquierda    
        else:
            animaciones = self.sprites_quieto

        # Actualizar la posición del enemigo según la velocidad en ambas direcciones
        self.rect.x += self.velocidad_X
        self.rect.y += self.velocidad_Y

        # Aplicar límites si se proporcionan
        if limites:
            self.aplicar_limites(limites)

        # Incrementar el contador de animación
        self.contador_animacion += 1

        # Lógica para cambiar de sprite y controlar la velocidad de la animación
        if self.contador_animacion >= self.velocidad_animacion:
            self.contador_animacion = 0
            self.indice_animacion += 1

            # Reiniciar el índice de animación si es mayor que la longitud de la lista de animaciones
            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            # Actualizar la imagen actual
            self.image = animaciones[self.indice_animacion]

    def aplicar_limites(self, limites):
        # Aplicar límites para evitar que el enemigo se escape de la ventana
        self.rect.x = max(limites[0], min(self.rect.x, limites[1] - self.rect.width))
        self.rect.y = max(limites[2], min(self.rect.y, limites[3] - self.rect.height))

    def dibujar_en_pantalla(self, pantalla):
        # Dibujar el rectángulo de colisión (opcional)
        pygame.draw.rect(pantalla, ROJO, self.rect, 2)

        # Calcular el offset para centrar la imagen dentro del rectángulo de colisión
        offset_x = (self.rect.width - self.ancho) / 2
        offset_y = (self.rect.height - self.alto) / 2

        # Dibujar la imagen del enemigo centrada dentro del rectángulo de colisión
        pantalla.blit(self.image, (self.rect.x + offset_x, self.rect.y + offset_y))

    def ataque_ligero(self, objetivo):
        if objetivo.escudo > 0:
            objetivo.escudo -= self.daño_ligero_enemigo
        else:
            objetivo.vida -= self.daño_ligero_enemigo

        objetivo.vida = max(objetivo.vida, 0)
        objetivo.escudo = max(objetivo.escudo, 0)

class EnemigoVolador(Enemigo):
    def __init__(self, x, y, ancho=100, alto=90):
        super().__init__(x, y, ancho, alto)

        self.velocidad_animacion = 10

        self.sprites_quieto_volador = estado_quieto_enemigo_volador()
        self.sprites_derecha_volador = estado_derecha_enemigo_volador()
        self.sprites_izquierda_volador = estado_izquierda_enemigo_volador()
        self.image = self.sprites_quieto_volador[0]

        # Inicializar la dirección del enemigo volador
        self.direccion_vuelo = 'derecha'  # Empezar volando hacia la derecha

    def actualizar_enemigo(self, limites=None):
        # Generar movimientos aleatorios en la dirección X
        movimiento_aleatorio = random.randint(1, 100)
        if movimiento_aleatorio == 1:  
            self.velocidad_X = random.choice([-5, 5])

        # Actualizar la posición del enemigo solo en el eje X
        self.rect.x += self.velocidad_X

        # Aplicar límites si se proporcionan y cambiar de dirección si toca los límites
        if limites:
            if self.rect.left <= limites[0] or self.rect.right >= limites[1]:
                # Cambiar la dirección del enemigo
                self.velocidad_X *= -1

        # Actualizar la imagen actual según la dirección del enemigo
        if self.velocidad_X > 0:
            # Usar sprite volando hacia la derecha
            self.image = self.sprites_derecha_volador[self.indice_animacion]
        elif self.velocidad_X < 0:
            # Usar sprite volando hacia la izquierda
            self.image = self.sprites_izquierda_volador[self.indice_animacion]
        else:
            # Usar sprite de enemigo quieto
            self.image = self.sprites_quieto_volador[self.indice_animacion]

        # Incrementar el contador de animación
        self.contador_animacion += 1

        # Lógica para cambiar de sprite y controlar la velocidad de la animación
        if self.contador_animacion >= self.velocidad_animacion:
            self.contador_animacion = 0
            self.indice_animacion += 1

            # Reiniciar el índice de animación si es mayor que la longitud de la lista de animaciones
            if self.indice_animacion >= len(self.sprites_quieto_volador):
                self.indice_animacion = 0

class EnemigoMago(Enemigo):
    def __init__(self, x, y, direccion_inicial='derecha', ancho=100, alto=90):
        super().__init__(x, y, ancho, alto)

        self.ticks_ultima_disparo = 0
        self.intervalo_disparo = 3000  # Intervalo de tiempo entre disparos (en milisegundos)
        self.max_disparos = 5  # Número máximo de disparos por ráfaga

        # Definir las animaciones del mago
        self.sprites_quietoD_mago = estado_quietoD_enemigo_mago()
        self.sprites_quietoI_mago = estado_quietoI_enemigo_mago()
        self.sprite_muriendo_mago = estado_muerto_enemigo_mago()
        self.sprites_ataque_derecha_mago = estado_ataque_derecha_enemigo_mago()
        self.sprites_ataque_izquierda_mago = estado_ataque_izquierda_enemigo_mago()

        self.velocidad_animacion = 10  # Ajusta este valor según la velocidad deseada
        self.direccion_actual = direccion_inicial  # Almacena la dirección actual del mago

        # Inicializar la imagen del mago según la dirección inicial
        if direccion_inicial == 'derecha':
            self.image = self.sprites_quietoD_mago[0]  # La primera imagen de la animación
            self.direccion_ataque = 'derecha'
        else:
            self.image = self.sprites_quietoI_mago[0]  # La primera imagen de la animación
            self.direccion_ataque = 'izquierda'

        self.indice_animacion_quieto = 0
        self.ticks_animacion = 0  # Contador para controlar la velocidad de la animación

    def disparar(self):
        # Instancia un nuevo proyectil enemigo desde la posición del enemigo
        proyectil_enemigo = ProyectilEnemigo(self.rect.centerx, self.rect.bottom, velocidad_x=5, velocidad_y=0)
        # Agrega el proyectil a la lista de proyectiles del juego
        lista_proyectiles.append(proyectil_enemigo)

    def animar_reposo(self):
        # Método para manejar la animación de reposo del mago
        self.ticks_animacion += 1

        # Verifica si ha pasado suficiente tiempo para cambiar de fotograma
        if self.ticks_animacion >= self.velocidad_animacion:
            if self.direccion_actual == 'derecha':
                self.image = self.sprites_quietoD_mago[self.indice_animacion_quieto]
            else:
                self.image = self.sprites_quietoI_mago[self.indice_animacion_quieto]

            self.indice_animacion_quieto += 1
            self.ticks_animacion = 0

            # Reinicia el índice de animación si supera la cantidad de imágenes
            if self.indice_animacion_quieto >= len(self.sprites_quietoD_mago):
                self.indice_animacion_quieto = 0

    def actualizar_enemigo(self, limites=None):
        # No hay movimiento para el mago, solo dispara
        self.animar_reposo()

    def dibujar_en_pantalla(self, pantalla):
        # Dibujar el rectángulo de colisión (opcional)
        pygame.draw.rect(pantalla, ROJO, self.rect, 2)

        # Calcular el offset para centrar la imagen dentro del rectángulo de colisión
        offset_x = (self.rect.width - self.ancho) / 2
        offset_y = (self.rect.height - self.alto) / 2

        # Dibujar la imagen del mago centrada dentro del rectángulo de colisión
        pantalla.blit(self.image, (self.rect.x + offset_x, self.rect.y + offset_y))

