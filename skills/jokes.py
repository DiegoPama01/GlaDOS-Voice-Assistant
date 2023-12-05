from dataclasses import dataclass
from skills import factory
from ai import AI
import pyjokes
from utils import wav_name, str_to_hash

@dataclass
class JokesSkill():
    name = 'jokes_skill'
    msg_list = []
    
    def commands(self, _):
        return ['cuentame un chiste']
    
    def handle_command(self, _,ai:AI):
        joke = pyjokes.get_joke(language="en", category="all")
        ai.say(joke, wav_name(self,index=str_to_hash(joke)))
        return joke
    
def initialize():
    factory.register(JokesSkill.name,JokesSkill)