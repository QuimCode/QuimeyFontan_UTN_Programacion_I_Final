##-------------MODULOS-------------##

import pygame

##-------------ARCHIVOS-------------##

from .Class_Nivel import *
from Game.Recursos.Parametros import *
from ..Personajes.Personaje import *


##---------------------------------##

class Nivel2(Nivel):
    def __init__(self, nombre_jugador, tiempo_restante, numero=2):
        super().__init__(tiempo_restante, nombre_jugador, numero)
        self.nombre_jugador = nombre_jugador
        self.tiempo_fotograma = pygame.time.Clock()

    def manejador_eventos_nivel2(self):
        super().manejador_eventos_nivel()

    def actualizar_nivel2(self):
        super().actualizar_nivel()

    def dibujar_nivel2(self):
        super().dibujar_nivel()

    def bucle_principal_nivel2(self):
        super().cargar_progreso_jugador()

        while True:
            self.manejador_eventos_nivel2()
            self.actualizar_nivel2()
            self.dibujar_nivel2()

            if self.verificar_transicion():
                self.finalizar_nivel()
                print("Transición al siguiente nivel")
                return self.tiempo_restante, 3  # Indicamos que debe pasar al nivel 3

            self.tiempo_fotograma.tick(60)
            pygame.time.delay(20)
            pygame.display.flip()

    @staticmethod
    def ejecutar_nivel2(nombre_jugador, tiempo_restante):
        nivel2 = Nivel2(nombre_jugador, tiempo_restante)
        tiempo_restante, next_level = nivel2.bucle_principal_nivel2()
        if next_level == 3:
            from .Class_Nivel3 import Nivel3
            return Nivel3.ejecutar_nivel3(nombre_jugador, tiempo_restante)
        return next_level

