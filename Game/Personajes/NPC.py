import pygame

class NpcBase ():
    def __init__ (self, x, y, ancho, alto):
        self.posX = x
        self.posY = y
        self.tamAncho = ancho
        self.tamAlto = alto
        
        self.hitbox = pygame.Rect(self.posX, self.posY, self.tamAncho, self.tamAlto)

    def draw(self):
        # Dibujar el NPC en la pantalla
        pass

    def update(self):
        # Actualizar la posición y el cubo de colisión del NPC
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)