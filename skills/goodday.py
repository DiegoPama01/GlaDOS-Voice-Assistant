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
        index = ""
        if hr <= 12:
            message = "Morning routines initialized. Good day, test subject."
            index = "0"
        if hr >= 12 <= 17:
            message = "Afternoon protocols engaged. Good afternoon, test subject."
            index = "1"
        if hr > 17:
            message = "Sleep mode activated. Goodnight, test subject."
            index = "2"

        ai.say(message, GoodDaySkill.name + index + ".wav")
        return self.name
    
def initialize():
    factory.register(GoodDaySkill.name,GoodDaySkill)