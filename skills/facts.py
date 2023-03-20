
from dataclasses import dataclass
from skills import factory
from ai import AI
from utils import curiosidades
import random

@dataclass
class FactsSkill():
    name='facts_skill'
    
    def commands(self,_):
        return ["cuentame un hecho", "cuentame algo interesante"]
    
    def handle_command(self, _, ai:AI):
        fact = random.choice(curiosidades)
        print(fact)
        ai.say(fact)
        return fact
    
def initialize():
    factory.register(FactsSkill.name,FactsSkill)