##-------------MODULOS-------------##

import pygame

##--------------------------------##

from Parametros import *
from Sprites import *
import datetime


##--------------------------------##

instancia_sprite = estado_quieto(), estado_izquierda(), estado_derecha(), estado_saltando()

class Personaje:
    def __init__(self, x, y, ancho, alto) -> None:


        # Definir una variable para almacenar el tiempo del último ataque
        self.ultimo_ataque_tiempo = datetime.datetime.now()

        # Definir un intervalo de tiempo mínimo entre ataques (en segundos)
        self.intervalo_ataque = 0.75  # Por ejemplo, 5 segundos

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
        ataque_reciente = False
        self.atacando = False
        self.moviendose_quieto = True
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

        Enemigo

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

    def aplicar_colisionar(self, plataformas, enemigos):
        tiempo_actual = datetime.datetime.now()
        colisiones_plataformas = pygame.sprite.spritecollide(self, plataformas, False)
        colisiones_enemigos = pygame.sprite.spritecollide(self, enemigos, False)

        for plataforma in colisiones_plataformas:
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
                # Colisión en el lado derecho
                if self.rect.left >= plataforma.rect.right:
                    self.velocidad_X = 0
                    self.rect.x = plataforma.rect.right
            elif self.velocidad_X < 0:
                # Colisión en el lado izquierdo
                if self.rect.right <= plataforma.rect.left:
                    self.velocidad_X = 0
                    self.rect.x = plataforma.rect.left

        ataque_reciente = False

        for enemigo in colisiones_enemigos:
            tiempo_transcurrido = tiempo_actual - self.ultimo_ataque_tiempo

            # Verificar si ha pasado suficiente tiempo desde el último ataque
            if tiempo_transcurrido.total_seconds() >= self.intervalo_ataque:
                # Realizar el ataque
                # Resto del código para manejar la colisión con el enemigo y realizar el ataque ligero
                self.ultimo_ataque_tiempo = tiempo_actual  # Actualizar el tiempo del último ataque
                
                # Verificar si ya se ha realizado un ataque recientemente
                if not ataque_reciente:
                    # Manejar colisiones laterales entre el personaje y el enemigo
                    # if self.rect.right >= enemigo.rect.left:  # Colisión en el lado izquierdo del personaje
                    #     # self.rect.right = enemigo.rect.left  # Ajustar la posición del personaje

                    # elif self.rect.left <= enemigo.rect.right:  # Colisión en el lado derecho del personaje
                    #     self.rect.left = enemigo.rect.right  # Ajustar la posición del personaje

                    # Llamar a la función ataque_ligero() del enemigo
                    enemigo.ataque_ligero(self)  # Aquí estás pasando el propio personaje como argumento

                    # Marcar que se ha realizado un ataque recientemente
                    ataque_reciente = True

                    # Imprimir la vida del personaje después del ataque ligero
                    print("Vida del personaje después del ataque ligero:", self.vida)
                    print("Escudo del personaje después del ataque ligero:", self.escudo)


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


    def ataque_ligero(self, objetivo):
        if objetivo.escudo > 0:
            objetivo.escudo -= self.daño_ligero_enemigo
        else:
            objetivo.vida -= self.daño_ligero_enemigo

        # Asegurarse de que la vida y el escudo no sean negativos
        objetivo.vida = max(objetivo.vida, 0)
        objetivo.escudo = max(objetivo.escudo, 0)