from abc import *
from datetime import datetime
from custom_types import *





class Utente(ABC):
    _username:str #immutabile
    _registrazione:datetime

    def __init__(self,username:str,registrazione:datetime):
        self._username=username
        self._registrazione=registrazione
    
    @property
    def username(self):
        return self._username
    
    @property
    def registrazione(self):
        return self._registrazione
    

    ## le operazioni di classe ,
    @classmethod
    def popolarita(i:datetime):
        pass
    @classmethod
    def affidabilita(i:datetime)->float|None:
        pass



      

class VenditoreProfessionale(Utente):
    _vetrina:URL #inverita è di tipo URL ,che dovrebbe essere creata
    def __init__(self, username:str, registrazione:datetime,vetrina:URL):
        super().__init__(username, registrazione)
        self.set_vetrina(vetrina)

    
    
    def set_vetrina(self,v:URL):
        self._vetrina=v
    
    def get_vetrina(self)->URL :
        return self._vetrina
    


###controllo ####
vetrina=URL(URL("https://www.mioshop.it/vetrina123"))
v=VenditoreProfessionale("esu-gra",12-10-2003,vetrina)





