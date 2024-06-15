##-------------MODULOS-------------##

import pygame
import csv

pygame.init()

##---------------------------------##

VELOCIDAD_ANIMACION = 6

# COLORES
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

#DIMENSIONES
ANCHO_MENU = (1500)
ALTO_MENU = (700)

ANCHO = (1920)
ALTO = (1050)

##--------------FUNCIONES DE CONTROL-------------------##

nombre_jugador_global = None

def establecer_nombre_jugador(nombre):
    global nombre_jugador_global
    nombre_jugador_global = nombre

def crear_verificar_nombre_usuario(nombre_usuario, archivo_csv):
    global nombre_jugador_global
    
    try:
        # Verificar si el archivo CSV existe
        with open(archivo_csv, 'r', newline='') as archivo:
            # Leer los datos del archivo CSV
            lector_csv = csv.DictReader(archivo)
            usuarios_existentes = {fila["Jugador"]: fila for fila in lector_csv}

            # Verificar si el nombre de usuario ya existe en los datos existentes
            if nombre_usuario in usuarios_existentes:
                print("El nombre de usuario ya está registrado.")
                establecer_nombre_jugador(nombre_usuario)
                return True, usuarios_existentes
            else:
                # Si el nombre de usuario no existe, agregarlo a los datos
                usuarios_existentes[nombre_usuario] = {
                    "Intentos": 3,
                    "Vida": 100,
                    "Escudo": 50,
                    "Proyectil": 0,
                    "Tiempo": "2:30",
                    "Puntaje": 0,
                    "Jugador": nombre_usuario  # Se usa el nombre como ID en este caso
                }
                # Escribir los datos actualizados en el archivo CSV
                with open(archivo_csv, 'w', newline='') as archivo:
                    nombres_columnas = ["Jugador", "Intentos", "Vida", "Escudo", "Proyectil", "Tiempo", "Puntaje"]
                    escritor_csv = csv.DictWriter(archivo, fieldnames=nombres_columnas)
                    escritor_csv.writeheader()
                    escritor_csv.writerows(usuarios_existentes.values())
                print("Nombre de usuario registrado con éxito.")
                establecer_nombre_jugador(nombre_usuario)
                return False, usuarios_existentes

    except FileNotFoundError:
        # Si el archivo CSV no existe, crear uno nuevo y agregar el nombre de usuario
        print("El archivo CSV no existe. Creando uno nuevo...")
        with open(archivo_csv, 'w', newline='') as archivo:
            nombres_columnas = ["Jugador", "Intentos", "Vida", "Escudo", "Proyectil", "Tiempo", "Puntaje"]
            escritor_csv = csv.DictWriter(archivo, fieldnames=nombres_columnas)
            escritor_csv.writeheader()
            escritor_csv.writerow({
                "Jugador": nombre_usuario,
                "Intentos": 3,
                "Vida": 100,
                "Escudo": 50,
                "Proyectil": 0,
                "Tiempo": "2:30",
                "Puntaje": 0
            })
        print("Nombre de usuario registrado con éxito.")
        establecer_nombre_jugador(nombre_usuario)
        return False, {nombre_usuario: {
            "Intentos": 3,
            "Vida": 100,
            "Escudo": 50,
            "Proyectil": 0,
            "Tiempo": "2:30",
            "Puntaje": 0,
            "Jugador": nombre_usuario
        }}