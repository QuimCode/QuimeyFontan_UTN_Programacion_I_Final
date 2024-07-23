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

#===================================LECTURA Y CREACION DE DATOS EN CSV ==============================================#

def leer_datos_csv(archivo_csv):
    try:
        with open(archivo_csv, 'r', newline='') as archivo:
            lector_csv = csv.DictReader(archivo)
            usuarios_existentes = {fila["Jugador"]: fila for fila in lector_csv}
            return usuarios_existentes
    except FileNotFoundError:
        return {}

def escribir_datos_csv(archivo_csv, datos):
    with open(archivo_csv, 'w', newline='') as archivo:
        nombres_columnas = ["Jugador", "Intentos", "Vida", "Escudo", "Proyectiles", "Tiempo", "Puntaje"]
        escritor_csv = csv.DictWriter(archivo, fieldnames=nombres_columnas)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos.values())

def crear_verificar_nombre_usuario(nombre_usuario, archivo_csv):
    global nombre_jugador_global
    
    usuarios_existentes = leer_datos_csv(archivo_csv)

    if nombre_usuario in usuarios_existentes:
        print("El nombre de usuario ya está registrado.")
        establecer_nombre_jugador(nombre_usuario)
        return True, usuarios_existentes
    else:
        usuarios_existentes[nombre_usuario] = {
            "Intentos": 0,
            "Vida": 0,
            "Escudo": 0,
            "Proyectiles": 0,
            "Tiempo": "2:30",
            "Puntaje": 0,
            "Jugador": nombre_usuario
        }
        escribir_datos_csv(archivo_csv, usuarios_existentes)
        print("Nombre de usuario registrado con éxito.")
        establecer_nombre_jugador(nombre_usuario)
        return False, usuarios_existentes

#===================================LECTURA Y GUARDADO DE NIVEL ==============================================#

def guardar_estadisticas_al_final_del_nivel(nombre_usuario, archivo_csv, intentos, vida, escudo, proyectiles, puntaje):
    # Leer los datos existentes
    datos = leer_datos_csv(archivo_csv)

    # Actualizar las estadísticas del usuario
    if nombre_usuario in datos:
        datos[nombre_usuario]["Intentos"] = intentos
        datos[nombre_usuario]["Vida"] = vida
        datos[nombre_usuario]["Escudo"] = escudo
        datos[nombre_usuario]["Proyectiles"] = proyectiles
        datos[nombre_usuario]["Puntaje"] = puntaje

    # Escribir los datos actualizados de vuelta en el archivo CSV
    escribir_datos_csv(archivo_csv, datos)

def cargar_estadisticas_para_nuevo_nivel(nombre_usuario, archivo_csv):
    # Leer los datos existentes
    datos = leer_datos_csv(archivo_csv)

    # Retornar las estadísticas del usuario
    if nombre_usuario in datos:
        return datos[nombre_usuario]
    else:
        return None


#===================================LECTURA Y GUARDADO DE GAME OVER ==============================================#