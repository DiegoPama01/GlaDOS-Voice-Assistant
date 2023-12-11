import os
import socket
from datetime import datetime as dt
from skills.skills import Skill
from typing import Union, Optional
from word2number import w2n
import re
from googletrans import Translator

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import dateparser


import hashlib


def str_to_hash(text: str, lon=16) -> str:
    hash_obj = hashlib.md5()
    text_bytes = text.encode('utf-8')

    hash_obj.update(text_bytes)

    result = hash_obj.hexdigest()[:lon]

    return result


def obtener_ip():
    try:
        # Obtiene el nombre del host y la dirección IP asociada
        nombre_host = socket.gethostname()
        direccion_ip = socket.gethostbyname(nombre_host)
        return direccion_ip
    except socket.error as e:
        print(f"No se pudo obtener la dirección IP: {e}")
        return None


def normalize(s: str) -> str:
    """Elimina las tildes de una cadena y devuelve esa cadena normalizada

    Args:
        s (str): El string a normalizar

    Returns:
        str: El string normalizado
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def wav_name(skill: Skill, message: str = "", index: Optional[Union[None, str]] = None) -> str:
    """Devuelve el nombre del archivo .wav necesario

    Args:
        skill (Skill): Funcionalidad que ha llamado a este método
        message (_type_): Texto que quiere ser producido
        index (_type_, optional): Indice que distingue al texto dentro del grupo de funcionalidad al que pertenece. 
        Si no se llena, usa por defecto el indice interno de la lista de mensajes

    Returns:
        str: Nombre del archivo .wav
    """

    if index == None:
        wav_file = skill.name + str(skill.msg_list.index(message)) + ".wav"
    else:
        wav_file = skill.name + index + ".wav"

    return wav_file


SCOPES = ["https://www.googleapis.com/auth/calendar"]





def recognized_date(raw_string: str):
    try:
        hoy = dateparser.parse(raw_string, languages=['es'])
    except AttributeError as e:
        print(e)
        return None

    return hoy



def change_str_with_number(texto):
    palabras = texto.split()
    traductor = Translator()

    for i, palabra in enumerate(palabras):
        try:
            numero = w2n.word_to_num(palabra)
            palabras[i] = str(numero)
        except ValueError:
            # Si la palabra no es un número, intenta traducirla a inglés y convertirla
            palabra_ingles = traductor.translate(palabra, src='es', dest='en').text
            try:
                numero_ingles = w2n.word_to_num(palabra_ingles)
                palabras[i] = str(numero_ingles)
            except ValueError:
                pass  # Si no se puede convertir, deja la palabra sin cambios

    # Modificación para agregar ":" entre números consecutivos sin espacios adicionales
    for i in range(len(palabras) - 1):
        if palabras[i].isdigit() and palabras[i + 1].isdigit():
            palabras[i] += ":"

    # Eliminar espacios adicionales y unir las palabras
    resultado = ' '.join(palabras)
    resultado = resultado.replace(": ", ":")
    
    
    resultado = resultado.replace("de la mañana", "AM")
    
    resultado = resultado.replace("de la tarde", "PM").replace("del mediodia", "PM").replace("de la noche", "PM")


    return resultado




def main():
    
    texto_original = "Hoy a las trece cuarenta de la mañana"
    resultado = change_str_with_number(texto_original)
    print(resultado)

    
  
    
    # service.events().insert(calendarId=CALENDAR_ID, body=ejemplo).execute()


if __name__ == "__main__":
    main()
