import pygame

from ..Recursos.Parametros import *

nombre_global = "-No Registrado-"

class Boton:
    def __init__(self, x, y, ANCHO_MENU, ALTO_MENU, color_normal, color_hover, texto, font, action=None):
        self.rect = pygame.Rect(x, y, ANCHO_MENU, ALTO_MENU)
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.texto = texto
        self.font = font
        self.action = action
        self.hover = False

    def update(self, screen):
        color = self.color_hover if self.hover else self.color_normal
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.texto, True, BLANCO)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hover:
            if self.action:
                self.action()

class BotonIcono(Boton):
    def __init__(self, x, y, width, height, color_hover, icono, action=None):
        super().__init__(x, y, width, height, None, color_hover, None, None, action)
        self.hover_icono = icono  # Aquí asignamos icono a hover_icono

    def update(self, screen):
        if self.hover:
            screen.blit(self.hover_icono, self.rect.topleft)  # Usamos hover_icono en lugar de icono
        else:
            # Tintar el icono con el color hover si no está en estado hover
            icono_tintado = self.hover_icono.copy()
            icono_tintado.fill(self.color_hover, None, pygame.BLEND_RGBA_MULT)
            screen.blit(icono_tintado, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hover:
            if self.action:
                self.action()


