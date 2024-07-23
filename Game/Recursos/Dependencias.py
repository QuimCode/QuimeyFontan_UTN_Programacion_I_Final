from ..Menu_AR.Menu_Principal import Menu
from ..Menu_AR.Submenu_Menu import Submenu
from ..Menu_AR.Registro_Menu import SubmenuRegistro
from ..Menu_AR.Menu_GameOver import GameOver

nombre_global = "-Usuario No Registrado-"

def crear_instancia_de_menu(nombre_global):
    return Menu(nombre_global)

def crear_instancia_de_submenu(nombre_global):
    return Submenu(nombre_global)

def crear_instancia_de_submenuregistro():
    return SubmenuRegistro()

def crear_instancia_de_gameover():
    return GameOver(nombre_global)

# Usando las funciones para crear las instancias
instancia_de_menu = crear_instancia_de_menu(nombre_global)
instancia_de_submenu = crear_instancia_de_submenu(nombre_global)
instancia_de_submenuregistro = crear_instancia_de_submenuregistro()
instancia_de_gameover = crear_instancia_de_gameover()