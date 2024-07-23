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
    def __init__(self, x, y, ancho=100, alto=100) -> None:
        # Definir una variable para almacenar el tiempo del último ataque
        self.ultimo_ataque_tiempo = datetime.datetime.now()

        # Definir un intervalo de tiempo mínimo entre ataques (en segundos)
        self.intervalo_ataque = 0.75  # Por ejemplo, 5 segundos

        # Composición
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.rect_ataque = pygame.Rect(x, y, ancho, alto)
        self.rect.x = x 
        self.rect.y = y 
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
        self.intervalo_inmunidad = 600 
        self.grupo_proyectiles = pygame.sprite.Group()

        # Velocidades iniciales
        self.velocidad_X = 0
        self.velocidad_Y = 0
        self.gravedad = -6
        self.velocidad_salto = 0

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
        self.intentos = 3
        self.vida = 100
        self.vida_maxima = 100
        self.escudo = 100
        self.proyectiles = 20
        self.ultimo_daño_tiempo = 0
        self.daño_proyectil = 20

#-------------------#### MOVIMIENTO #-------------------####

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
                self.velocidad_salto = 8  # Ajustar este valor para cambiar la altura del salto
                self.saltando = True
                self.colisionando = False
                self.colisionando_abajo = False
                print("Iniciando salto")
        else:
            # Si el jugador no está en contacto con una plataforma por debajo, no permitir el salto
            print("No se puede saltar mientras no se está en contacto con una plataforma por debajo")

        if self.saltando:
            # Aplicar la velocidad de salto
            if self.velocidad_salto >= -2:
                self.velocidad_Y = - (self.velocidad_salto * abs(self.velocidad_salto) * 0.67)
                self.velocidad_salto -= 1
            else:
                self.velocidad_salto = 1
                self.saltando = False
                self.colisionando = True
                self.colisionando_abajo = True
            print(f"Colisionando Personaje: Colision desde abajo- {self.colisionando_abajo}, Saltando- {self.saltando}")


#-------------------#### APLICACION #-------------------####

    def aplicar_gravedad(self):
        self.velocidad_Y -= self.gravedad
        self.rect.y += self.velocidad_Y

    def aplicar_limites(self, limites):
        # Aplicar límites para evitar que el personaje se escape de la ventana
        self.rect.x = max(limites[0], min(self.rect.x, limites[1] - self.rect.width))
        self.rect.y = max(limites[2], min(self.rect.y, limites[3] - self.rect.height))

    def aplicar_daño_enemigo(self, enemigos):
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):
                if self.rect.bottom > enemigo.rect.top and self.rect.top < enemigo.rect.bottom:
                    enemigo.vida_enemigo -= 100
                    print(f"El jugador hizo daño al enemigo. Vida del enemigo: {enemigo.vida_enemigo}")

    def disparar_proyectil(self):
        # Verifica si hay suficientes proyectiles disponibles
        if self.proyectiles > 0:
            # Instancia un nuevo proyectil del jugador en la posición del personaje
            proyectil = ProyectilJugador(self.rect.centerx, self.rect.centery, velocidad_x=5 if not self.ultimo_movimiento_izquierda else -5, velocidad_y=0)
            self.grupo_proyectiles.add(proyectil)
            self.proyectiles -= 1
            print("¡Disparo de jugador agregado al grupo de proyectiles del jugador!")
        else:
            print("¡No hay suficientes proyectiles disponibles!")

    def aplicar_morir(self):
        if self.vida <= 0:
            self.intentos -= 1
            print(f"El personaje ha muerto. Intentos restantes: {self.intentos}")
            if self.intentos > 0:
                self.vida = 100
                self.escudo = 100
                self.energia = 100
                self.rect.x = 10
                self.rect.y = 650
                self.velocidad_X = 0
                self.velocidad_Y = 0
                self.saltando = False
                self.colisionando = True
                self.colisionando_abajo = True
            else:
                print("Game Over")
                from ..Recursos.Dependencias import crear_instancia_de_gameover
                gameOverMenu = crear_instancia_de_gameover()
                gameOverMenu.run()
                # funcion()

    def regresar_al_menu(self, nombre):
        # Importar la clase del submenu aquí dentro del método jugar
        from ..Recursos.Dependencias import crear_instancia_de_submenu
        submenu = crear_instancia_de_submenu(nombre)
        submenu.run()

    # def provocar_daño_ligero(self):
    #     self.atacando = True
    #     self.saltando = False
    #     self.moviendose_quieto = False
    #     self.movimiendose_derecha = False
    #     self.movimiendose_izquierda = False

#-------------------#### COLISION #-------------------####


    def colisionar_horizontal(self, lista_plataforma):
        # Reiniciar los estados de colisión
        self.colisionando = False

        # Manejar colisiones horizontales
        for plataforma in lista_plataforma:
            if plataforma.rect.colliderect(self.rect):
                # Colisiones desde la derecha
                if self.velocidad_X > 0 and self.rect.right + 6 >= plataforma.rect.left:
                    self.rect.right = plataforma.rect.left
                    # print("Colisionando derecha")
                    self.velocidad_X = 0
                # Colisiones desde la izquierda
                elif self.velocidad_X < 0 and self.rect.left - 6 <= plataforma.rect.right:
                    self.rect.left = plataforma.rect.right
                    # print("Colisionando izquierda")
                    self.velocidad_X = 0
                self.colisionando = True

        # Actualizar la posición real del personaje
        self.rect.x = self.rect.x

    def colisionar_vertical(self, lista_plataforma):
        # Reiniciar los estados de colisión
        self.colisionando_abajo = False

        # Manejar colisiones verticales
        for plataforma in lista_plataforma:
            if plataforma.rect.colliderect(self.rect):
                if self.velocidad_Y > 0:  # Moviendo hacia abajo
                    self.rect.bottom = plataforma.rect.top
                    self.saltando = False
                    self.colisionando_abajo = True
                elif self.velocidad_Y < 0:  # Moviendo hacia arriba
                    self.rect.top = plataforma.rect.bottom
                self.velocidad_Y = 0
                # print("Colisionando arriba o abajo")

        # Actualizar la posición real del personaje
        self.rect.y = self.rect.y

#-------------------#### COLISION-DAÑO #-------------------####

    def recibir_daño(self, proyectiles, enemigos, trampas):
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.ultimo_daño_tiempo < self.intervalo_inmunidad:
                return

            # Verificar colisiones con proyectiles enemigos
            for proyectil in proyectiles:
                if self.rect.colliderect(proyectil.rect):
                    self.aplicar_daño(proyectil.daño)
                    proyectiles.remove(proyectil)
                    print(f"Recibió daño de proyectil. Vida: {self.vida}, Escudo: {self.escudo}")
                    self.ultimo_daño_tiempo = tiempo_actual
                    break

            # Verificar colisiones con enemigos
            for enemigo in enemigos:
                if self.rect.colliderect(enemigo.rect):
                    # Verificar individualmente cada lado de la colisión
                    if self.rect.bottom > enemigo.rect.top:  # Colisión desde abajo
                        self.aplicar_daño(enemigo.daño_ligero_enemigo)  # Aplicar daño lateral
                        print(f"Recibió daño de enemigo por el lado. Vida: {self.vida}, Escudo: {self.escudo}")
                        self.ultimo_daño_tiempo = tiempo_actual
                        break
                    elif self.rect.top < enemigo.rect.bottom:  # Colisión desde arriba
                        self.aplicar_daño_enemigo(enemigos)
                        continue
                    elif self.rect.right < enemigo.rect.left:  # Colisión desde la izquierda
                        # Manejar colisión desde la izquierda
                        self.aplicar_daño(enemigo.daño_ligero_enemigo)
                        print(f"Recibió daño de enemigo por el lado izquierdo. Vida: {self.vida}, Escudo: {self.escudo}")
                        self.ultimo_daño_tiempo = tiempo_actual
                        break
                    elif self.rect.left > enemigo.rect.right:  # Colisión desde la derecha
                        # Manejar colisión desde la derecha
                        self.aplicar_daño(enemigo.daño_ligero_enemigo)
                        print(f"Recibió daño de enemigo por el lado derecho. Vida: {self.vida}, Escudo: {self.escudo}")
                        self.ultimo_daño_tiempo = tiempo_actual
                        break

            # Verificar colisiones con trampas
            for trampa in trampas:
                if self.rect.colliderect(trampa.rect):
                    self.aplicar_daño(trampa.daño)
                    print(f"Recibió daño de trampa. Vida: {self.vida}, Escudo: {self.escudo}")
                    self.ultimo_daño_tiempo = tiempo_actual
                    break



    def provocar_daño(self, objetivo, lista_proyectiles):
            
            for proyectil in lista_proyectiles:
                if proyectil.rect.colliderect(objetivo.rect):
                    if self.velocidad_X > 0:
                        # El enemigo se mueve hacia la derecha, el proyectil lo golpea desde la izquierda
                        proyectil.rect.right = objetivo.rect.left
                        objetivo.vida_enemigo -= 100
                    elif self.velocidad_X < 0:
                        # El enemigo se mueve hacia la izquierda, el proyectil lo golpea desde la derecha
                        proyectil.rect.left = objetivo.rect.right
                        objetivo.vida_enemigo -= 100

                    # Reducir la vida del enemigo por el impacto del proyectil
                    print(f"El jugador hizo daño al enemigo. Vida del enemigo: {self.vida_enemigo}")

    def aplicar_daño(self, daño):
        if self.escudo > 0:
            self.escudo -= daño
            if self.escudo < 0:
                self.vida += self.escudo  # Si el escudo es negativo, se resta de la vida
                self.escudo = 0
        else:
            self.vida -= daño

        # Asegurarse de que los valores no sean negativos
        self.vida = max(self.vida, 0)
        self.escudo = max(self.escudo, 0)

#-------------------#### ACTUALIZACION #-------------------####

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

    def actualizar_personaje(self, lista_plataformas, lista_proyectiles, lista_enemigos, lista_trampas, limites=None):
        # Actualizar el área de ataque
        # self.recibir_daño(lista_proyectiles, lista_enemigos, lista_trampas)
        self.actualizar_area_ataque()

        self.rect.x += self.velocidad_X
        self.colisionar_horizontal(lista_plataformas)  # Colisiones horizontales

        self.rect.y += self.velocidad_Y
        self.aplicar_gravedad()
        self.colisionar_vertical(lista_plataformas)  # Colisiones verticales

        self.recibir_daño(lista_proyectiles, lista_enemigos, lista_trampas)
        self.provocar_daño(lista_enemigos, lista_proyectiles)
        self.aplicar_daño_enemigo(lista_enemigos)

        # self.aplicar_morir(funcion=self.regresar_al_menu(nombre="-Usuario No Registrado-"))
        self.aplicar_morir()

        # Obtener las animaciones correspondientes al estado del personaje
        if self.moviendose_quieto:
            animaciones = self.sprites_quieto if not self.ultimo_movimiento_izquierda else self.sprites_quieto_izquierda
        elif self.saltando:
            animaciones = self.sprites_saltando
        elif self.movimiendose_derecha:
            animaciones = self.sprites_derecha
        elif self.movimiendose_izquierda:
            animaciones = self.sprites_izquierda
        # elif self.provocar_daño_ligero:
        #     animaciones = self.sprites_ataque_der if not self.ultimo_movimiento_izquierda else self.sprites_ataque_izq
        else:
            animaciones = [self.imagen]  # Lista con una sola imagen por defecto

        # actualizo indice
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION:
            self.contador_animacion = 0
            self.indice_animacion += 1

            # no exederme con los límites de la lista de animaciones
            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            self.imagen = animaciones[self.indice_animacion]

        if limites:
            self.aplicar_limites(limites)

        self.grupo_proyectiles.update()

    def dibujar_en_pantalla(self, pantalla):
        pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 2)
        pantalla.blit(self.imagen, self.rect)
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect_ataque)

        # Dibujar proyectiles
        for proyectil in self.grupo_proyectiles:
            proyectil.dibujar(pantalla)

    def get_posicion_x(self):
        return self.rect.x
