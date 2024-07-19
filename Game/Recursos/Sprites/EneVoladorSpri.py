import pygame

def estado_quieto_enemigo_volador():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador4.png'), (100, 90))
    ]

    return imagenes

# def estado_quieto_enemigo_volador():
#     imagenes = [
#         pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador1.png'), (100, 90)), True, False),
#         pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador2.png'), (100, 90)), True, False),
#         pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador3.png'), (100, 90)), True, False),
#         pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador4.png'), (100, 90)), True, False)
#     ]

#     return imagenes


def estado_derecha_enemigo_volador():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador1.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador2.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador3.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador4.png'), True, False), (100, 90))
    ]

    return imagenes

def estado_izquierda_enemigo_volador():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador3.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/EnemigoVolador/Volador4.png'), (100, 90))

    ]

    return imagenes