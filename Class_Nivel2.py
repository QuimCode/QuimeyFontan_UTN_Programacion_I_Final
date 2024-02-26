##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from Class_Nivel import *
from Parametros import *
from Personaje import *


##---------------------------------##

class Nivel2(Nivel):
    def __init__(self, numero):
        super().__init__(numero)
        self.tiempo_fotograma = pygame.time.Clock()

    def manejador_eventos_nivel1(self):
        super().manejador_eventos_nivel()

    def actualizar_nivel1(self):
        super().actualizar_nivel()

    def dibujar_nivel1(self):
        super().dibujar_nivel()


    def bucle_principal_nivel2(self):
        while True:
            self.manejador_eventos_nivel1()
            self.actualizar_nivel1()
            self.dibujar_nivel1()
            self.tiempo_fotograma.tick(60)
            pygame.time.delay(15)
            pygame.display.flip()

# Ejecutar el nivel
    @staticmethod
    def ejecutar_nivel2():
        nivel2 = Nivel2(numero=2)
        nivel2.bucle_principal_nivel2()
        pygame.quit()  # Limpia Pygame y cierra la ventana
        sys.exit()
