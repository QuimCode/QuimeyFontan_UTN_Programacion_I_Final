#INFORMACION DE PANTALLA // CODIGO VIEJO

# info = pygame.display.Info()
# tamaño_monitor = (info.current_w, info.current_h)
# tamaño_deseado = (int(tamaño_monitor[0] * 1), int(tamaño_monitor[1] * 0.95))

# Función para obtener los bordes como rectángulos
# def obtener_bordes(ancho_pantalla, alto_pantalla):
#     borde_izquierdo = pygame.Rect(0, 0, 1, alto_pantalla)
#     borde_derecho = pygame.Rect(ancho_pantalla - 1, 0, 1, alto_pantalla)
#     borde_superior = pygame.Rect(0, 0, ancho_pantalla, 1)
#     borde_inferior = pygame.Rect(0, alto_pantalla - 1, ancho_pantalla, 1)
#     return [borde_izquierdo, borde_derecho, borde_superior, borde_inferior]


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

    # def aplicar_colisionar2(self, plataformas):
    #     for plataforma in plataformas:
    #         if self.rect.colliderect(plataforma.rect):
    #             # Colisión vertical
    #             if self.velocidad_Y > 0:  # Movimiento hacia abajo
    #                 self.rect.bottom = plataforma.rect.top  # Coloca al jugador en la parte superior de la plataforma
    #                 self.velocidad_Y = 0  # Detiene el movimiento vertical
    #                 print("Desde Arriba")
    #                 self.saltando = False  # El jugador no está saltando
    #             elif self.velocidad_Y < 0:  # Movimiento hacia arriba
    #                 self.rect.top = plataforma.rect.bottom  # Coloca al jugador en la parte inferior de la plataforma
    #                 self.velocidad_Y = 0  # Detiene el movimiento vertical
    #                 print("Desde Bajo")

    #             # # Colisión lateral
    #             # if self.velocidad_X > 0:  # Movimiento hacia la derecha
    #             #     # self.rect.right = plataforma.rect.left  # Coloca al jugador en el borde izquierdo de la plataforma
    #             #     # self.velocidad_X = 0  # Detiene el movimiento horizontal
    #             #     print("Desde Derecha")
    #             # elif self.velocidad_X < 0:  # Movimiento hacia la izquierda
    #             #     # self.rect.left = plataforma.rect.right  # Coloca al jugador en el borde derecho de la plataforma
    #             #     # self.velocidad_X = 0  # Detiene el movimiento horizontal
    #             #     print("Desde Izquierda")






        #     # Colisión desde arriba o abajo
        #     if self.velocidad_Y > 0:
        #         print("Colisión desde arriba")
        #         self.velocidad_Y = 0
        #         self.rect.y = plataforma.rect.top - self.rect.height
        #         self.saltando = False
        #     elif self.velocidad_Y < 0:
        #         print("Colisión desde abajo")
        #         self.velocidad_Y = 0
        #         self.rect.y = plataforma.rect.bottom
        #         self.saltando = False

        # for plataforma in colisiones_plataformas:
        #     # Colisión desde la izquierda o derecha
        #     if self.velocidad_X != 0 and self.rect.colliderect(plataforma):
        #         if self.velocidad_X < 0:  # Colisión desde la izquierda
        #             print("Colisión desde izquierda")
        #             self.rect.left = plataforma.rect.right
        #             self.velocidad_X = 0
        #             self.rebote += 1
        #         elif self.velocidad_X > 0:  # Colisión desde la derecha
        #             print("Colisión desde derecha")
        #             self.rect.right = plataforma.rect.left
        #             self.velocidad_X = 0
        #             self.rebote += 1

    # def aplicar_colisionar(self, plataformas, enemigos):
    #     tiempo_actual = datetime.datetime.now()
    #     colisiones_plataformas = pygame.sprite.spritecollide(self, plataformas, False)
    #     colisiones_enemigos = pygame.sprite.spritecollide(self, enemigos, False)

    #     # Definir los rectángulos de colisión para diferentes partes del personaje
    #     top_rect = self.rect.copy()
    #     top_rect.height = 1
    #     bottom_rect = self.rect.copy()
    #     bottom_rect.y += bottom_rect.height
    #     bottom_rect.height = 1
    #     left_rect = self.rect.copy()
    #     left_rect.width = 1
    #     right_rect = self.rect.copy()
    #     right_rect.x += right_rect.width
    #     right_rect.width = 1

    #     for plataforma in plataformas:
    #         if top_rect.colliderect(plataforma.rect) and self.velocidad_Y < 0:
    #             # Colisión desde abajo del personaje
    #             self.velocidad_Y = 0
    #             self.rect.top = plataforma.rect.bottom
    #             self.saltando = False
    #             self.colisionando = True


    #         elif bottom_rect.colliderect(plataforma.rect) and self.velocidad_Y >= 0:
    #             # Colisión desde arriba del personaje
    #             self.colisionando = True
    #             self.rect.bottom = plataforma.rect.top
    #             self.velocidad_Y = -1

    #     ataque_reciente = False

    #     for enemigo in colisiones_enemigos:
    #         tiempo_transcurrido = tiempo_actual - self.ultimo_ataque_tiempo

    #         # Verificar si ha pasado suficiente tiempo desde el último ataque
    #         if tiempo_transcurrido.total_seconds() >= self.intervalo_ataque:
    #             # Realizar el ataque
    #             # Resto del código para manejar la colisión con el enemigo y realizar el ataque ligero
    #             self.ultimo_ataque_tiempo = tiempo_actual  # Actualizar el tiempo del último ataque
                
    #             # Verificar si ya se ha realizado un ataque recientemente
    #             if not ataque_reciente:
    #                 # Llamar a la función ataque_ligero() del enemigo
    #                 enemigo.ataque_ligero(self)  # Aquí estás pasando el propio personaje como argumento

    #                 ataque_reciente = True

    #                 # Imprimir la vida del personaje después del ataque ligero
    #                 print("Vida del personaje después del ataque ligero:", self.vida)
    #                 print("Escudo del personaje después del ataque ligero:", self.escudo)