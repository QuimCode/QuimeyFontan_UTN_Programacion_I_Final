import pygame

from ...Personajes.Personaje import Personaje
from ...Personajes.Enemigo import Enemigo,EnemigoVolador,EnemigoMago
from ..Plataformas.Class_Plataforma import Plataformas,PlataformaBase,PlataformaVoladora
from ..Proyectiles.Proyectil import ProyectilEnemigo,ProyectilJugador

# def colisiones_plataformas(enemigo, enemigoV, enemigoM, jugador, proyectilE, proyectilJ, plataformas):

#     """Colisiones entre plataformas y jugadors"""
#     for plataforma in plataformas:
#         if enemigo.rect.colliderect(plataforma.rect):
#             if isinstance(plataforma, PlataformaVoladora):
#                 if enemigoV.rect.colliderect(plataforma.rect):
#                     enemigoV.actualizar_enemigo(plataforma.limites_ventana)
#                     enemigoV.dibujar_en_pantalla(enemigoV.ventana, offset_x=-enemigoV.camara_X)
#                     proyectilE.dibujar_en_pantalla(proyectilE.ventana, offset_x=-proyectilE.camara_X)


def verificar_colisiones(plataformas, enemigos, trampas, jugador):

    for plataforma in plataformas:
        for enemigo in enemigos:
            # Comprobar si hay colisión entre el enemigo y la plataforma
            if pygame.sprite.collide_rect(enemigo, plataforma):
                # Si el enemigo está por encima de la plataforma
                if enemigo.rect.bottom <= plataforma.rect.top + 10:
                    # Reposicionar al enemigo justo sobre la plataforma
                    enemigo.rect.bottom = plataforma.rect.top
                    # Detener la velocidad vertical del enemigo
                    enemigo.velocidad_Y = 0
                # Si el enemigo está por debajo de la plataforma
                elif enemigo.rect.top >= plataforma.rect.bottom - 10:
                    if enemigo.velocidad_Y > 0:
                        enemigo.rect.top = plataforma.rect.bottom
                    elif enemigo.velocidad_Y < 0:
                        enemigo.rect.top = plataforma.rect.bottom
                    enemigo.velocidad_Y = 0
                    # # Reposicionar al enemigo justo debajo de la plataforma
                    # enemigo.rect.top = plataforma.rect.bottom
                    # # Detener la velocidad vertical del enemigo
                    # enemigo.velocidad_Y = 0
                # Si el enemigo está a un lado de la plataforma
                elif enemigo.rect.right >= plataforma.rect.left and enemigo.rect.left <= plataforma.rect.right:
                    # Determinar la dirección del movimiento del enemigo
                    if enemigo.velocidad_X > 0:  # Movimiento hacia la derecha
                        enemigo.rect.right = plataforma.rect.left
                    elif enemigo.velocidad_X < 0:  # Movimiento hacia la izquierda
                        enemigo.rect.left = plataforma.rect.right
                    # Detener la velocidad horizontal del enemigo
                    enemigo.velocidad_X = 0

    for plataforma in plataformas:
        if pygame.sprite.collide_rect(jugador, plataforma):
            # Si el jugador está colisionando con la plataforma
            if jugador.rect.colliderect(plataforma.rect):
                # Si el jugador está por encima de la plataforma y no está saltando
                if jugador.velocidad_Y >= 0 and jugador.rect.bottom <= plataforma.rect.top + 10:
                    jugador.rect.bottom = plataforma.rect.top
                    jugador.velocidad_Y = 0
                    jugador.saltando = False
                    jugador.colisionando_abajo = True
                    print("Colisionando arriba")

                # Si el jugador está por debajo de la plataforma
                elif jugador.rect.top >= plataforma.rect.bottom - 10:
                    jugador.rect.top = plataforma.rect.bottom
                    jugador.velocidad_Y = 0

                # Si el jugador está a un lado de la plataforma
                elif jugador.rect.right >= plataforma.rect.left and jugador.rect.left <= plataforma.rect.right:
                    # Determinar la dirección del movimiento del jugador
                    if jugador.velocidad_X > 0:  # Movimiento hacia la derecha
                        jugador.rect.right = plataforma.rect.left
                        print("Colisionando derecha")
                    elif jugador.velocidad_X < 0:  # Movimiento hacia la izquierda
                        jugador.rect.left = plataforma.rect.right
                        print("Colisionando izquierda")
                    jugador.velocidad_X = 0


    for trampa in trampas:
        if pygame.sprite.collide_rect(jugador, trampa):
            # Activar la trampa cuando el jugador colisiona con ella
            trampa.activar_trampa(jugador)


def comprobacion_colision(plataformas, enemigos, trampas, jugador):
    verificar_colisiones(plataformas, enemigos, trampas, jugador)

