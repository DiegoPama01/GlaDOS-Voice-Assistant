from dataclasses import dataclass
import sys
import threading

import pygame
from skills import factory
from ai import AI
import random
from utils import wav_name


@dataclass
class SingSkill():
    name = "sing_skill"
    msg_list = []

    def commands(self, _):
        return ("canta algo", "puedes cantar algo", "cantame algo")

    def play_music(self, ai:AI):
        pygame.init()
        
        songs = ["db/songs/Want you gone.mp3", "db/songs/Still alive.mp3","db/songs/Cara mia addio.mp3"]

        # Ruta de la canción (modifica esto según tu estructura de archivos)
        song_path = random.choice(songs)
        
        # Inicia la reproducción de la canción
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        
        paused = False

        while pygame.mixer.music.get_busy() or paused:
            
            sentence = ai.listen()

            if "para" in sentence:

                pygame.mixer.music.pause()
                paused = True
                
                print("Song paused")

                
            if any(word in sentence for word in ("sigue", "continúa")):

                pygame.mixer.music.unpause()
                paused = False
                
                print("Song unpaused")


            if ("termina") in sentence:
                
                break
            
            # Espera para evitar un uso intensivo de la CPU
            
            pygame.time.Clock().tick(10)


        print("Song finished")
        
        # Detén pygame al finalizar
        pygame.quit()
        

    def handle_command(self, _, ai: AI):
        
        # Crear dos hilos
        song_thread = threading.Thread(target=self.play_music(ai))


       # Iniciar los hilos
        song_thread.start()


        return None


def initialize():
    factory.register(SingSkill.name, SingSkill)
