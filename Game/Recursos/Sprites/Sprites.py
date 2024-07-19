import pygame
import imageio
from moviepy.editor import VideoFileClip

pygame.init()


def estado_quieto():
    imagenes = [
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_1.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_2.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_3.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_4.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_5.png'), (100, 100)),
            pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_6.png'), (100, 100))
        ]

    return imagenes

def estado_quieto_izquerda():
    imagenes = [
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_1.png'), True, False), (100, 100)),
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_2.png'), True, False), (100, 100)),
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_3.png'), True, False), (100, 100)),
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_4.png'), True, False), (100, 100)),
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_5.png'), True, False), (100, 100)),
            pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/idle/Warrior_Idle_6.png'), True, False), (100, 100))
        ]

    return imagenes


def estado_izquierda():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_1.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_2.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_3.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_4.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_5.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_6.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_7.png'), True, False), (100, 100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_8.png'), True, False), (100, 100))
    ]

    return imagenes

def estado_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_3.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_4.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_5.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_6.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_7.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Run/Warrior_Run_8.png'), (100, 100))
    ]

    return imagenes

def estado_saltando():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Jump/Warrior_Jump_3.png'), (100, 100))
    ]

    return imagenes

def estado_ataque_ligero_derecha():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_1.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_2.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_3.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_4.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_5.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_6.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_7.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_8.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_9.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_10.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_11.png'),(100,100)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_12.png'),(100,100))
    ]

    return imagenes

def estado_ataque_ligero_izquierda():
    imagenes = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_1.png'), True, False), (100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_2.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_3.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_4.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_5.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_6.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_7.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_8.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_9.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_10.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_11.png'), True, False),(100,100)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Game/Recursos/Jugador_Enemigos/Warrior/Individual Sprite/Attack/Warrior_Attack_12.png'), True, False),(100,100))
    ]

    return imagenes

#-------------------------------------------------------------------------ENEMIGO-------------------------------------------------------------------------#
#-------------------------------------------------------------------------ENEMIGO-------------------------------------------------------------------------#

# def estado_quieto_enemigo():
#     gif_path = 'Jugador_Enemigos/Skeleton (Enemigos)/GIFS/Skeleton Idle.gif'
#     clip = VideoFileClip(gif_path)
#     clip_duration = clip.duration
#     frames = [clip.get_frame(t) for t in range(0, int(clip_duration * clip.fps))]
#     for frame in frames:
#         print("Tamaño del frame:", frame.size)
#     imagenes_convertidas = [pygame.image.fromstring(frame.tobytes(), frame.size, "RGB") for frame in frames]
#     return imagenes_convertidas