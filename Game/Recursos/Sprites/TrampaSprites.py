import pygame


def estado_ataque():
    imagenes = [
        pygame.transform.scale(pygame.image.load('Game\Recursos\Trampas\ImagenTrap\Trap1.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Trampas\ImagenTrap\Trap2.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Trampas\ImagenTrap\Trap3.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Trampas\ImagenTrap\Trap4.png'), (100, 90)),
        pygame.transform.scale(pygame.image.load('Game\Recursos\Trampas\ImagenTrap\Trap5.png'), (100, 90))
    ]

    return imagenes
