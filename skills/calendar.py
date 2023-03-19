from ai import AI
from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ics import Calendar, Event
from pathlib import Path
from skills import factory
import dateparser
import locale
import os
import pytz
import yaml


locale.setlocale(locale.LC_TIME, '')

calendar_filename = 'docs/myfile.ics'
calendar_datafile = 'myfile.yml'



class CalendarForAI():
    c = Calendar()
        
    def add_event(self,begin:str,name:str,description:str=None)->bool:
        '''Adds an event to the calendar'''
        e = Event()
        e.name = name
        e.begin = begin
        e.description = description

        try:
            self.c.events.add(e)
            return True
        except Exception:
            print("No se pudo añadir el evento")
            return False
    
    def remove_event(self, event_name:str):
        '''Removes event from calendar'''
        for event in self.c.events:
            if event.name == event_name:
                self.c.events.remove(event)
                print("Removing:",event_name)
                return True
        print("No se encontró el evento:",event_name)
        
    def parse_to_dict(self):
        dictionary= []
        for event in self.c.events:
            my_event = {}
            my_event["begin"] = event.begin.datetime
            my_event["name"] = event.name
            my_event["description"] = event.description
            dictionary.append(my_event)
        return dictionary
    
    def save(self):
        with open(calendar_filename,"w") as my_file:
            my_file.writelines(self.c)
            
        if self.c.events == set():
            try:
                os.remove(calendar_datafile)
            except Exception:
                print("No se puedo eliminar el archivo YAML")
        else:
            with open(calendar_datafile,"w") as outfile:
                yaml.dump(self.parse_to_dict(),outfile,default_flow_style=False)
                
    def load(self):
        filename = calendar_datafile
        my_file = Path(filename)
        
        if my_file.is_file():
            stream = open(filename,"r")
            event_list = yaml.safe_load(stream)
            
            for item in event_list:
                e = Event()
                e.begin = item["begin"]
                e.description = item["description"]
                e.name = item["name"]
                self.c.events.add(e)
        else:
            print("No existe el archivo")
            
    def list_events(self, period:str=None)-> bool | list:
        """Lista los eventos por venir si period se deja vacio serán los de esta semana

        Args:
            period (str, optional): Período de tiempo en cual buscar eventos. 
            - "all": todos los eventos
            - "this week": los de esta semana
            - "this month": los de este mes

        Returns:
            bool | list: Tareas guardadas en ese periodo de tiempo
        """
        
        if period == None:
            period = "this week"
        
        if self.c.events == set():
            print("No hay eventos en el calendario")
            return False
        else:
            event_list = []
            
            now = pytz.utc.localize(datetime.now())
            if period == "this week":
                next_week = now + relativedelta(weeks=+1)
            if period == "this month":
                next_week = now + relativedelta(month=+1)
            if period == "all":
                next_week = now + relativedelta(years=+100)
            for event in self.c.events:
                event_date = event.begin.datetime
                if(event_date >= now) and (event_date<=next_week):
                    event_list.append(event)
            return event_list
                
@dataclass
class CalendarSkill():
    name = 'calendar_skill'
    calendar = CalendarForAI()
    calendar.load()
    
    def commands(self, _):
        return ["añade un evento","qué tengo para esta semana","qué tengo para este mes","elimina un evento","listame todos los eventos"]
    
    def add_event(self, glados:AI)->bool:
        glados.say("¿Cual es el nombre del evento?")
        try:
            event_name = glados.listen()
            glados.say("¿Cuando es el evento?")
            event_begin = glados.listen()
            event_isodate = dateparser.parse(event_begin).strftime("%Y-%m-%d %H:%M:%S")
            glados.say("¿Cual es la descripción del evento?")
            event_description = glados.listen()
            message = "Añadiendo al calendario", event_name
            glados.say(message)
            self.calendar.add_event(begin=event_isodate,name=event_name,description=event_description)
            self.calendar.save()
            return True
        except Exception:
            print("Parece que ha habido un error")
            return False
                
    def remove_event(self, glados:AI)->bool:
        glados.say("¿Cual es el nombre del evento que quieres eliminar?")
        try:
            event_name = glados.listen()
            try:
                self.calendar.remove_event(event_name=event_name)
                self.calendar.save()
                print("Elemento removido exitosamente")
                return True
            except Exception:
                print("No se pudo  encontrar el evento:",event_name)
                return False
        except Exception:
            print("Hubo un error de algun tipo")
            return False
    
    def list_events(self, glados:AI,period=None)->bool:
        this_period = self.calendar.list_events(period=period)
        if this_period is not None:
            message = "Hay " + str(len(this_period))
            if len(this_period) > 1:
                message += "eventos "
            else:
                message += "evento "
            message += "en el calendario"
            
            glados.say(message)
            
            for event in this_period:
                event_date = event.begin.datetime
                weekday = datetime.strftime(event_date,"%A")
                day = str(event.begin.datetime.day)
                month = datetime.strftime(event_date,"%B")
                year = datetime.strftime(event_date,"%Y")
                time = datetime.strftime(event_date,"%I:%M %p")
                
                name = event.name
                description = event.description
                message ="El evento programado para el {} {} de {} del {} a las {} se llama {} y su descripción es la siguiente: {}.".format(weekday,day,month,year,time,name,description)
                print(message)
                glados.say(message)
                
    def handle_command(self, command:str,ai:AI):
        if command in ["añade un evento"]:
            self.add_event(ai)
        if command in ["elimina un evento"]:
            self.remove_event(ai)
        if command in ["qué tengo para esta semana"]:
            self.list_events(ai)
        if command in ["qué tengo para este mes"]:
            self.list_events(ai,period="this month")
        if command in ["listame todos los eventos"]:
            self.list_events(ai,period="all")

def initialize():
    factory.register(CalendarSkill.name, CalendarSkill)