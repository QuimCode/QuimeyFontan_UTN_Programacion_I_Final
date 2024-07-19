import pygame


def estado_ataque():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game/Recursos/Trampas/ImagenTrap/Trap1.png'), (50, 50)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Trampas/ImagenTrap/Trap2.png'), (50, 50)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Trampas/ImagenTrap/Trap3.png'), (50, 50)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Trampas/ImagenTrap/Trap4.png'), (50, 50)),
        pygame.transform.scale(pygame.image.load('Game/Recursos/Trampas/ImagenTrap/Trap5.png'), (50, 50))
    ]

    return imagenes
