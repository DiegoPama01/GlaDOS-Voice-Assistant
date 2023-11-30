from dataclasses import dataclass
from skills import factory
from ai import AI

@dataclass
class MirrorMirrorSkill():
    name = "mirror_mirror_skill"
    
    def commands(self, _):
        return ("espejito espejito quien es el más listo de esta sala","espejo")
    
    def handle_command(self, _, ai:AI):
        message = "Las leyes federales me exigen que te recuerde que la siguiente cámara tiene...     muy buena pinta"
        ai.say(message)
        print(message)
        return message
    
def initialize():
    factory.register(MirrorMirrorSkill.name,MirrorMirrorSkill)