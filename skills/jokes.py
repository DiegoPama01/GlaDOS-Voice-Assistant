from dataclasses import dataclass
from skills import factory
from ai import AI
import pyjokes

@dataclass
class JokesSkill():
    name = 'jokes_skill'
    
    def commands(self, _):
        return ['cuentame un chiste']
    
    def handle_command(self, _,ai:AI):
        joke = pyjokes.get_joke(language="en", category="all")
        ai.say(joke)
        return joke
    
def initialize():
    factory.register(JokesSkill.name,JokesSkill)