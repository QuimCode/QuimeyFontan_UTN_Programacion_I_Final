import pygame
import sys
import csv

from ..Parametros import *
from .Recursos_Menu import Boton

class GameOver:
    def __init__(self, nombre_usuario):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
        pygame.display.set_caption("Game Over")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)
        self.nombre_usuario = nombre_usuario

        # Definir el color de fondo como negro
        self.fondo_game_over = NEGRO

        self.botones = []
        self.create_buttons()

    def create_buttons(self):
        # Definir los botones del game over
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2, 200, 50, AZUL, VERDE, "Guardar", self.font, self.guardar))
        self.botones.append(Boton(ANCHO_MENU/2 - 100, ALTO_MENU/2 + 100, 200, 50, AZUL, VERDE, "Salir", self.font, self.salir))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for boton in self.botones:
                    boton.handle_event(event)

            # Dibujar fondo y botones
            self.screen.fill(self.fondo_game_over)

            for boton in self.botones:
                boton.update(self.screen)

            # Mostrar el texto "Game Over" en el centro de la pantalla
            texto_game_over = self.font.render("Game Over", True, BLANCO)
            self.screen.blit(texto_game_over, (ANCHO_MENU/2 - texto_game_over.get_width()/2, ALTO_MENU/2 - 150))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def guardar(self):
        # Llamar a la función para guardar estadísticas
        # guardar_estadisticas_game_over(self.nombre_usuario, 'estadisticas_jugadores.csv')
        # Volver al menú principal
        pass

    def salir(self):
        # Volver al menú principal
        from ..Recursos.Dependencias import crear_instancia_de_menu
        menu = crear_instancia_de_menu(self.nombre_usuario)
        menu.run()

# Función para guardar estadísticas en caso de game over
# def guardar_estadisticas_game_over(nombre_usuario, archivo_csv):
#     with open(archivo_csv, 'r', newline='') as archivo:
#         lector_csv = csv.DictReader(archivo)
#         usuarios_existentes = {fila["Jugador"]: fila for fila in lector_csv}

#     if nombre_usuario in usuarios_existentes:
#         usuarios_existentes[nombre_usuario]["Intentos"] = 0
#         usuarios_existentes[nombre_usuario]["Puntaje"] += 10  # Puedes ajustar esta línea según sea necesario

#     with open(archivo_csv, 'w', newline='') as archivo:
#         nombres_columnas = ["Jugador", "Intentos", "Vida", "Escudo", "Proyectil", "Tiempo", "Puntaje"]
#         escritor_csv = csv.DictWriter(archivo, fieldnames=nombres_columnas)
#         escritor_csv.writeheader()
#         escritor_csv.writerows(usuarios_existentes.values())

#     print(f"Estadísticas guardadas para {nombre_usuario}.")
