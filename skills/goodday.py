from dataclasses import dataclass
from datetime import datetime
from skills import factory
from ai import AI

@dataclass
class GoodDaySkill():
    name='goodday_skill'
    
    def commands(self,command:str):
        return ["hola","buen día","buenos días","buenas tardes","buenas noches"]
    
    def handle_command(self, command:str, ai:AI):
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <= 12:
            message = "Buenos días"
        if hr >= 12 <= 17:
            message = "Buenas tardes"
        if hr > 17:
            message = "Buenas noches"
        
        message = message + " Diego"
        ai.say(message)
        return self.name
    
def initialize():
    factory.register(GoodDaySkill.name,GoodDaySkill)