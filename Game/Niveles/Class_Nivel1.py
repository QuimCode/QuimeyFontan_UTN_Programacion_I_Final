##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from .Class_Nivel import *
from Game.Parametros import *
from ..Personajes.Personaje import *

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
        super().dibujar_nivel()

    def finalizar_nivel(self):
        nombre_usuario = nombre_jugador_global  # Aquí debes obtener el nombre del jugador real
        archivo_csv = "datos_jugadores.csv"  # Ruta al archivo CSV
        estadisticas = self.obtener_estadisticas()
        guardar_estadisticas_al_final_del_nivel(nombre_usuario== nombre_jugador_global, archivo_csv, 
            estadisticas["Intentos"], estadisticas["Vida"], estadisticas["Escudo"], estadisticas["Proyectil"], estadisticas["Puntaje"])
        print("Estadísticas guardadas al final del nivel")

    def bucle_principal_nivel1(self):
        while True:
            self.manejador_eventos_nivel1()
            self.actualizar_nivel1()
            self.dibujar_nivel1()

            if self.verificar_transicion():
                self.finalizar_nivel()
                print("Transición al siguiente nivel")
                return 2  # Indicamos que debe pasar al nivel 2

            self.tiempo_fotograma.tick(60)
            pygame.time.delay(20)
            pygame.display.flip()

            # self.posicion_X_Personaje()

# Ejecutar el nivel
    @staticmethod
    def ejecutar_nivel1():
        nivel1 = Nivel1(numero=1)
        next_level = nivel1.bucle_principal_nivel1()
        if next_level == 2:
            from .Class_Nivel2 import Nivel2
            return Nivel2.ejecutar_nivel2()
        return next_level
