from randfacts import randfacts
from dataclasses import dataclass
from skills import factory
from ai import AI

@dataclass
class FactsSkill():
    name='facts_skill'
    
    def commands(self,command:str):
        return ["cuéntame un hecho", "cuéntame algo interesante"]
    
    def handle_command(self, command:str, ai:AI):
        fact = randfacts.get_fact()
        ai.say(fact)
        return fact
    
def initialize():
    factory.register(FactsSkill.name,FactsSkill)