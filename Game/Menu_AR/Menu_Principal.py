import pygame
import sys

from ..Parametros import *
from .Recursos_Menu import Boton, BotonIcono

class Menu:
    def __init__(self, nombre):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Menú del juego")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        # Cargar la imagen del fondo del menú
        self.fondo_menu = pygame.image.load("Game\Recursos\Mapas_Fondos\Menu\castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (ANCHO_MENU, ALTO_MENU))
        self.icono_mute = pygame.image.load("Game\Recursos\Iconos\icons8-sin-audio-80.png").convert_alpha()
        # pygame.mixer.music.load("Game\\Recursos\\Musica\\bit-fantasy-rpg-adventure-music-1.mp3") -------------------------        MUSICA ------------------------------------
        self.sonido_activado = True

        self.nombre_capturado = nombre
        self.nombre_usuario = self.nombre_capturado

        self.botones = []
        self.creacion_iconos()
        self.create_buttons()

    def create_buttons(self):
        # Definir los botones del menú
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 50, 200, 50, AZUL, VERDE, "Jugar", self.font, self.jugar))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 50, 200, 50, AZUL, VERDE, "Controles", self.font, self.controles))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 150, 200, 50, AZUL, VERDE, "Salir", self.font, self.salir ))

    def creacion_iconos(self):
        self.boton_mute = BotonIcono(ANCHO_MENU/2 + 620, ALTO_MENU/2 - 320, 80, 80, AZUL, self.icono_mute, self.activacion_sonido)

    def run(self):
        # Reproducir música de fondo
        # pygame.mixer.music.play(-1) ---------------------------------------------- MUSICA

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for boton in self.botones:
                    boton.handle_event(event)
                self.boton_mute.handle_event(event)

            # Dibujar Menu/Botones/Iconos
            self.screen.blit(self.fondo_menu, (0, 0))
            self.boton_mute.update(self.screen)

            # Actualiza los botones regulares
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
        # Importar la clase del submenu aquí dentro del método jugar
        from ..Recursos.Dependencias import crear_instancia_de_submenu
        submenu = crear_instancia_de_submenu(self.nombre_usuario)
        submenu.run()

    def salir(self):
        pygame.quit()
        sys.exit()

    def controles(self):
        pass

    def activacion_sonido(self):
        # Alternar estado de sonido activado/desactivado
        self.sonido_activado = not self.sonido_activado
        if self.sonido_activado:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()