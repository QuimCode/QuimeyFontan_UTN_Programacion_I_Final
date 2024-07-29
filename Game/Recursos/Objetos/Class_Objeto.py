import pygame

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, imagen_path=None, ancho=None, alto=None):
        super().__init__()
        if imagen_path is not None:
            self.imagen = pygame.image.load(imagen_path).convert_alpha()
            if ancho is not None and alto is not None:
                self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        else:
            self.imagen = None  # O usa una imagen predeterminada si lo deseas
        self.rect = self.imagen.get_rect(topleft=(x, y)) if self.imagen else pygame.Rect(x, y, 0, 0)

    def actualizar(self):
        # Método para actualizar el estado del objeto, si es necesario
        pass

    def dibujar_en_pantalla(self, superficie):
        if self.imagen:
            superficie.blit(self.imagen, self.rect)

class PocionVida(Objeto):
    def __init__(self, x, y, imagen_path=None, ancho=None, alto=None):
        super().__init__(x, y, imagen_path, ancho, alto)
        self.vida_extra = 50  # Cantidad de vida que otorga la poción

    def usar(self, personaje):
        personaje.vida += self.vida_extra
        # Asegúrate de que la vida del personaje no exceda su vida máxima
        personaje.vida = min(personaje.vida, personaje.vida_maxima)

class PocionEscudo(Objeto):
    def __init__(self, x, y, imagen_path=None, ancho=None, alto=None):
        super().__init__(x, y, imagen_path, ancho, alto)
        self.escudo_extra = 30  # Cantidad de escudo que otorga la poción

    def usar(self, personaje):
        personaje.escudo += self.escudo_extra
        # Asegúrate de que el escudo del personaje no exceda su escudo máximo
        personaje.escudo = min(personaje.escudo, personaje.escudo_maximo)

class LlavePortal(Objeto):
    def __init__(self, x, y, imagen_path=None, ancho=None, alto=None):
        super().__init__(x, y, imagen_path, ancho, alto)
        self.tipo_llave = 'Portal'  # Tipo de llave

    def usar(self, jugador):
        # Método específico para usar la llave, tal vez para abrir un portal
        print("Llave de portal usada")

