import pygame

pygame.init()

import pygame

pygame.init()

def estado_quieto():
    imagenes = [
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_1.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_2.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_3.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_4.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_5.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Idle/Warrior_Idle_6.png'), (100, 100))
        ]

    return imagenes

def estado_izquierda():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_1.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_2.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_3.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_4.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_5.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_6.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_7.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_8.png'), True, False), (100, 100))
    ]

    return imagenes

def estado_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_3.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_4.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_5.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_6.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_7.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_8.png'), (100, 100))
    ]

    return imagenes

def estado_saltando():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_3.png'), (100, 100))
    ]

    return imagenes

def estado_ataque_ligero_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_1.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_2.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_3.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_4.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_5.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_6.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_7.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_8.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_9.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_10.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_11.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_12.png'),(100,100))
    ]

    return imagenes

def estado_ataque_ligero_izquierda():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_1.png'), True, False), (100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_2.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_3.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_4.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_5.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_6.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_7.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_8.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_9.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_10.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_11.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_12.png'), True, False),(100,100))
    ]

    return imagenes

