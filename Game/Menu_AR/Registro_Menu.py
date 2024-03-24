import pygame

from .Recursos_Menu import Boton
from ..Parametros import *

class SubmenuRegistro:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Registro de Jugador")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)

        self.fondo_menu = pygame.image.load("Game\Recursos\Mapas_Fondos\Menu\castle-medieval-pixel-art-pixelated-field-2254356.jpg").convert()

        self.nombre = ""
        self.fecha = ""
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
            # pygame.draw.rect(self.screen, BLANCO if self.fecha_activo else AZUL, self.input_fecha, 2)

            nombre_texto = self.font.render("Nombre:", True, BLANCO)
            # fecha_texto = self.font.render("Fecha:", True, BLANCO)
            self.screen.blit(nombre_texto, (ANCHO_MENU/2 - 200, ALTO_MENU/2 - 150))
            # self.screen.blit(fecha_texto, (ANCHO_MENU/2 - 200, ALTO_MENU/2 - 50))

            nombre = self.font.render(self.nombre, True, BLANCO)
            # fecha = self.font.render(self.fecha, True, BLANCO)
            self.screen.blit(nombre, (self.input_nombre.x + 5, self.input_nombre.y + 5))
            # self.screen.blit(fecha, (self.input_fecha.x + 5, self.input_fecha.y + 5))

            # Actualizar y dibujar los botones
            for boton in self.botones:
                boton.update(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def continuar(self):
        from ..Recursos.Dependencias import crear_instancia_de_submenu
        if self.nombre:
            # Verificar si el nombre de usuario ya está registrado
            nombre_duplicado, usuarios_existentes = crear_verificar_nombre_usuario(self.nombre, 'datos_jugadores.csv')
            if nombre_duplicado:
                print("El nombre de usuario ya está registrado. Sobrescribiendo el archivo CSV.")
                submenu = crear_instancia_de_submenu(self.nombre)
                submenu.run()
            else:
                print("Nombre de usuario registrado con éxito.")
                print("Usuarios existentes:", usuarios_existentes)
                submenu = crear_instancia_de_submenu(self.nombre)
                submenu.run()

                global nombre_global
                nombre_global = self.nombre
        else:
            print("Por favor, ingresa un nombre de usuario antes de continuar.")