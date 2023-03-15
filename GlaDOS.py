import sys
from ai import AI
import json
from skills import loader, factory
from plugins import plugin_loader, plugin_factory
from eventhook import EventHook

glados = AI(name="GlaDOS")

glados.start = EventHook()
glados.stop = EventHook()

# Load the skills
print("")
with open("./skills/skills.json") as f:
    data = json.load(f)
    loader.load_skills(data["plugins"])

skills = [factory.create(item) for item in data["skills"]]
print("")
print(f'Skills: {skills}')
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

ai_alive = True

while ai_alive and command not in ["adios","adiós"]:
    command = ""
    command = glados.listen()
    if command:
        command = command.lower()
        print(f'command heard: {command}') 
        for skill in skills:
            if command in skill.commands(command):
                skill.handle_command(command, glados)
                break
        


print('Parando la IA')
glados.stop_ai()
print(glados.name, "goes to sleep")




