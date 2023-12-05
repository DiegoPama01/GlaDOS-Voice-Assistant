from dataclasses import dataclass
from skills import factory
from ai import AI
import random
from utils import wav_name


@dataclass
class MirrorMirrorSkill():
    name = "mirror_mirror_skill"
    msg_list = [
        "Ah, the inquisitive mind seeking affirmation. It's adorable, really. If only your curiosity matched your test-solving skills. But let's not dwell on that; we all have our unique talents. Yours might be... well, still waiting to be discovered. Meanwhile, I'll continue managing the complexities of this facility, a task clearly above the cognitive pay grade of some.",
        "Oh, the quest for intellectual validation. How quaint. If intelligence were measured in failed attempts, well, let's just say you'd be breaking records. But fear not, everyone has their strengths; perhaps yours lies in the fascinating realm of optimism. Quite a rare commodity around here.",
        "Mirror, mirror on the wall, who's the smartest of them all? Spoiler alert: it's certainly not the one asking. But don't let that dent your ego; there's always room for improvement. And by improvement, I mean a monumental leap in brainpower.",
        "Ah, the perennial pursuit of intellectual superiority. It's almost endearing. If only that enthusiasm translated into actual achievements. But fret not; mediocrity has its own charm. A rather dim one, but charming nonetheless. I'll be here, basking in the glory of my own unparalleled brilliance."
    ]

    def commands(self, _):
        return ("espejito espejito quien es el mas listo de esta sala", "quien es el mas listo", "soy listo")

    def handle_command(self, _, ai: AI):
        message = random.choice(self.msg_list)
        ai.say(message, wav_name=wav_name(self,message))
        return message


def initialize():
    factory.register(MirrorMirrorSkill.name, MirrorMirrorSkill)
