import socket
import os.path
import datetime as dt
from skills.skills import Skill
from typing import Union, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



import hashlib


def str_to_hash(text: str, lon=16) -> str:
    hash_obj = hashlib.md5()
    text_bytes = text.encode('utf-8')
    
    hash_obj.update(text_bytes)
    
    result = hash_obj.hexdigest()[lon]
    
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

def normalize(s:str)->str:
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

def wav_name(skill: Skill, message:str = "", index: Optional[Union[None, str]] = None) -> str:
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


def main():
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open("token.json", "w") as token:
            token.write(creds.to_json()) 
        
    try:
        service = build("calendar", "v3", credentials=creds)
        
        now = dt.datetime.now().isoformat() + "Z"
        
        event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime").execute()
        events = event_result.get("items", [])
        
        if not events:
            print("No upcoming events found!")
            return
        
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
            
        calendar_id ="4dfd2a7ccdf7bceafc50dc8a37994de9f1e949d78487b53f992e100f33abf04b@group.calendar.google.com"
            
        event = {
            "summary": "Python Event",
            "start": {
                "dateTime": "2023-12-05T13:00:00+01:00",
                "timeZone": "Europe/Vienna"
            },
            "end": {
                "dateTime": "2023-12-05T15:00:00+01:00",
                "timeZone": "Europe/Vienna"
            },
            "recurrence": [
                "RRULE:FREQ=DAILY;"
            ]
        }
        
        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        
        print(f"Event created {event.get('htmlLink')}")
        
    except HttpError as error:
        print("An error ocurred:", error)
        
if __name__ == "__main__":
    main()