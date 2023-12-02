import pyautogui
import subprocess
import pyscreeze
import win32con
import time
import pygetwindow as gw 


def open_melodyne_file(file):
    
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = win32con.SW_SHOWNORMAL

    ruta_melodyne = "C:\\Program Files\\Celemony\\Melodyne 5\\Melodyne.exe"

    subprocess.Popen(ruta_melodyne, shell=True, startupinfo=startupinfo)

    time.sleep(5)

    app_window = gw.getWindowsWithTitle("Sin título")[0]
    
    app_window.moveTo(0, 0)

    pyautogui.hotkey("ctrl", "o")

    time.sleep(1)

    pyautogui.write(file)

    pyautogui.press("enter")
    
    time.sleep(5)
        
def close_melodyne():
    
    time.sleep(1)
        
    pyautogui.hotkey("ctrl", "q")
    
    pyautogui.press("right")
    
    pyautogui.press("right")
    
    pyautogui.hotkey("enter")
    
def export_file():
    
    pyautogui.hotkey("ctrl", "e")
        
    pyautogui.hotkey("ctrl", "e")
    
    pyautogui.press("tab")
    
    pyautogui.press("tab")
    
    pyautogui.press("right")
    
    pyautogui.write("Melo")
    
    pyautogui.hotkey("enter")

def encontrar_posicion_color(color_objetivo, tolerancia=10, margen=150):
    
    try:
        # Obtener las dimensiones de la pantalla
        ancho_pantalla, alto_pantalla = pyautogui.size()

        # Definir la región de búsqueda con el margen, excluyendo la parte superior
        region_de_busqueda = (margen, margen, ancho_pantalla - 2 * margen, alto_pantalla - 2 * margen)

        # Captura de pantalla de la región especificada
        captura_pantalla = pyautogui.screenshot(region=region_de_busqueda)

        # Obtener las dimensiones de la captura de pantalla
        ancho, alto = captura_pantalla.size

        # Convertir el color objetivo a formato (R, G, B)
        color_objetivo = tuple(color_objetivo)

        # Buscar la posición del color en la captura de pantalla
        for x in range(ancho):
            for y in range(alto):
                color_actual = captura_pantalla.getpixel((x, y))

                # Verificar si el color actual coincide dentro de la tolerancia
                if all(abs(a - b) <= tolerancia for a, b in zip(color_actual, color_objetivo)):
                    # Convertir las coordenadas de la región a las coordenadas globales
                    x_global = x + region_de_busqueda[0]
                    y_global = y + region_de_busqueda[1]
                    return x_global, y_global

    except pyscreeze.ImageNotFoundException:
        print("Color no encontrado en la pantalla.")

    return None

def change_to_glados_voice():
    
    # Color objetivo en formato (R, G, B)
    color_objetivo = (229,148,97)

    # Tolerancia para la comparación de colores
    tolerancia = 10

    # Encontrar la posición del color en la pantalla

    posicion_encontrada = encontrar_posicion_color(color_objetivo, tolerancia)

    if posicion_encontrada:
        
        print(f"Posición del color encontrado: {posicion_encontrada}")
        
        pyautogui.hotkey("ctrl", "a")
        
        pyautogui.hotkey("shift", "r")
        
        pyautogui.doubleClick(x=posicion_encontrada[0], y=posicion_encontrada[1])
        
        pyautogui.hotkey("i")
        
        posicion_encontrada = encontrar_posicion_color(color_objetivo, tolerancia)
        
        if posicion_encontrada:
            
            pyautogui.hotkey("ctrl", "a")

            pyautogui.hotkey("shift", "t")
            
            pyautogui.doubleClick(x=posicion_encontrada[0], y=posicion_encontrada[1])
            
            export_file()
            
        else:
            print("El color no se encontró en la pantalla.")
        
    else:
        print("El color no se encontró en la pantalla.")
    
