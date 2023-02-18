import pyttsx3
import speech_recognition as sr
from eventhook import Event_hook
from threading import Thread, Lock

class AI():
    __name = ""
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'spanish')
        
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        if name is not None:
            self.__name = name

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            
        # Setup event hooks
        self.before_speaking = Event_hook()
        self.after_speaking = Event_hook()
        self.before_listening = Event_hook()
        self.after_listening = Event_hook()
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        sentence = "Hola, mi nombre es " + self.__name
        self.engine.say(sentence)
        self.engine.runAndWait()
            
    def say(self, sentence):
        self.before_speaking.trigger(sentence)
        self.engine.say(sentence)
        self.engine.runAndWait()
        self.after_speaking.trigger(sentence)
    
            
    def listen(self):
        print("Di algo")
        self.before_listening.trigger()
        with self.m as source:
            audio = self.r.listen(source)
                
        print("Entendido") 
        phrase = ""        
        try:
            phrase = self.r.recognize_google(audio,language="es-ES",show_all=False)
            self.after_listening.trigger(phrase)
            sentence = "Creo que ha dicho " + phrase
            self.engine.say(sentence)
            #self.engine.save_to_file(sentence,"speech.wav")
            self.engine.runAndWait()
        except Exception as error:
            print("Lo siento no te he entendido", error)
            self.engine.say("Lo siento no te he entendido")
            self.engine.runAndWait()
        return phrase
    
    def stop_ai(self):
        self.engine.stop()
        print("stopped engine")
            