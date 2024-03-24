##-------------MODULOS-------------##

import pygame
import sys
import csv
import random
import math
import os
from os import listdir
from os.path import isfile, join

pygame.init()

##---------------------------------##

VELOCIDAD_ANIMACION = 5

# COLORES
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

#DIMENSIONES
ANCHO_MENU = (1500)
ALTO_MENU = (700)

ANCHO = (1600)
ALTO = (800)

##--------------FUNCIONES DE CONTROL-------------------##

def crear_verificar_nombre_usuario(nombre_usuario, archivo_csv):
    try:
        usuarios_existentes = []  # Lista para almacenar nombres de usuario existentes en el archivo CSV
        
        # Abrir el archivo CSV en modo lectura
        with open(archivo_csv, 'r', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            # Leer cada fila del archivo CSV
            for fila in lector_csv:
                usuarios_existentes.append(fila[0])  # Agregar el nombre de usuario a la lista
        
        # Verificar si el nombre de usuario ya está en la lista antes de agregarlo
        if nombre_usuario in usuarios_existentes:
            print("El nombre de usuario ya está registrado.")
            return True, usuarios_existentes
        else:
            # Si el nombre de usuario no está en la lista, agregarlo y escribir en el archivo CSV
            usuarios_existentes.append(nombre_usuario)
            with open(archivo_csv, 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                for usuario in usuarios_existentes:
                    escritor_csv.writerow([usuario])
            print("Nombre de usuario registrado con éxito.")
            return False, usuarios_existentes

    except FileNotFoundError:
        # Manejar el caso donde el archivo CSV no existe
        print("El archivo CSV no existe.")
        return False, []
    except Exception as e:
        # Manejar cualquier otro error que pueda ocurrir durante la lectura o escritura del archivo
        print("Error al leer/escribir el archivo CSV:", e)
        return False, []

nombre_jugador_global = None

def establecer_nombre_jugador(nombre):
    global nombre_jugador_global
    nombre_jugador_global = nombre