from eventhook import EventHook
from pyaudio import PyAudio, paInt16
from vosk import Model, KaldiRecognizer
import json
import pyttsx3

class AI():
    __name = ""
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        
        model = Model('model\\vosk-model-es-0.42') # path to model
        self.r = KaldiRecognizer(model, 16000)

        self.m = PyAudio()

        if name is not None:
            self.__name = name 

        self.audio = self.m.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.audio.start_stream()
            
        # Setup event hooks
        self.before_speaking = EventHook()
        self.after_speaking = EventHook()
        self.before_listening = EventHook()
        self.after_listening = EventHook()
        self.start = EventHook()
        self.stop = EventHook()
        
        self.start.trigger()
            
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
           
        phrase = ""
        
        if self.r.AcceptWaveform(self.audio.read(4096,exception_on_overflow = False)): 
            self.before_listening.trigger()
            phrase = self.r.Result()
            phrase = phrase.removeprefix('the ')
            
            phrase = str(json.loads(phrase)["text"])

            if phrase:
                self.after_listening.trigger(phrase)
            return phrase   

        return None
    
    def stop_ai(self):
        self.engine.stop()
        self.stop.trigger()
        print("IA parada")
            