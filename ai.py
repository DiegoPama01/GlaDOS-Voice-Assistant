from eventhook import EventHook
from pyaudio import PyAudio, paInt16
from vosk import Model, KaldiRecognizer
import melodyne_voice_change as mvc
import json
import pyttsx3
import pygame
import os

THRESHOLD_VALUE = 0.6
class AI():
    __name = ""
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        self.engine.setProperty('rate',160)
        
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
            
    def say(self, sentence, wav_name=None):
        
        if wav_name == None:
            wav_name = sentence + ".wav"
             
        route = "C:\\Users\\diego\\MelodyneWavs\\" + wav_name
        
        self.before_speaking.trigger(sentence)
        
        # Si no existe el archivo modificado se crea
        
        if not os.path.exists(route):
        
            self.engine.save_to_file(sentence, "db\\sentences\\" + wav_name)
            
            self.engine.runAndWait()
            
            mvc.open_melodyne_file(wav_name)
            
            mvc.change_to_glados_voice()
            
            mvc.close_melodyne()
            
            
        # Una vez creado el archivo se reproduce
        
        pygame.mixer.init()
        
        pygame.mixer.music.load(route)
        
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        self.after_speaking.trigger(sentence)
    
    def listen(self):
           
        phrase = ""
        
        while phrase == "":
        
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
            