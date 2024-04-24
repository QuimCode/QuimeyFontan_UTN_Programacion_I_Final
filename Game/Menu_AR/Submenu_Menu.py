import pygame

from .Recursos_Menu import Boton,BotonIcono
from ..Niveles.Class_Nivel1 import Nivel1
from ..Niveles.Class_Nivel2 import Nivel2
from ..Niveles.Class_Nivel3 import Nivel3
from ..Parametros import *

class Submenu:
    def __init__(self, nombre):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Submenú")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        self.fondo_menu = pygame.image.load("Game\Recursos\Mapas_Fondos\Menu\castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (ANCHO_MENU, ALTO_MENU))
        self.icono_mute = pygame.image.load("Game\Recursos\Iconos\icons8-sin-audio-80.png").convert_alpha()
        # pygame.mixer.music.load("Game\\Recursos\\Musica\\bit-fantasy-rpg-adventure-music-1.mp3")
        self.sonido_activado = True

        self.nombre_cap = nombre
        self.nombre_usuario = self.nombre_cap

        self.botones = []
        self.create_buttons()
        self.creacion_iconos()

    def create_buttons(self):
        # Definir los botones del submenú
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 150, 200, 50, AZUL, VERDE, "Menu", self.font, self.jugar))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 - 50, 200, 50, AZUL, VERDE, "Registro", self.font, self.registro))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 50, 200, 50, AZUL, VERDE, "Jugar Nivel 1", self.font, self.jugar_nivel_1))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 150, 200, 50, AZUL, VERDE, "Jugar Nivel 2", self.font, self.jugar_nivel_2))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 250, 200, 50, AZUL, VERDE, "Jugar Nivel 3", self.font, self.jugar_nivel_3))

    def creacion_iconos(self):
        self.boton_mute = BotonIcono(ANCHO_MENU/2 + 620, ALTO_MENU/2 - 320, 80, 80, AZUL, self.icono_mute, self.activacion_sonido)

    def run(self):
        # pygame.mixer.music.play(-1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for boton in self.botones:
                    boton.handle_event(event)
                self.boton_mute.handle_event(event)

            # Dibujar el fondo del menú
            self.screen.blit(self.fondo_menu, (0, 0))
            self.boton_mute.update(self.screen)

            
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
        # Inicio del apartado del registro con la instancia de la misma desde la carpeta de dependencias.
        from ..Recursos.Dependencias import crear_instancia_de_submenuregistro
        submenu_registro = crear_instancia_de_submenuregistro()
        submenu_registro.run()
        # Actualizar el nombre de usuario después de que se complete el registro.
        self.nombre_usuario = submenu_registro.nombre

    def jugar(self):
        # Importar la clase del menu aquí dentro del método jugar
        from ..Recursos.Dependencias import crear_instancia_de_menu
        menu = crear_instancia_de_menu(self.nombre_usuario)
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
        if not self.nombre_usuario == "-Usuario No Registrado-":
            Nivel3.ejecutar_nivel3()
            print("Iniciar nivel 3...")
        else:
            print("Por favor, registra un usuario antes de jugar.")

    def activacion_sonido(self):
        # Alternar estado de sonido activado/desactivado
        self.sonido_activado = not self.sonido_activado
        if self.sonido_activado:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
