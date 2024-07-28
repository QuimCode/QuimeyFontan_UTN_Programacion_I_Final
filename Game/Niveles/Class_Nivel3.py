##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from .Class_Nivel import *
from ..Personajes.Personaje import *
from Game.Recursos.Parametros import *


##---------------------------------##

class Nivel3(Nivel):
    def __init__(self, nombre_jugador, tiempo_restante, numero=3):
        super().__init__(tiempo_restante, nombre_jugador, numero)
        self.nombre_jugador = nombre_jugador
        self.tiempo_fotograma = pygame.time.Clock()

    def manejador_eventos_nivel3(self):
        super().manejador_eventos_nivel()

    def actualizar_nivel3(self):
        super().actualizar_nivel()

    def dibujar_nivel3(self):
        super().dibujar_nivel()

    def bucle_principal_nivel3(self):
        super().cargar_progreso_jugador()

        while True:
            self.manejador_eventos_nivel3()
            self.actualizar_nivel3()
            self.dibujar_nivel3()

            if self.verificar_transicion():
                self.finalizar_nivel()
                print("Transición al siguiente nivel")
                from Game.Recursos.Dependencias import crear_instancia_de_JuegoGanado
                juegoGanadoMenu = crear_instancia_de_JuegoGanado()
                juegoGanadoMenu.run()
        
            self.tiempo_fotograma.tick(60)
            pygame.time.delay(20)
            pygame.display.flip()

    @staticmethod
    def ejecutar_nivel3(nombre_jugador, tiempo_restante):
        nivel3 = Nivel3(nombre_jugador, tiempo_restante)
        nivel3.bucle_principal_nivel3()
        pygame.quit()  # Limpio Pygame y cierra la ventana
        sys.exit()
