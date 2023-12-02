import subprocess
import time
import pyautogui


ruta_melodyne = "C:\\Program Files\\Celemony\\Melodyne 5\\Melodyne.exe"






subprocess.Popen(ruta_melodyne)

time.sleep(5)

pyautogui.hotkey("ctrl", "o")

time.sleep(5)

pyautogui.write("espeak.wav")

time.sleep(5)

pyautogui.press("enter")

time.sleep(5)



# Color objetivo en formato (R, G, B)
color_objetivo = (255, 0, 0)  # Por ejemplo, rojo

# Tolerancia para la comparación de colores
tolerancia = 10

# Obtener la resolución de la pantalla principal
resolucion_principal = pyautogui.size()



# Buscar la posición del color en la pantalla
posicion = pyautogui.locateCenterOnScreen('captura_pantalla.png', region=(0, 0, resolucion_principal.width, resolucion_principal.height), grayscale=True)

# Verificar si se encontró la posición y el color coincide dentro de la tolerancia
if posicion:
    # Obtener las coordenadas del centro de la región encontrada
    x, y = posicion

    # Obtener el color en las coordenadas especificadas
    color_en_coord = pyautogui.pixel(x, y)

    # Verificar si el color coincide dentro de la tolerancia especificada
    if all(abs(a - b) <= tolerancia for a, b in zip(color_en_coord, color_objetivo)):
        # Hacer clic en las coordenadas del centro de la región
        pyautogui.click(x, y)


        
        

# time.sleep(5)

# pyautogui.hotkey("ctrl", "a")

# time.sleep(5)

# pyautogui.hotkey("shift", "r")

# pyautogui.doubleClick(236, 236)

# time.sleep(5)

# pyautogui.hotkey("shift", "t")

# time.sleep(5)

# pyautogui.hotkey("shift", "y")

# time.sleep(5)


