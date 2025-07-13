from abc import *
from datetime import datetime
from custom_types import *





class Utente(ABC):
    _username:str #immutabile
    _registrazione:datetime

    @abstractmethod
    def __init__(self,username:str,registrazione:datetime):
        self._username=username
        self.set_registrazione(registrazione)
    
    
    def username(self)->str:
        return self._username
    
    def set_registrazione(self,d:datetime)->datetime|None:
        if not d: raise ValueError("la data non puo essere None")
        self._registrazione=d

    def registrazione(self)->datetime:
        return self._registrazione
    



    ## le operazioni di classe ,
    @classmethod
    def popolarita(i:datetime):
        pass
    @classmethod
    def affidabilita(i:datetime)->float|None:
        pass



      



###controllo ####






