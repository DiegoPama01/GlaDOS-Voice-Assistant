from dataclasses import dataclass
from skills import factory
from ai import AI
import pyjokes

@dataclass
class Jokes_skill():
    name = 'jokes_skill'
    
    def commands(self, command:str):
        return ['cuéntame un chiste']
    
    def handle_command(self, command:str,ai:AI):
        joke = pyjokes.get_joke(language="es")
        ai.say(joke)
        return joke
    
def initialize():
    factory.register(Jokes_skill.name,Jokes_skill)