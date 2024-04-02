import pygame


def estado_quieto_enemigo():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_5.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_6.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_7.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Idle\Bringer-of-Death_Idle_8.png'), (100, 90)),
    ]
    
    return imagenes

def estado_derecha_enemigo():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_1.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_2.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_3.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_4.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_5.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_6.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_7.png'), True, False), (100, 90)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_8.png'), True, False), (100, 90))
    ]

    return imagenes

def estado_izquierda_enemigo():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_3.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_5.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_6.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_7.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Walk\Bringer-of-Death_Walk_8.png'), (100, 90))
    ]

    return imagenes


def estado_ataque_enemigo():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_1.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_2.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_3.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_4.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_5.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_6.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_7.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_8.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_9.png'), (90, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Jugador_Enemigos\Bringer-Of-Death\Individual Sprite\Attack\Bringer-of-Death_Attack_10.png'), (90, 90))
    ]

    return imagenes



