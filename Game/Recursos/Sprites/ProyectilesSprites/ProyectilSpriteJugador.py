import pygame

def estado_disparoJ_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga2.png'), (100, 90))
    ]

    return imagenes

def estado_disparoJ_izquierda():
    imagenes = [
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga1.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga2.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga1.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Proyectil\ProyectilJugador\ProyectilJuga2.png'), (100, 90)), True, False)
    ]

    return imagenes