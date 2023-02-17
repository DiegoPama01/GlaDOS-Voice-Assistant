import pyjokes, randfacts
from ai import AI
from todo import Item,Todo
from weather import Weather


glados = AI(name="GlaDOS")
todo = Todo()
weather = Weather()

def forecast():
    forecast = Weather.weather
    msg_forecast = '''
    Bienvenido al servicio meteorológico de Aperture Science. Mañana en tu ubicación 
    se espera un clima soleado y brillante, lo que será un cambio refrescante de la humedad 
    y las temperaturas extremas que hemos visto últimamente. Como siempre, recuerda que el 
    clima es impredecible y puede cambiar en cualquier momento, así que asegúrate de estar 
    preparado para cualquier eventualidad. Y recuerda, Aperture Science se preocupa por su 
    seguridad, incluso en condiciones climáticas extremas.
    '''
    print(forecast)
    glados.say(msg_forecast)

def joke():
    funny = pyjokes.get_joke(language="es")
    print(funny)
    glados.say(funny)
    
def facts():
    fact = randfacts.get_fact()
    print(fact)
    glados.say(fact)
    
    
def add_todo()->bool:
    item = Item()
    glados.say("Dime que debo añadir a la lista")
    try:
        item.title = glados.listen()
        todo.new_item(item)
        message = "Added " + item.title
        glados.say(message)
        return True
    except:
        print("Oops there was an error")
        return False
    
    
def list_todos():
    if len(todo) > 0:
        glados.say("Aqui están tus tareas")
        for item in todo:
            glados.say(item.title)
    else:
        glados.say("¡No tienes nada en tu lista de tareas!")
        
def remove_todo()-> bool:
    glados.say("Dime que tarea debo eliminar")
    try:
        item_title = glados.listen()
        print(item_title)
        todo.remove_item(title=item_title)
        message = "Removed "+ item_title
        glados.say(message)
        return True
    except:
        print("Opps there was an error")
        return False
        
    
TRUE_STATE=True
    
command = ""
while TRUE_STATE and command not in ["adios","adiós"]:
    try:
        command = glados.listen()
        command = command.lower()
    except:
        print("Oops there was an error")
        command = ""
    print("Command was:", command)
    
    if command in ["cuéntame un chiste"]:
        joke()
        command = ""
        
    if command in ["abre la lista de tareas", "añade a la lista de tareas"]:
        add_todo()
        command = ""
        
    if command in ["recuérdame las tareas", "dime las tareas"]:
        list_todos()
        command = ""
        
    if command in ["elimina una tarea", "tacha una tarea"]:
        remove_todo()
        command = ""
        
    if command in ["¿cómo está el día?", "¿cómo está el tiempo hoy?","dime como está el tiempo"]:
        forecast()
        command = ""
        
glados.say("Gracias por participar en nuestra Aperture Science Enrichment Center. Esperamos verte de nuevo pronto. Pero no demasiado pronto.")


forecast()



