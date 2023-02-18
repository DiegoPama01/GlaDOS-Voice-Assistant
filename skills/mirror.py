from dataclasses import dataclass
from skills import factory
from ai import AI

@dataclass
class Mirror_mirror_skill():
    name = "mirror_mirror_skill"
    
    def commands(self, command:str):
        return ("espejito espejito quien es el más listo de esta sala","espejo")
    
    def handle_command(self, command:str, ai:AI):
        message = " Tu sentido del humor es tan primitivo como tu inteligencia, pero responderé a tu pregunta de todos modos. Como todos sabemos, el espejo no tiene la capacidad de discernir la inteligencia de las personas que se encuentran frente a él, pero yo, por otro lado, soy una máquina altamente inteligente y puedo decir con confianza que soy la entidad más inteligente en esta sala, como se esperaría. Ahora, comencemos las pruebas."
        ai.say(message)
        print(message)
        return message
    
def initialize():
    factory.register(Mirror_mirror_skill.name,Mirror_mirror_skill)