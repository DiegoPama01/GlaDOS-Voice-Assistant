import audioFile
import pyttsx3
import pyaudio

# Configuración de eSpeak
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Velocidad de habla en palabras por minuto

engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

# Configuración de PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)

def text_to_speech(text, filename="sentence.wav"):
    # Generar audio con eSpeak
    engine.save_to_file(text,filename)
    engine.runAndWait()
    engine.stop()

# Ejemplo de uso
text_to_speech('I am confused',"espeak.wav")
audioFile.AudioFile("espeak.wav").play()

engine.save_to_file('I am confused', 'db\\I am confused.wav')
engine.runAndWait()