import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'spanish')
        voices = self.engine.getProperty("voices")
        self.engine.setProperty('voice', voices[0].id) 
        
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        if name is not None:
            self.__name = name
            
        print("Listening")
        
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            self.r.energy_threshold = self.r.energy_threshold + 50
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()
            
    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
            
    def listen(self):
        print("Say something")
        with self.m as source:
            audio = self.r.listen(source)
                
        print("Got it") 
        phrase = ""        
        try:
            phrase = self.r.recognize_google(audio,language="es-ES",show_all=False)
            sentence = "Got it, you said" + phrase
            self.engine.say(sentence)
            #self.engine.save_to_file(sentence,"speech.wav")
            self.engine.runAndWait()
        except Exception as error:
            print("Sorry, didn't catch that", error)
            self.engine.say("Sorry, didn't catch that")
            self.engine.runAndWait()
        return phrase
        
            