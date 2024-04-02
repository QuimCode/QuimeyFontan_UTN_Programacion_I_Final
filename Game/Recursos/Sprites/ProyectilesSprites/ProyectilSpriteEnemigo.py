import pygame

def estado_disparo_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil2.png'), (100, 90))
    ]

    return imagenes

def estado_disparo_izquierda():
    imagenes = [
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil1.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil2.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil1.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\Proyectil2.png'), (100, 90)), True, False)
    ]

    return imagenes