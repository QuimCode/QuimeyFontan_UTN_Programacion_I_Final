##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from .Class_Nivel import *
from Game.Parametros import *
from ..Personajes.Personaje import *


##---------------------------------##

class Nivel2(Nivel):
    def __init__(self, numero):
        super().__init__(numero)
        self.tiempo_fotograma = pygame.time.Clock()

    def manejador_eventos_nivel2(self):
        super().manejador_eventos_nivel()

    def actualizar_nivel2(self):
        super().actualizar_nivel()

    def dibujar_nivel2(self):
        super().dibujar_nivel()


    def bucle_principal_nivel2(self):
        while True:
            self.manejador_eventos_nivel2()
            self.actualizar_nivel2()
            self.dibujar_nivel2()

            if self.verificar_transicion():
                print("Transición al siguiente nivel")
                return 3  # Indicamos que debe pasar al nivel 3

            self.tiempo_fotograma.tick(60)
            pygame.time.delay(20)
            pygame.display.flip()

# Ejecutar el nivel
    @staticmethod
    def ejecutar_nivel2():
        nivel2 = Nivel2(numero=2)
        next_level = nivel2.bucle_principal_nivel2()
        if next_level == 3:
            from .Class_Nivel3 import Nivel3
            return Nivel3.ejecutar_nivel3()
        return next_level
