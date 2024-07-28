##-------------MODULOS-------------##

import pygame
import sys
from os import listdir
from os.path import isfile, join

##-------------ARCHIVOS-------------##

from Game.Recursos.Parametros import *
from ..Personajes.Personaje import Personaje, lista_proyectiles
from ..Personajes.Enemigo import Enemigo, EnemigoVolador, EnemigoMago
from ..Recursos.Sprites.Sprites import *
from ..Recursos.Trampas.Trampa import Trampa
from ..Recursos.Plataformas.Class_Plataforma import *
# from ..Recursos.Colision.Colisiones import comprobacion_colision


##---------------------------------##

class Nivel:
    def __init__(self, tiempo_restante, nombre_jugador, numero) -> None:
        pygame.init()
        pygame.joystick.init()

#=================== COMPOSICION VISUAL ===================#

        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        fondo_original = pygame.image.load(fondos_nivel.get(numero))
        self.fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO)).convert()

#=================== INSTANCIA/GRUPOS ===================#
        #Jugador
        self.jugador = Personaje(10, 950, nombre=nombre_jugador)
        print(f"Nombre al iniciar Nivel: {nombre_jugador}")
        self.grupo_proyectiles_jugador = self.jugador.grupo_proyectiles
        self.grupo_proyectiles_jugador = pygame.sprite.Group()
        
        #Trampas - Grupo
        self.trampas = pygame.sprite.Group()  # Grupo para almacenar las trampitas
        for trampa in trampas_nivel.get(numero, []):
            self.trampas.add(trampa)  # cada trampa individualmente al grupete
        
        #Enemigos - Grupo
        self.enemigos = pygame.sprite.Group()  
        for enemigo in enemigos_nivel.get(numero, []):
            self.enemigos.add(enemigo)  # cada enemigo individualmente
        
        #Plataformas - Grupo
        self.plataformas = pygame.sprite.Group()
        self.plataformas.add(plataformas_nivel[numero])

#=================== MARCADORES/TIEMPO/PUNTAJE ===================#
        #Tiempo
        self.reloj = pygame.time.Clock()
        self.tiempo_restante = tiempo_restante
        # self.tiempo_restante = 100  # Tiempo inicial en segundos (2 minutos y 50 segundos)
        self.tiempo_anterior = pygame.time.get_ticks()
        self.tiempo = 0

        #Punto
        self.puntaje = 0

        #Fuente
        self.fuente = pygame.font.Font(None, 36)

#=================== PASAR NIVEL ===================#

        self.numero = numero


        # Coordenadas de transición para cada nivel
        self.transicion_coordenadas = {
            1: (900, 650),  # Ejemplo de coordenadas para nivel 1
            2: (500, 400),  # Ejemplo de coordenadas para nivel 2
            3: (700, 300)   # Ejemplo de coordenadas para nivel 3
        }

#=================== MANEJADOR/CONTROLES ===================#

    def manejador_eventos_nivel(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    if not self.jugador.atacando:
                        self.jugador.movimiento_izquierda()
                elif event.key == pygame.K_d:
                    if not self.jugador.atacando:
                        self.jugador.movimiento_derecha()
                elif event.key == pygame.K_w and not self.jugador.saltando:
                    if not self.jugador.atacando:
                        self.jugador.movimiento_salto()
                elif event.key == pygame.K_s:
                    if not self.jugador.atacando:
                        self.jugador.disparar_proyectil()
                elif event.key == pygame.K_k:
                    self.jugador.recibir_daño
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.jugador.movimiento_detener()

#=================== MANEJADOR/NIVELES ===================#

    def cargar_progreso_jugador(self):
        datos_jugador = cargar_datos_jugador(self.nombre_jugador, 'datos_jugadores.csv')
        if datos_jugador:
            self.jugador.cargar_progreso(datos_jugador)
            print(f"Se cargaron los datos del jugador {self.nombre_jugador}")
        else:
            print(f"No se pudo cargar el progreso del jugador {self.nombre_jugador}. Usando valores por defecto.")


    def verificar_transicion(self):
        if self.numero in self.transicion_coordenadas:
            x, y = self.transicion_coordenadas[self.numero]
            if self.jugador.rect.x >= x and self.jugador.rect.y >= y:
                return True
        return False

#=================== MANEJADOR/TEXTO ===================#

    def dibujar_texto_de_niveles(self, superficie):
        texto_posiciones = {
            "Intentos": (250, 50),
            "Vida": (450, 50),
            "Escudo": (600, 50),
            "Proyectil": (800, 50),
            "Tiempo": (1000, 50),
            "Puntaje": (1200, 50),
            "Nombre" : (1400, 50),
        }

        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60
        tiempo_formateado = f"Tiempo: {minutos:02}:{segundos:02}"

        textos = {
            "Intentos": f"Intentos: {self.jugador.intentos}",
            "Vida": f"Vida: {self.jugador.vida}",
            "Escudo": f"Escudo: {self.jugador.escudo}",
            "Proyectil": f"Proyectil: {self.jugador.proyectiles}",
            "Tiempo": tiempo_formateado,
            "Puntaje": f"Puntaje: {self.puntaje}",
            "Nombre": f"Nombre: {self.jugador.nombre}",
        }

        for texto, posicion in texto_posiciones.items():
            texto_surface = self.fuente.render(textos[texto], True, BLANCO)
            texto_rect = texto_surface.get_rect(topleft=posicion)
            self.ventana.blit(texto_surface, texto_rect)

        if len(lista_proyectiles) > 0:
            print("Lista de proyectiles Nivel:", lista_proyectiles)
            print("Número de proyectiles en la lista Nivel:", len(lista_proyectiles))

    def obtener_estadisticas(self):
        return {
            "Intentos": self.jugador.intentos,
            "Vida": self.jugador.vida,
            "Escudo": self.jugador.escudo,
            "Proyectil": self.jugador.proyectiles,
            "Puntaje": self.puntaje,
        }

#=================== MANEJAR TIEMPO ===================#

    def actualizar_tiempo(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_anterior >= 1000:
            self.tiempo_restante -= 1
            self.tiempo_anterior = tiempo_actual
            if self.tiempo_restante <= 0:
                self.tiempo_restante = 0
                self.jugador.intentos -= 1
                if self.jugador.intentos > 0:
                    self.reiniciar_nivel()
                else:
                    print("Game Over")
                    pygame.quit()


    def reiniciar_nivel(self):
        self.jugador.vida = self.jugador.vida_maxima  # Reiniciar la vida del jugador
        self.jugador.rect.x = 10  # Reubicar al jugador en la posición inicial
        self.jugador.rect.y = 650
        self.tiempo_restante = 170  # Reiniciar el tiempo del nivel

    def finalizar_nivel(self):
        archivo_csv = "datos_jugadores.csv"
        guardar_estadisticas_al_final_del_nivel(self.jugador, self, archivo_csv)  # Asume que self.jugador es una instancia de Personaje
        print("Estadísticas guardadas al final del nivel")

    def dibujar_nivel(self):
        self.ventana.fill(NEGRO)
        for x in range(0, 8000, self.fondo.get_width()):
            for y in range(0, ALTO, self.fondo.get_height()):
                self.ventana.blit(self.fondo, (x, y))

        # Dibujo al jugador y otros elementos dependientes de la cámara
        self.jugador.dibujar_en_pantalla(self.ventana)
        self.dibujar_texto_de_niveles(self.ventana)

        # Dibujo solo las plataformas que estan dentro de la pantalla visible
        for plataforma in self.plataformas:
            plataforma.dibujar_en_pantalla(self.ventana)

        for trampa in self.trampas:
            trampa.dibujar_trampa(self.ventana)

        # Dibujo todos los enemigos sin importar su posición relativa a la cámara
        for enemigo in self.enemigos:
            enemigo.dibujar_en_pantalla(self.ventana)

        for proyectil in self.grupo_proyectiles_jugador:
            proyectil.dibujar(self.ventana)


    def actualizar_nivel(self):
        limites_ventana = [0, ANCHO, 0, ALTO]

        self.manejador_eventos_nivel()
        self.jugador.actualizar_personaje(self.plataformas, self.grupo_proyectiles_jugador, self.enemigos, self.trampas, limites_ventana)
        self.grupo_proyectiles_jugador.update()
        self.plataformas.update()
        self.enemigos.update()

        # self.verificar_colisiones(self.plataformas, self.enemigos, self.trampas, self.jugador)

        # Eliminar enemigos con vida igual o menor a 0
        enemigos_a_eliminar = [enemigo for enemigo in self.enemigos if enemigo.vida_enemigo <= 0]
        for enemigo in enemigos_a_eliminar:
            self.enemigos.remove(enemigo)

        # Actualizo los enemigos individualmente
        for enemigo in self.enemigos:
            # verifico si el sprite es de la clase Enemigo
            if isinstance(enemigo, Enemigo):
                # Llamo al método actualizar_enemigo si está 
                if hasattr(enemigo, 'actualizar_enemigo'):
                    enemigo.actualizar_enemigo(self.plataformas, self.grupo_proyectiles_jugador, limites_ventana)

        for trampa in self.trampas:
            trampa.actualizar(self.jugador)

        self.actualizar_tiempo()

#-------------LISTA/DICCIONARIO PLATAFORMAS-------------#

plataformas_nivel = {
    1: [ Plataformas(200, 960, 100, 100, AZUL), Plataformas(370, 960, 100, 30, AZUL) ,Plataformas(900, 800, 500, 30, AZUL), PlataformaBase(0, 1040, 1920, 30, ROJO) ],
    2: [ PlataformaBase(0, 1040, 1920, 30, ROJO) ],
    3: [ PlataformaBase(0, 1040, 1920, 30, ROJO) ],
}



trampas_nivel = {
    1: [Trampa(500, 900)],
    2: [],
    3: []
}

enemigos_nivel = {
    1: [Enemigo(1100, 720), Enemigo(2100, 710), Enemigo(3100, 710), Enemigo(4100, 710), Enemigo(5100, 710), EnemigoVolador(400, 650), EnemigoMago(100, 650, "izquierda"), EnemigoMago(600, 650, "derecha")],
    2: [Enemigo(1100, 720), Enemigo(2100, 710), Enemigo(3100, 710), Enemigo(4100, 710), Enemigo(5100, 710), EnemigoVolador(400, 650), EnemigoMago(100, 650, "izquierda"), EnemigoMago(600, 650, "derecha")],
    3: [Enemigo(1100, 720), Enemigo(2100, 710), Enemigo(3100, 710), Enemigo(4100, 710), Enemigo(5100, 710), EnemigoVolador(400, 650), EnemigoMago(100, 650, "izquierda"), EnemigoMago(600, 650, "derecha")]
}

fondos_nivel = {
    1: "Game/Recursos/Mapas_Fondos/Free Pixel Art Forest/Preview/Back1920.png",
    2: "Game/Recursos/Mapas_Fondos/Free Pixel Art Hill/PREVIEWS/Hills1920.png",
    3: "Game/Recursos/Mapas_Fondos/Glacial-mountains-parallax-background_vnitti/HillsFrozen1920.png"
}



            # Captura del clic del ratón
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # 1 para el clic izquierdo
            #         # Obtener las coordenadas del mouse en relación con la pantalla
            #         mouse_x_screen, mouse_y_screen = pygame.mouse.get_pos()
            #         # Ajustar las coordenadas del mouse para tener en cuenta la posición de la cámara
            #         mouse_x_world = mouse_x_screen + self.camara_X
            #         mouse_y_world = mouse_y_screen
            #         print(f"Posición del ratón - X: {mouse_x_world}")
            #         print(f"Posición del ratón - Y: {mouse_y_world}")