import pyjokes
from ai import AI


glados = AI(name="GlaDOS")

def joke():
    funny = pyjokes.get_joke(language="es")
    print(funny)
    glados.say(funny)
    
TRUE_STATE=True
    
command = ""
while TRUE_STATE and command != "adiós":
    command = glados.listen()
    
    print("Command was:", command)
    
    if command == "hola":
        joke()
        
glados.say("Goodbye")



