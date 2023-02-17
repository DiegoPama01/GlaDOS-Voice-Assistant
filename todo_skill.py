from datetime import date
from enum import Enum
from uuid import uuid4

class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2   

class Item():
    __creation_date = date.today()
    __title = "empty"
    __status=Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False
    __url = ""
    __due_date = date
    __state=False
    __notes=""
    __icon=""
    
    def __init__(self,title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4())
        
    @property
    def icon(self):
        return self.__icon
    
    @icon.setter
    def icon(self,icon):
        self.__icon = icon
    
    @property
    def due_date(self):
        return self.__due_date
    
    @due_date.setter
    def due_date(self, due_date):
        self.__due_date = due_date   
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state
        
    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url
         
    @property
    def flag(self):
        return self.__flag
    
    @flag.setter
    def flag(self, flag):
        self.__flag = flag
        
    @property
    def title(self)->str:
        return self.__title
    
    @title.setter
    def title(self, url):
        self.__title = url
        
    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, priority):
        self.__priority = priority
        
    @property
    def creation_date(self):
        return self.__creation_date
    
    @creation_date.setter
    def creation_date(self,creation_date):
        self.__creation_date = creation_date
        
    @property
    def age(self):
        return self.creation_date - date.today()
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,status):
        self.__status = status
        
    @property
    def notes(self:str):
        return self.__notes
    
    @notes.setter
    def notes(self,notes):
        self.__notes = notes
        
    
class Todo():
    __todos = []
    
    def __init__(self):
        print("New todo list created")
        self._current = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < len(self.__todos) -1:
            self._current += 1
            print(self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current = -1
        raise StopIteration
    
    def __len__(self):
        return len(self.__todos)
            
            
    def new_item(self,item:Item):
        self.__todos.append(item)
        
    @property
    def items(self)->list:
        return self.__todos
    
    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title,item.status,item.priority,item.age)
    
    def remove_item(self,uuid:str=None,title:str=None)->bool:
        if title is None and uuid is None:
            print("You need to provide some detail for me to remove an item from the list")
            
        if uuid is None and title:
            for item in self.__todos:
                if title == item.title:
                    self.__todos.remove(item)
                    return True
                print("Item with title", title, "not found")
                return False
        if uuid:
            self.__todos.remove(uuid)
            return True
        
