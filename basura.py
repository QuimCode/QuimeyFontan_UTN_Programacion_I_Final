#     def manejador_evento(self, event):
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 self.velocidad_X = -1
#             elif event.key == pygame.K_d:
#                 self.velocidad_X = 1
#             elif event.key == pygame.K_w:
#                 self.velocidad_Y = -1
#             elif event.key == pygame.K_s:
#                 self.velocidad_Y = 1

#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_a and self.velocidad_X < 0:
#                 self.velocidad_X = 0
#             elif event.key == pygame.K_d and self.velocidad_X > 0:
#                 self.velocidad_X = 0
#             elif event.key == pygame.K_w and self.velocidad_Y < 0:
#                 self.velocidad_Y = 0
#             elif event.key == pygame.K_s and self.velocidad_Y > 0:
#                 self.velocidad_Y = 0

#     def aplicar_gravedad(self):
#         self.velocidad_Y += self.gravedad

#     def movimiento_actualizado(self, velocidad_X, velocidad_Y, limites):
#         nueva_posicion_x = self.rect.x + velocidad_X
#         nueva_posicion_y = self.rect.y + velocidad_Y + self.velocidad_Y

#         # Verifica límites horizontales 
#         if limites[0].left <= nueva_posicion_x <= limites[1].right - self.rect.width:
#             self.rect.x = nueva_posicion_x
#         else:
#             print(f"Límite horizontal alcanzado. Coordenada actual: ({self.rect.x}, {self.rect.y})")

#         # Verifica límites verticales
#         if limites[2].top <= nueva_posicion_y <= limites[3].bottom - self.rect.height:
#             self.rect.y = nueva_posicion_y
#         else:
#             print(f"Límite horizontal alcanzado. Coordenada actual: ({self.rect.x}, {self.rect.y})")

#         # Imprimir los límites
#         # print("Limite izquierdo:", limites[0])
#         # print("Limite derecho:", limites[1])
#         # print("Limite superior:", limites[2])
#         # print("Limite inferior:", limites[3])

#     def actualizar(self, limites):
#         self.aplicar_gravedad()
#         self.movimiento_actualizado(self.velocidad_X, self.velocidad_Y, limites)

#         for obstaculo in limites:
#             if self.rect.colliderect(obstaculo):
#                 # Realiza acciones para manejar la colisión (ajusta la posición de manera más segura)
#                 if self.velocidad_X > 0:
#                     self.rect.right = obstaculo.left
#                 elif self.velocidad_X < 0:
#                     self.rect.left = obstaculo.right

#                 if self.velocidad_Y > 0:
#                     self.rect.bottom = obstaculo.top
#                 elif self.velocidad_Y < 0:
#                     self.rect.top = obstaculo.bottom

# #------------------MOVIMIENTO------------------#

#     def dibujar_en_pantalla(self, pantalla):
#         # Dibuja al personaje en la pantalla
#         pantalla.blit(self.imagen, self.rect.topleft)
    



            # self.sprites_animacion = sprites_animacion
        # self.indice_sprite_actual = 0
        # self.imagen_actual = self.sprites_animacion[self.indice_sprite_actual]

        # Aparición
        # self.rect = self.imagen_actual.get_rect()
        # self.rect.center = origen



    #-----------MOVIMIENTO/GRAVEDAD-----------#
# Toma de presion de teclas y asignacion de metodos de movimiento de la clase Personaje instanciada en la variable jugador # 
        # teclas = pygame.key.get_pressed()

        # if teclas[pygame.K_a]:
        #     self.jugador.movimiento_izquierda()
        # elif teclas[pygame.K_d]:
        #     self.jugador.movimiento_derecha()
        # elif teclas[pygame.K_w] and not self.jugador.saltando:
        #     self.jugador.movimiento_salto()
        #     print(self.jugador.saltando)
        # else:
        #     self.jugador.movimiento_detener()

    #-----------MOVIMIENTO/GRAVEDAD-----------#