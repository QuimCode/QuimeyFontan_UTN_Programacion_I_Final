import pygame

def estado_quietoD_enemigo_mago():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle5.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle6.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle7.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle8.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle9.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle10.png'), (100, 90))
    ]

    return imagenes

def estado_quietoI_enemigo_mago():
    imagenes = [
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle1.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle2.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle3.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle4.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle5.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle6.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle7.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle8.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle9.png'), (100, 90)), True, False),
        pygame.transform.flip(pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Idle\EneMagoIdle10.png'), (100, 90)), True, False)
    ]

    return imagenes


def estado_ataque_izquierda_enemigo_mago():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador5.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador6.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador7.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador8.png'), (100, 90))
    ]

    return imagenes

def estado_ataque_derecha_enemigo_mago():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador1.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador2.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador3.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador4.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador5.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador6.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador7.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Shoot\EnemigoTirador8.png'), True, False), (100, 90))
    ]

    return imagenes

def estado_muerto_enemigo_mago():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht5.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht6.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht7.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht8.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht9.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\EnemigoMago\Deaht\EneMagoDeaht10.png'), (100, 90))
    ]

    return imagenes