
from dataclasses import dataclass
from ai import AI
import plugins.plugin_factory

@dataclass
class CowsayPlugin:
    name = 'cowsay_plugin'

    def cowsay(self, message):
        print(f"moo {message}")

    def register(self, ai:AI):
        self.ai = ai
        print("registering cowsay plugin - after speaking") 
        self.ai.after_speaking.register(self.cowsay)   
        return self

def initialize():
    # register with Factory or plugin?
    plugins.plugin_factory.register(CowsayPlugin.name, CowsayPlugin)
    
    print("Cow Say Plugin initialized")