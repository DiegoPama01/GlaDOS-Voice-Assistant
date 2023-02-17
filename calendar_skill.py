from ics import Calendar, Event
from pathlib import Path
import os
import yaml
from datetime import datetime
from dateutil.relativedelta import *
import pytz


calendar_filename = 'docs/myfile.ics'
calendar_datafile = 'myfile.yml'

class Calendar_Skill():
    c = Calendar()
    
    def __init__(self):
        '''Print a nice banner'''
        print("*"*50)
        print("Calendar Skill Loaded")
        print("*"*50)
        
    def add_event(self,begin:str,name:str,description:str=None)->bool:
        '''Adds an event to the calendar'''
        e = Event()
        e.name = name
        e.begin = begin
        e.description = description

        try:
            self.c.events.add(e)
            return True
        except:
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
        dict= []
        for event in self.c.events:
            my_event = {}
            my_event["begin"] = event.begin.datetime
            my_event["name"] = event.name
            my_event["description"] = event.description
            dict.append(my_event)
        return dict
    
    def save(self):
        with open(calendar_filename,"w") as my_file:
            my_file.writelines(self.c)
            
        if self.c.events == set():
            try:
                os.remove(calendar_datafile)
            except:
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
            
    def list_events(self, period:str=None)->bool:
        ''' Lista los eventos por venir
            si period se deja vacio serán los de esta semana
            - "all" - todos los eventos
            - "this week" - los de esta semana
            - "this month" - los de este mes
        '''
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
                
                