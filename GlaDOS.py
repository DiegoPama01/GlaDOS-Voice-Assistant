from ai import AI
import json
from skills import loader, factory
from plugins import plugin_loader, plugin_factory
from eventhook import EventHook
from utils import normalize;
from threading import Timer


timer = None


def enable_listening_for_name():
    global listening_for_name
    print("Se activa el timer")
    listening_for_name = True
    
def reset_timer():
    global timer
    if timer:
        timer.cancel()  # Cancela el temporizador existente
        enable_listening_for_name()  # Reinicia el temporizador

glados = AI(name="GlaDOS")

glados.start = EventHook()
glados.stop = EventHook()

# Load the skills
print("")
with open("./skills/skills.json") as f:
    data = json.load(f)
    loader.load_skills(data["plugins"])


glados.__skill = [factory.create(item) for item in data["skills"]]
print("")
print(f'Skills: {glados.__skill}')
print("")
# Load the plugins
print("")
with open("./plugins/plugins.json") as f:
    plugin_data = json.load(f)
    plugin_loader.load_plugins(plugin_data["plugins"])
    
plugins = [plugin_factory.create(item) for item in plugin_data["items"]]
print("")
print(f'Plugins: {plugin_data["plugins"]}')
print("")
# Register all the plugins
for item in plugins:
    item.register(glados)

glados.start.trigger()

command = ""
listening_for_name = True

enable_listening_for_name()


while command not in ["adiós"]:
    
    if listening_for_name:
        glados.listen_for_name()
        listening_for_name = False
        glados.play("db/sounds/OkGoogle.mp3")
    else:
        command = ""
        command = glados.listen()
        if command:
            command = command.lower()
            command_normalized = normalize(command)
            
            print(f'command heard: {command}')
            print(f'command normalized: {command_normalized}') 
            for skill in glados.__skill:
                if command_normalized in skill.commands(command_normalized):
                    skill.handle_command(command_normalized, glados)
                    break
             
            timer = Timer(40, enable_listening_for_name)
            timer.start()   
            
timer.cancel()

print('Parando la IA')
glados.stop_ai()
print(glados.name, "goes to sleep")