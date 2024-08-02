#-------------------- IMPORTACIONES ----------------#

import pygame
import sys


#-------------------- INICIALIZACION ----------------#

pygame.init()

#-------------------- CLASE-MENU ----------------#

class MenuPadre:
    def __init__(self, pantalla) -> None:
        self.ventana = pantalla
        self.botones_menu = []
        self.selected_