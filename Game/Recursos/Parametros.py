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

def crear_verificar_nombre_usuario(nombre_usuario, archivo_csv):
    usuarios_existentes = leer_datos_csv(archivo_csv)
    nombre_duplicado = nombre_usuario in usuarios_existentes

    if not nombre_duplicado:
        usuarios_existentes[nombre_usuario] = {
            "Nombre": nombre_usuario,
            "Intentos": 0,
            "Vida": 0,
            "Escudo": 0,
            "Proyectiles": 0,
            "Tiempo": 0,
            "Puntaje": 0
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

def actualizar_estadisticas(nombre_usuario, archivo_csv, intentos, vida, escudo, proyectiles, tiempo, puntaje):
    usuarios_existentes = leer_datos_csv(archivo_csv)

    if nombre_usuario in usuarios_existentes:
        usuarios_existentes[nombre_usuario].update({
            "Intentos": intentos,
            "Vida": vida,
            "Escudo": escudo,
            "Proyectiles": proyectiles,
            "Tiempo": tiempo,
            "Puntaje": puntaje
        })
        escribir_datos_csv(archivo_csv, usuarios_existentes)
    else:
        print(f"Error: el usuario {nombre_usuario} no existe en el archivo CSV.")

#===================================LECTURA Y GUARDADO DE NIVEL ==============================================#

def guardar_estadisticas_al_final_del_nivel(personaje, archivo_csv):
    usuarios_existentes = leer_datos_csv(archivo_csv)
    
    if personaje.nombre:
        # Verificar si el nombre del personaje ya existe en el diccionario
        if personaje.nombre in usuarios_existentes:
            # Actualizar los datos del personaje existente
            usuarios_existentes[personaje.nombre].update({
                "Intentos": personaje.intentos,
                "Vida": personaje.vida,
                "Escudo": personaje.escudo,
                "Proyectiles": personaje.proyectiles,
                "Puntaje": personaje.puntaje
            })
        else:
            # Agregar un nuevo personaje
            usuarios_existentes[personaje.nombre] = {
                "Nombre": personaje.nombre,
                "Intentos": personaje.intentos,
                "Vida": personaje.vida,
                "Escudo": personaje.escudo,
                "Proyectiles": personaje.proyectiles,
                "Puntaje": personaje.puntaje
            }
        
        # Guardar los datos actualizados en el CSV
        escribir_datos_csv(archivo_csv, usuarios_existentes)
    else:
        print("Error: El nombre del personaje está vacío.")


# def cargar_estadisticas_para_nuevo_nivel(nombre_usuario, archivo_csv):
#     # Leer los datos existentes
#     datos = leer_datos_csv(archivo_csv)

#     # Retornar las estadísticas del usuario
#     if nombre_usuario in datos:
#         return datos[nombre_usuario]
#     else:
#         return None


#===================================LECTURA Y GUARDADO DE GAME OVER ==============================================#