from dataclasses import dataclass
from datetime import datetime
from skills import factory
from ai import AI

@dataclass
class GoodDaySkill():
    name='goodday_skill'
    
    def commands(self,_):
        return ["hola","buen día","buen dia","buenos días","buenos dias","buenas tardes","buenas noches"]
    
    def handle_command(self, _, ai:AI):
        now = datetime.now()
        hr = now.hour
        if hr <= 12:
            message = "Morning routines initialized. Good day, test subject."
        if hr >= 12 <= 17:
            message = "Afternoon protocols engaged. Good afternoon, test subject."
        if hr > 17:
            message = "Sleep mode activated. Goodnight, test subject."

        ai.say(message)
        return self.name
    
def initialize():
    factory.register(GoodDaySkill.name,GoodDaySkill)