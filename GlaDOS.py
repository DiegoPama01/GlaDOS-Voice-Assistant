from datetime import datetime
import pyjokes, randfacts
from ai import AI
from calendar_skill import Calendar_Skill
from todo_skill import Item,Todo
from weather_skill import Weather
import messages
import dateparser
import locale
locale.setlocale(locale.LC_TIME, '')


glados = AI(name="GlaDOS")

todo = Todo()
weather = Weather()
calendar = Calendar_Skill()
calendar.load()



def add_event()->bool:
    glados.say("¿Cual es el nombre del evento?")
    try:
        event_name = glados.listen()
        glados.say("¿Cuando es el evento?")
        event_begin = glados.listen()
        event_isodate = dateparser.parse(event_begin).strftime("%Y-%m-%d %H:%M:%S")
        glados.say("¿Cual es la descripción del evento?")
        event_description = glados.listen()
        message = "Añadiendo al calendario", event_name
        glados.say(message)
        calendar.add_event(begin=event_isodate,name=event_name,description=event_description)
        calendar.save()
        return True
    except:
        print("Parece que ha habido un error")
        return False
    
def remove_event()->bool:
    glados.say("¿Cual es el nombre del evento que quieres eliminar?")
    try:
        event_name = glados.listen()
        try:
            calendar.remove_event(event_name=event_name)
            calendar.save()
            print("Elemento removido exitosamente")
            return True
        except:
            print("No se pudo  encontrar el evento:",event_name)
            return False
    except:
        print("Hubo un error de algun tipo")
        return False
    
def list_events(period=None):
    this_period = calendar.list_events(period=period)
    if this_period is not None:
        message = "Hay " + str(len(this_period))
        if len(this_period) > 1:
            message += "eventos "
        else:
            message += "evento "
        message += "en el calendario"
        
        glados.say(message)
        
        for event in this_period:
            event_date = event.begin.datetime
            weekday = datetime.strftime(event_date,"%A")
            day = str(event.begin.datetime.day)
            month = datetime.strftime(event_date,"%B")
            year = datetime.strftime(event_date,"%Y")
            time = datetime.strftime(event_date,"%I:%M %p")
            
            name = event.name
            description = event.description
            message ="El evento programado para el {} {} de {} del {} a las {} se llama {} y su descripción es la siguiente: {}. Espero que este evento sea emocionante y lleno de ciencia innovadora, como todos los demás eventos que se llevan a cabo aquí en las instalaciones de Apertur Saiens".format(
                weekday,day,month,year,time,name,description
            )
            print(message)
            glados.say(message)

def forecast():
    forecast = Weather.weather
    msg_forecast = messages.FORECAST_MSG["spanish"]
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
        
    
life=True
    
command = ""
while life and command not in ["adios","adiós"]:
    try:
        command = glados.listen()
        command = command.lower()
    except:
        print("Oops there was an error")
        command = ""
        life = False
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
        
    if command in ["cómo está el día", "cómo está el tiempo hoy","dime como está el tiempo"]:
        forecast()
        command = ""
        
    if command in ["añade un evento"]:
        add_event()
        command = ""

    if command in ["qué tengo para esta semana"]:
        list_events()
        command = ""
    
    if command in ["elimina un evento"]:
        remove_event()
        command = ""
        
glados.say("Adiós")




