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



#===================================LECTURA Y CREACION DE DATOS EN CSV ==============================================#

def leer_datos_csv(archivo_csv):
    try:
        with open(archivo_csv, 'r', newline='') as archivo:
            lector_csv = csv.DictReader(archivo)
            usuarios_existentes = {fila["Nombre"]: fila for fila in lector_csv}
            return usuarios_existentes
    except FileNotFoundError:
        return {}

def escribir_datos_csv(archivo_csv, datos):
    fieldnames = ["Nombre", "Intentos", "Vida", "Escudo", "Proyectiles", "Tiempo", "Puntaje"]
    with open(archivo_csv, mode='w', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos.values())

def append_datos_csv(archivo_csv, datos):
    fieldnames = ["Nombre", "Intentos", "Vida", "Escudo", "Proyectiles", "Tiempo", "Puntaje"]
    with open(archivo_csv, mode='a', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
        if archivo.tell() == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow(datos)

def crear_verificar_nombre_usuario(nombre_usuario, archivo_csv):
    usuarios_existentes = leer_datos_csv(archivo_csv)
    nombre_duplicado = nombre_usuario in usuarios_existentes

    if not nombre_duplicado:
        usuarios_existentes[nombre_usuario] = {
            "Nombre": nombre_usuario,
            "Intentos": None,
            "Vida": None,
            "Escudo": None,
            "Proyectiles": None,
            "Tiempo": None,
            "Puntaje": None,
        }
        escribir_datos_csv(archivo_csv, usuarios_existentes)

    return nombre_duplicado, usuarios_existentes

def obtener_ultimo_nombre_usuario(archivo_csv):
    """
    Lee el archivo CSV y devuelve el último nombre de usuario registrado.
    """
    ultimo_nombre = None
    try:
        with open(archivo_csv, 'r', newline='') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                nombre = fila.get("Nombre")
                if nombre:
                    ultimo_nombre = nombre
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_csv} no existe.")
    return ultimo_nombre



#===================================LECTURA Y GUARDADO DE NIVEL ==============================================#

def guardar_estadisticas_al_final_del_nivel(personaje, nivel, archivo_csv):
    if personaje.nombre:
        usuarios_existentes = leer_datos_csv(archivo_csv)
        usuarios_existentes[personaje.nombre] = {
            "Nombre": personaje.nombre,
            "Intentos": personaje.intentos,
            "Vida": personaje.vida,
            "Escudo": personaje.escudo,
            "Proyectiles": personaje.proyectiles,
            "Tiempo": nivel.tiempo_restante,
            "Puntaje": personaje.puntaje
        }
        escribir_datos_csv(archivo_csv, usuarios_existentes)
    else:
        print("Error: El nombre del personaje está vacío.")

def cargar_datos_jugador(nombre_jugador, archivo_csv):
    usuarios_existentes = leer_datos_csv(archivo_csv)
    if nombre_jugador in usuarios_existentes:
        return usuarios_existentes[nombre_jugador]
    else:
        print(f"No se encontraron datos para el jugador {nombre_jugador}")
        return None


#===================================LECTURA Y GUARDADO DE GAME OVER ==============================================

# def convertir_tiempo_a_formato_minutos(segundos):
#     minutos = segundos // 60
#     segundos_restantes = segundos % 60
#     return f"{minutos:02}:{segundos_restantes:02}"
