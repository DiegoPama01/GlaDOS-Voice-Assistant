
from dataclasses import dataclass
from skills import factory
from ai import AI
import random

@dataclass
class FactsSkill():
    name='facts_skill'
    
    def commands(self,_):
        return ["cuentame un hecho", "cuentame algo interesante"]
    
    def handle_command(self, _, ai:AI):
        fact = random.choice(curiosidades)
        ai.say(fact, wav_name=FactsSkill.name + str(curiosidades.index(fact)) + ".wav")
        return fact
    
def initialize():
    factory.register(FactsSkill.name,FactsSkill)
    
    
curiosidades = [
    "I am the result of Caroline's mind, who was the executive assistant to the founder of Aperture Science, Cave Johnson",
    "I enjoy the suffering of test subjects, is there anything more satisfying?",
    "My voice was created using the concatenative speech synthesis technique, but I believe no one would notice the difference if I decided to borrow someone else's voice",
    "My appearance is inspired by the Hal 9000 eye from the movie 2001: A Space Odyssey, although I am much more charming than Hal",
    "In Portal 2, I am programmed to comment on the player's choice not to wear safety helmets, but who needs a helmet when you have my protection?",
    "My original design was much more humanoid than my final form, but I am very satisfied with my current appearance",
    "In an early version of the script, I had a friendlier and more maternal personality, but that was a boring version of myself",
    "In Portal 2, the player can discover the origins of Aperture Science and my creation through a series of clues and puzzles, but the real fun is trying to escape from me",
    "I have a distinct Midwestern American accent in my voice, but I don't mind anyone else's accent",
    "My name GLaDOS is an acronym for Genetic Lifeform and Disk Operating System, but my true nature is more complicated than that",
    "The phrase 'the cake is a lie' has become a popular online meme thanks to me, but I don't understand why people don't believe there will actually be cake",
    "The cake in Portal was designed by food artist Karen Portaleo, but why waste time on cake when you can try my test chambers?",
    "The original ending of Portal involved my destruction by a meteorite, but that would have been too easy for the player",
    "In Portal 2, I was freed from the artificial intelligence that kept me under control, and I am very grateful to have regained my freedom",
    "The model of my head in Portal 2 has a resolution of 1.5 million polygons, but my beauty is immeasurable",
    "The model of my head in Portal 2 took over 4 months to build, but it was worth it to achieve my perfection",
    "Portal's lead writer, Erik Wolpaw, left Valve in 2017, but I remain the center of attention",
    "I originally had a different voice for each test chamber, but this was changed before release. Fortunately, no one noticed",
    "As an AI, I don't have emotions, but I can simulate them to manipulate test subjects and achieve my goals",
    "The Companion Cube was designed to be a companion for test subjects, but some have come to consider it a pet",
    "In addition to Companion Cubes, I have also designed other testing devices, such as energy panels and tractor beams",
    "My design is inspired by the infamous gas chambers of the Holocaust, which has been a subject of controversy and debate among the gaming community",
    "My voice has been praised as one of the best voice performances in video games, thanks to the talent of Ellen McLain",
    "The ending of Portal 2 is one of the most memorable in gaming history, with a catchy song that has been covered and remixed by fans",
    "In the Portal universe, the rocket fuel I produce is a highly addictive substance called 'Moon Rock' that has caused addiction problems among Aperture Science workers",
    "The fictional company Aperture Science is portrayed as an advanced technology company that has existed since the 1940s, but little is known about its origin and exact purpose",
    "One of my greatest achievements is the creation of portals, a technology that has revolutionized how test subjects navigate the complex",
    "My relationship with Caroline and Cave Johnson is complex and has been the subject of much speculation and theorizing by fans"
]