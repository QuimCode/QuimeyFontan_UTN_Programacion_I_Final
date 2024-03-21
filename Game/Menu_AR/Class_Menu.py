import pygame
import sys
import csv
import datetime

from ..Niveles.Class_Nivel import *
from ..Niveles.Class_Nivel2 import *
from ..Niveles.Class_Nivel3 import *
from ..Parametros import *

nombre_global = "---"

class Boton:
    def __init__(self, x, y, ANCHO_MENU, ALTO_MENU, color_normal, color_hover, texto, font, action=None):
        self.rect = pygame.Rect(x, y, ANCHO_MENU, ALTO_MENU)
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.texto = texto
        self.font = font
        self.action = action
        self.hover = False

    def update(self, screen):
        color = self.color_hover if self.hover else self.color_normal
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.texto, True, BLANCO)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hover:
            if self.action:
                self.action()

class Menu:
    def __init__(self, nombre):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Menú del juego")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        # Cargar la imagen del fondo del menú
        self.fondo_menu = pygame.image.load("Mapas_Fondos/Menu/castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()

        self.nombre_capturado = nombre
        self.nombre_usuario = self.nombre_capturado

        self.botones = []
        self.create_buttons()

    def create_buttons(self):
        # Definir los botones del menú
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 50, 200, 50, AZUL, VERDE, "Jugar", self.font, self.jugar))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 50, 200, 50, AZUL, VERDE, "Salir", self.font, self.salir))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for boton in self.botones:
                    boton.handle_event(event)

            # Dibujar el fondo del menú
            self.screen.blit(self.fondo_menu, (0, 0))

            for boton in self.botones:
                boton.update(self.screen)

            # Mostrar el nombre de usuario en la esquina superior izquierda
            nombre_texto = self.font.render("Usuario: " + self.nombre_usuario, True, BLANCO)
            self.screen.blit(nombre_texto, (20, 20))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def jugar(self):
        submenu = Submenu(self.nombre_usuario)
        submenu.run()

    def salir(self):
        pygame.quit()
        sys.exit()

class Submenu:
    def __init__(self, nombre):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Submenú")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        self.fondo_menu = pygame.image.load("Mapas_Fondos/Menu/castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()

        self.nombre_cap = nombre
        self.nombre_usuario = self.nombre_cap

        self.botones = []
        self.create_buttons()

    def create_buttons(self):
        # Definir los botones del submenú
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 150, 200, 50, AZUL, VERDE, "Menu", self.font, self.jugar))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 50, 200, 50, AZUL, VERDE, "Registro", self.font, self.registro))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 50, 200, 50, AZUL, VERDE, "Jugar Nivel 1", self.font, self.jugar_nivel_1))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 150, 200, 50, AZUL, VERDE, "Jugar Nivel 2", self.font, self.jugar_nivel_2))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 250, 200, 50, AZUL, VERDE, "Jugar Nivel 3", self.font, self.jugar_nivel_3))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for boton in self.botones:
                    boton.handle_event(event)

            # Dibujar el fondo del menú
            self.screen.blit(self.fondo_menu, (0, 0))
            
            for boton in self.botones:
                boton.update(self.screen)

            # Mostrar el nombre de usuario en la esquina superior izquierda
            nombre_texto = self.font.render("Usuario: " + self.nombre_usuario, True, BLANCO)
            self.screen.blit(nombre_texto, (20, 20))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def registro(self):
        submenu_registro = SubmenuRegistro(self)
        submenu_registro.run()
        # Actualizar el nombre de usuario después de que se complete el registro
        self.nombre_usuario = submenu_registro.nombre

    def jugar(self):
        menu = Menu(self.nombre_usuario)
        menu.run()
        print("Volviendo a Menu...")

    def jugar_nivel_1(self):
        if self.nombre_usuario:
            Nivel1.ejecutar_nivel1()
            print("Iniciar nivel 1...")
        else:
            print("Por favor, registra un usuario antes de jugar.")

    def jugar_nivel_2(self):
        if self.nombre_usuario:
            Nivel2.ejecutar_nivel2()
            print("Iniciar nivel 2...")
        else:
            print("Por favor, registra un usuario antes de jugar.")

    def jugar_nivel_3(self):
        if self.nombre_usuario:
            Nivel3.ejecutar_nivel3()
            print("Iniciar nivel 3...")
        else:
            print("Por favor, registra un usuario antes de jugar.")



class SubmenuRegistro:
    def __init__(self, submenu):
        self.Submenu = submenu
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Registro de Jugador")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        self.fondo_menu = pygame.image.load("Mapas_Fondos/Menu/castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()

        # self.nombre_jugador = ""
        self.nombre = ""
        self.fecha = ""
        self.puntos = 0
        self.input_nombre = pygame.Rect(ANCHO_MENU/2 - 150, ALTO_MENU/2 - 100, 300, 50)
        self.input_fecha = pygame.Rect(ANCHO_MENU/2 - 150, ALTO_MENU/2, 300, 50)

        self.nombre_activo = True  # Variable para controlar el estado activo del campo de nombre
        self.fecha_activo = False  # Variable para controlar el estado activo del campo de fecha

        self.botones = []
        self.create_buttons()

    def create_buttons(self):
        # Botón para continuar después de ingresar los datos
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU - 100, 200, 50, AZUL, VERDE, "Continuar", self.font, self.continuar))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Cambiar el estado activo del campo de entrada
                        if self.nombre_activo:
                            self.nombre_activo = False
                            self.fecha_activo = True
                        elif self.fecha_activo:
                            self.fecha_activo = False
                    elif event.key == pygame.K_TAB:  # Cambiar de un campo de entrada a otro al presionar Tab
                        if self.nombre_activo:
                            self.nombre_activo = False
                            self.fecha_activo = True
                        elif self.fecha_activo:
                            self.fecha_activo = False
                            self.nombre_activo = True
                    elif self.nombre_activo:  # Capturar entrada de texto para el campo de nombre
                        if event.key == pygame.K_BACKSPACE:
                            self.nombre = self.nombre[:-1]
                        else:
                            self.nombre += event.unicode
                    elif self.fecha_activo:  # Capturar entrada de texto para el campo de fecha
                        if event.key == pygame.K_BACKSPACE:
                            self.fecha = self.fecha[:-1]
                        else:
                            self.fecha += event.unicode

                # Manejar eventos de los botones
                for boton in self.botones:
                    boton.handle_event(event)

            # Dibujar el fondo del menú
            self.screen.blit(self.fondo_menu, (0, 0))

            # Dibujar campos de entrada y texto
            pygame.draw.rect(self.screen, BLANCO if self.nombre_activo else AZUL, self.input_nombre, 2)
            pygame.draw.rect(self.screen, BLANCO if self.fecha_activo else AZUL, self.input_fecha, 2)

            nombre_texto = self.font.render("Nombre:", True, BLANCO)
            fecha_texto = self.font.render("Fecha:", True, BLANCO)
            self.screen.blit(nombre_texto, (ANCHO_MENU/2 - 200, ALTO_MENU/2 - 150))
            self.screen.blit(fecha_texto, (ANCHO_MENU/2 - 200, ALTO_MENU/2 - 50))

            nombre = self.font.render(self.nombre, True, BLANCO)
            fecha = self.font.render(self.fecha, True, BLANCO)
            self.screen.blit(nombre, (self.input_nombre.x + 5, self.input_nombre.y + 5))
            self.screen.blit(fecha, (self.input_fecha.x + 5, self.input_fecha.y + 5))

            # Actualizar y dibujar los botones
            for boton in self.botones:
                boton.update(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def continuar(self):
        if self.nombre:
            # Verificar si el nombre de usuario ya está registrado
            nombre_duplicado, usuarios_existentes = crear_verificar_nombre_usuario(self.nombre, 'datos_jugadores.csv')
            if nombre_duplicado:
                print("El nombre de usuario ya está registrado. Sobrescribiendo el archivo CSV.")
                self.Submenu.nombre_usuario = self.nombre
                self.Submenu.run()
            else:
                print("Nombre de usuario registrado con éxito.")
                print("Usuarios existentes:", usuarios_existentes)
                self.Submenu.nombre_usuario = self.nombre
                self.Submenu.run()

                global nombre_global
                nombre_global = self.nombre
        else:
            print("Por favor, ingresa un nombre de usuario antes de continuar.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu = Menu(nombre_global)
    menu.run()
