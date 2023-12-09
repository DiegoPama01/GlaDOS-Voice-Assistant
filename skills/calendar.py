from ai import AI
from dataclasses import dataclass
from datetime import datetime, timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from skills import factory
from utils import wav_name, recognized_date, change_str_with_number
import os
import datetime as dt


locale = 'es'

SCOPES = ["https://www.googleapis.com/auth/calendar"]


@dataclass
class CalendarSkill():
    name = 'calendar_skill'
    msg_list = [
        "What will the event be called?",
        "What day will it start?",
        "Event added",
        "When will this event start?",
        "Sorry, I did not hear it. Can you repeat?",
        "How long will it last?",
        "What event do you want to remove?"
    ]

    def commands(self, _):
        return ["añade un evento", "que tengo para esta semana", "que tengo para este mes", "elimina un evento", "listame todos los eventos", "que tengo para hoy"]

    def add_event(self, glados: AI) -> bool:
        try:
            
            all_day = False

            # Pillar el nombre del evento

            glados.say(self.msg_list[0], wav_name(self, self.msg_list[0]))

            event_name = ""

            while event_name == "":
                event_name = glados.listen()

            # Pillar dia del evento

            glados.say(self.msg_list[1], wav_name(self, self.msg_list[1]))

            event_date = None

            while event_date == None:

                event_date = ""

                while event_date == "":
                    event_date = glados.listen()
                    event_date = change_str_with_number(event_date)
                    print(event_date)

                event_date = recognized_date(event_date)

                if event_date == None:
                    # Aqui el say que le dice que no se ha entendido
                    glados.say(self.msg_list[4], wav_name(
                        self, self.msg_list[4]))
                    
            # Pillar duración del evento

            glados.say(self.msg_list[5], wav_name(self, self.msg_list[5]))

            event_duration = None

            while event_duration == None:

                event_duration = ""

                while event_duration == "":
                    event_duration = glados.listen()
                    event_duration = change_str_with_number(event_duration)
                    print(event_duration)
                    
                    
                if event_duration == "todo el día":
                    all_day = True
                    break
                    

                event_duration = recognized_date(event_duration)

                if event_duration == None:
                    # Aqui el say que le dice que no se ha entendido
                    glados.say(self.msg_list[4], wav_name(
                        self, self.msg_list[4]))

            # Pillar hora del evento


            if not all_day:
                glados.say(self.msg_list[3], wav_name(self, self.msg_list[3]))

                event_time = None

                while event_time == None:

                    event_time = ""

                    while event_time == "":
                        event_time = glados.listen()
                        event_time = change_str_with_number(event_time)
                        print(event_time)

                    event_time = recognized_date(event_time)

                    if event_time == None:
                        # Aqui el say que le dice que no se ha entendido
                        glados.say(self.msg_list[4], wav_name(
                            self, self.msg_list[4]))

                # Añadir evento al calendario

                calendar.create_event(event_name, event_date,
                                    event_time, event_duration)
            else:
                calendar.create_event(event_name, event_date)

            # Dar feedback

            glados.say(self.msg_list[2], wav_name(self, self.msg_list[2]))
            return True
        except Exception as ex:
            print("Parece que ha habido un error", ex)
            return False

    def remove_event(self, glados: AI) -> bool:
        glados.say(self.msg_list[6], wav_name(self, self.msg_list[6]))
        try:
            event_name = glados.listen()
            try:
                calendar.remove_event(event_name)
                print("Elemento removido exitosamente")
                return True
            except Exception:
                print("No se pudo encontrar el evento:", event_name)
                return False
        except Exception:
            print("Hubo un error de algun tipo")
            return False

    def list_events(self, glados: AI, period = "") -> bool:
        if period == "diario":
            calendar.list_events(period)
        if period == "semanal":
            calendar.list_events(period)
        if period == "mensual":
            calendar.list_events(period)
        else:
            calendar.list_events()

    def handle_command(self, command: str, ai: AI):
        if command in ["añade un evento"]:
            self.add_event(ai)
        if command in ["elimina un evento"]:
            self.remove_event(ai)
        if command in ["que tengo para hoy"]:
            self.list_events(ai, "diario")
        if command in ["que tengo para esta semana"]:
            self.list_events(ai, "semanal")
        if command in ["que tengo para este mes"]:
            self.list_events(ai, "mensual")
        if command in ["listame todos los eventos"]:
            self.list_events(ai)


class CalendarCreds():
    creds = None
    service = None

    TOKEN_DIR = "token.json"
    CREDENTIALS_DIR = "credentials.json"
    CALENDAR_ID = "4dfd2a7ccdf7bceafc50dc8a37994de9f1e949d78487b53f992e100f33abf04b@group.calendar.google.com"

    def __init__(self) -> None:
        print("Obtaining Google Calendar credentials")

        if os.path.exists(self.TOKEN_DIR):
            self.creds = Credentials.from_authorized_user_file(self.TOKEN_DIR)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDENTIALS_DIR, SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open(self.TOKEN_DIR, "w") as token:
                token.write(self.creds.to_json())

        self.service = build("calendar", "v3", credentials=self.creds)

    def list_events(self, period: str):
        try:
            # Obtén la fecha actual en formato ISO 8601
            today = datetime.utcnow().isoformat() + 'Z'
            
            if period == "semanal":
                # Define el rango de tiempo para la búsqueda (semanal)
                end_of_day = (datetime.utcnow() + timedelta(weeks=1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ).isoformat() + 'Z'
                
                # Realiza la búsqueda de eventos para hoy
                events_result = self.service.events().list(
                    calendarId=self.CALENDAR_ID,
                    timeMin=today,
                    timeMax=end_of_day,
                    singleEvents=True,
                    orderBy='startTime'
                ).execute()
                
            elif period == "mensual":
                # Define el rango de tiempo para la búsqueda (mensual)
                end_of_day = (datetime.utcnow() + timedelta(month=1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ).isoformat() + 'Z'
                
                # Realiza la búsqueda de eventos para hoy
                events_result = self.service.events().list(
                    calendarId=self.CALENDAR_ID,
                    timeMin=today,
                    timeMax=end_of_day,
                    singleEvents=True,
                    orderBy='startTime'
                ).execute()
                
            elif period == "diario":
                # Define el rango de tiempo para la búsqueda (hoy)
                end_of_day = (datetime.utcnow() + timedelta(days=1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ).isoformat() + 'Z'
                
                # Realiza la búsqueda de eventos para hoy
                events_result = self.service.events().list(
                    calendarId=self.CALENDAR_ID,
                    timeMin=today,
                    timeMax=end_of_day,
                    singleEvents=True,
                    orderBy='startTime'
                ).execute()
            else:
                # Realiza la búsqueda de todos los eventos
                events_result = self.service.events().list(
                    calendarId=self.CALENDAR_ID,
                    singleEvents=True,
                    orderBy='startTime'
                ).execute()
            
            
            events = events_result.get('items', [])
            
            if not events:
                print('No hay eventos programados para hoy.')
            else:
                print('Eventos de hoy:')
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    print(f"{start} - {event['summary']}")
        except HttpError as error:
            print("An error ocurred:", error)

    def create_event(self, summary: str, start_day: datetime, start_time = "", event_duration="todo el dia"):

        if event_duration == "todo el dia":

            event = {
                "summary": summary,
                "start": {
                    "date": start_day.strftime('%Y-%m-%d'),
                },
                "end": {
                    "date": start_day.strftime('%Y-%m-%d'),
                }
            }

            event = self.service.events().insert(
                calendarId=self.CALENDAR_ID, body=event).execute()
        else:

            start_datetime = datetime.combine(
                start_day.date(), start_time.time())

            # Tomar la fecha y hora actual como referencia para la duración
            
            now = datetime.now()

            duration_delta = abs(event_duration - now)

            end_datetime = start_datetime + duration_delta

            # Crear el evento
            event = {
                "summary": summary,
                "start": {
                    "dateTime": start_datetime.isoformat(),
                    "timeZone": "Europe/Vienna"
                },
                "end": {
                    "dateTime": end_datetime.isoformat(),
                    "timeZone": "Europe/Vienna"
                }
            }

            # Insertar el evento en el calendario
            event = self.service.events().insert(
                calendarId=self.CALENDAR_ID, body=event).execute()

    def remove_event(self, event_name: str):
        events_result = self.service.events().list(calendarId=self.CALENDAR_ID, q=event_name).execute()
        events = events_result.get('items', [])
        if events:
            event_to_delete = events[0]
            self.service.events().delete(calendarId=self.CALENDAR_ID, eventId=event_to_delete['id']).execute()
            print(f'Evento "{event_name}" eliminado con éxito.')
        else:
            print(f'No se encontraron eventos con el nombre "{event_name}".')


calendar = CalendarCreds()


def initialize():
    factory.register(CalendarSkill.name, CalendarSkill)
