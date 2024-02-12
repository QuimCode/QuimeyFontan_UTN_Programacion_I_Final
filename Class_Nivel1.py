##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from Parametros import *
from Personaje import *
from Class_Nivel import *

##---------------------------------##

class Nivel1(Nivel):
    def __init__(self, numero):
        super().__init__(numero)
        self.tiempo_fotograma = pygame.time.Clock()

    def posicion_X_Personaje(self):
        super().imprimir_posicion_personaje()

    def manejador_eventos_nivel1(self):
        super().manejador_eventos_nivel()

    def actualizar_nivel1(self):
        super().actualizar_nivel()

    def dibujar_nivel1(self):
        # for plataforma in self.plataformas:
        #     print(f"Plataforma - X: {plataforma.rect.x}, Y: {plataforma.rect.y}, Ancho: {plataforma.rect.width}, Alto: {plataforma.rect.height}")
        super().dibujar_nivel()


    def bucle_principal_nivel1(self):

        while True:
            self.manejador_eventos_nivel1()
            self.actualizar_nivel1()
            self.dibujar_nivel1()
            self.tiempo_fotograma.tick(60)
            pygame.time.delay(15)
            pygame.display.flip()

            self.posicion_X_Personaje()

# Ejecutar el nivel
    @staticmethod
    def ejecutar_nivel1():
        nivel1 = Nivel1(numero=1)
        nivel1.bucle_principal_nivel1()
        pygame.quit()  # Limpia Pygame y cierra la ventana
        sys.exit()
