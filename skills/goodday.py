from dataclasses import dataclass
from datetime import datetime
from skills import factory
from ai import AI
from utils import wav_name


@dataclass
class GoodDaySkill():
    name = 'goodday_skill'
    msg_list = [
    "Morning routines initialized. Good day, test subject.",
    "Afternoon protocols engaged. Good afternoon, test subject.",
    "Sleep mode activated. Goodnight, test subject."
]

    def commands(self, _):
        return ["hola", "buen día", "buen dia", "buenos días", "buenos dias", "buenas tardes", "buenas noches"]

    def handle_command(self, _, ai: AI):
        hr = datetime.now().hour
        
        if hr <= 12:
            message = self.msg_list[0]
        if hr >= 12 <= 17:
            message = self.msg_list[1]
        if hr > 17:
            message = self.msg_list[2]
            
        ai.say(message, wav_name= wav_name(self,message))

        return self.name


def initialize():
    factory.register(GoodDaySkill.name, GoodDaySkill)



