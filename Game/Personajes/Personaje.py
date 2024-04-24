##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Game.Parametros import *
# from ..Recursos.Sprites.Sprites import *
from ..Recursos.Sprites.Sprites import *
from ..Recursos.Proyectiles.Proyectil import ProyectilJugador
import datetime


##--------------------------------##

instancia_sprite = estado_quieto(), estado_izquierda(), estado_derecha(), estado_saltando()
lista_proyectiles = []

class Personaje:
    def __init__(self, x, y, ancho, alto) -> None:
        # Definir una variable para almacenar el tiempo del último ataque
        self.ultimo_ataque_tiempo = datetime.datetime.now()

        # Definir un intervalo de tiempo mínimo entre ataques (en segundos)
        self.intervalo_ataque = 0.75  # Por ejemplo, 5 segundos

        # Composición
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect_ataque = pygame.Rect(x, y, ancho, alto)

        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

        # Cargar sprites para diferentes estados
        self.sprites_quieto = estado_quieto()
        self.sprites_quieto_izquierda = estado_quieto_izquerda()
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
        self.colisionando = True
        self.colisionando_abajo = True
        self.saltando = False
        self.ataque_reciente = False
        self.atacando = False
        self.moviendose_quieto = True
        self.ultimo_movimiento_izquierda = False
        self.movimidose_derecha = False
        self.movimiendose_izquierda = False

        # Estadísticas
        self.vida = 100
        self.escudo = 100
        self.energia = 100
        self.proyectiles = 3
        self.daño_ligero = 20
        self.daño_pesado = 40
        self.daño_proyectil = 50


    def movimiento_detener(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = True
        self.movimiendose_derecha = False
        self.movimiendose_izquierda = False
        self.velocidad_X = 0
        self.velocidad_Y = 0

    def movimiento_izquierda(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = False
        self.movimiendose_derecha = False
        self.movimiendose_izquierda = True
        self.ultimo_movimiento_izquierda = True
        self.velocidad_X = -5
        self.velocidad_Y = 0

    def movimiento_derecha(self):
        self.atacando = False
        self.saltando = False
        self.moviendose_quieto = False
        self.movimiendose_derecha = True
        self.movimiendose_izquierda = False
        self.ultimo_movimiento_izquierda = False
        self.velocidad_X = 5
        self.velocidad_Y = 0

    def movimiento_salto(self):
        # Verificar si el jugador está colisionando con una plataforma por debajo
        if self.colisionando_abajo:
            # Iniciar el salto solo si el jugador está en el suelo
            if not self.saltando:
                self.velocidad_salto = 10
                self.saltando = True
                self.colisionando = False
                self.colisionando_abajo = False
                print("Iniciando salto")
        else:
            # Si el jugador no está en contacto con una plataforma por debajo, no permitir el salto
            print("No se puede saltar mientras no se está en contacto con una plataforma por debajo")

        if self.saltando:
            # Aplicar la velocidad de salto
            if self.velocidad_salto >= -10:
                self.velocidad_Y = - (self.velocidad_salto * abs(self.velocidad_salto) * 0.67)
                self.velocidad_salto -= 1
            else:
                self.velocidad_salto = 10
                self.saltando = False
                self.colisionando = True
                self.colisionando_abajo = True
            print(f"ColisionandoPersonaje: ColiAbajo- {self.colisionando_abajo}, Saltando- {self.saltando}")


    def disparar_proyectil(self):
        # Verifica si hay suficientes proyectiles disponibles
        if self.proyectiles > 0:
            # Instancia un nuevo proyectil del jugador en la posición del personaje
            proyectil = ProyectilJugador(self.rect.x, self.rect.y, velocidad_x=5, velocidad_y=0)
            # Resta uno al contador de proyectiles
            self.proyectiles -= 1
            # Agrega el proyectil al grupo de sprites de los proyectiles del jugador
            # Imprime un mensaje indicando que se agregó el proyectil al grupo de sprites
            print("¡Disparo de jugador agregado al grupo de proyectiles del jugador!")
        else:
            print("¡No hay suficientes proyectiles disponibles!")

        if len(lista_proyectiles) > 0:
            print("Lista de proyectiles:", lista_proyectiles)
            print("Número de proyectiles en la lista:", len(lista_proyectiles))

    def provocar_daño_ligero(self):
        self.atacando = True
        self.saltando = False
        self.moviendose_quieto = False
        self.movimiendose_derecha = False
        self.movimiendose_izquierda = False



    def aplicar_gravedad(self):
        self.velocidad_Y -= self.gravedad
        self.rect.y += self.velocidad_Y

    # def aplicar_colisionar(self, plataformas, enemigos):
    #     tiempo_actual = datetime.datetime.now()
    #     colisiones_plataformas = pygame.sprite.spritecollide(self, plataformas, False)
    #     colisiones_enemigos = pygame.sprite.spritecollide(self, enemigos, False)

    #     # Definir los rectángulos de colisión para diferentes partes del personaje
    #     top_rect = self.rect.copy()
    #     top_rect.height = 1
    #     bottom_rect = self.rect.copy()
    #     bottom_rect.y += bottom_rect.height
    #     bottom_rect.height = 1
    #     left_rect = self.rect.copy()
    #     left_rect.width = 1
    #     right_rect = self.rect.copy()
    #     right_rect.x += right_rect.width
    #     right_rect.width = 1

    #     for plataforma in plataformas:
    #         if top_rect.colliderect(plataforma.rect) and self.velocidad_Y < 0:
    #             # Colisión desde abajo del personaje
    #             self.velocidad_Y = 0
    #             self.rect.top = plataforma.rect.bottom
    #             self.saltando = False
    #             self.colisionando = True


    #         elif bottom_rect.colliderect(plataforma.rect) and self.velocidad_Y >= 0:
    #             # Colisión desde arriba del personaje
    #             self.colisionando = True
    #             self.rect.bottom = plataforma.rect.top
    #             self.velocidad_Y = -1

    #     ataque_reciente = False

    #     for enemigo in colisiones_enemigos:
    #         tiempo_transcurrido = tiempo_actual - self.ultimo_ataque_tiempo

    #         # Verificar si ha pasado suficiente tiempo desde el último ataque
    #         if tiempo_transcurrido.total_seconds() >= self.intervalo_ataque:
    #             # Realizar el ataque
    #             # Resto del código para manejar la colisión con el enemigo y realizar el ataque ligero
    #             self.ultimo_ataque_tiempo = tiempo_actual  # Actualizar el tiempo del último ataque
                
    #             # Verificar si ya se ha realizado un ataque recientemente
    #             if not ataque_reciente:
    #                 # Llamar a la función ataque_ligero() del enemigo
    #                 enemigo.ataque_ligero(self)  # Aquí estás pasando el propio personaje como argumento

    #                 ataque_reciente = True

    #                 # Imprimir la vida del personaje después del ataque ligero
    #                 print("Vida del personaje después del ataque ligero:", self.vida)
    #                 print("Escudo del personaje después del ataque ligero:", self.escudo)


    def aplicar_limites(self, limites):
        # Aplicar límites para evitar que el personaje se escape de la ventana
        self.rect.x = max(limites[0], min(self.rect.x, limites[1] - self.rect.width))
        self.rect.y = max(limites[2], min(self.rect.y, limites[3] - self.rect.height))

    def actualizar_area_ataque(self):
        # Ajusta la posición y el tamaño del área de ataque según el estado del personaje
        # Por ejemplo, si el personaje está atacando hacia la derecha
        if self.atacando:
            if self.ultimo_movimiento_izquierda:
                # Si el personaje está mirando hacia la izquierda, ajusta el área de ataque a la izquierda del personaje
                self.rect_ataque.x = self.rect.x - self.rect_ataque.width
            else:
                # Si el personaje está mirando hacia la derecha, ajusta el área de ataque a la derecha del personaje
                self.rect_ataque.x = self.rect.x + self.rect.width

            # Ajusta la posición vertical y el tamaño del área de ataque según sea necesario
            self.rect_ataque.y = self.rect.y
            self.rect_ataque.height = self.rect.height

    def actualizar_personaje(self, limites=None):
        # Actualizar el área de ataque
        self.actualizar_area_ataque()

        # Actualizar la posición del personaje según la velocidad
        self.rect.x += self.velocidad_X
        self.aplicar_gravedad()

        # Obtener las animaciones correspondientes al estado del personaje
        if self.moviendose_quieto:
            animaciones = self.sprites_quieto if not self.ultimo_movimiento_izquierda else self.sprites_quieto_izquierda
        elif self.saltando:
            animaciones = self.sprites_saltando
        elif self.movimiendose_derecha:
            animaciones = self.sprites_derecha
        elif self.movimiendose_izquierda:
            animaciones = self.sprites_izquierda
        elif self.provocar_daño_ligero:
            animaciones = self.sprites_ataque_der if not self.ultimo_movimiento_izquierda else self.sprites_ataque_izq
        else:
            animaciones = [self.imagen]  # Lista con una sola imagen por defecto

        # Actualizar índice de sprite y obtener el sprite actual
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION:
            self.contador_animacion = 0
            self.indice_animacion += 1

            # Asegurarse de no exceder los límites de la lista de animaciones
            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            # Asignar la imagen actual del sprite al personaje
            self.imagen = animaciones[self.indice_animacion]


        # Aplicar límites si se proporcionan
        if limites:
            self.aplicar_limites(limites)


    def dibujar_en_pantalla(self, pantalla, offset_x=0):
        padding = 0
        # Dibuja al personaje en la pantalla
        pygame.draw.rect(pantalla, (0, 0, 0), (self.rect.x + offset_x - padding, self.rect.y - padding, self.rect.width + padding * 2, self.rect.height + padding * 2), 2)
        pantalla.blit(self.imagen, (self.rect.x + offset_x, self.rect.y)) 

        # Dibujar el área de ataque en la pantalla
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect_ataque)


    def get_posicion_x(self):
        return self.rect.x
