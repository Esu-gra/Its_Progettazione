from abc import *
from datetime import datetime

import re

class URL:
    def __init__(self, indirizzo: str):
        if not self._valida_url(indirizzo):
            raise ValueError(f"URL non valido: {indirizzo}")
        self.indirizzo = indirizzo

    def _valida_url(self, url: str) -> bool:
        # Controllo basilare con espressione regolare
        pattern = r'^https?://[\w\-\.]+\.\w+.*$'
        return re.match(pattern, url) is not None

    def __str__(self):
        return self.indirizzo

class Utente(ABC):
    _username:str #immutabile
    _registrazione:datetime

    def __init__(self,username:str,registrazione:datetime):
        self.username=username
        self.registrazione=registrazione
    
    @abstractmethod
    def username(self):
        return self._username
    
    @abstractmethod 
    def registrazione(self):
        return self._registrazione
    

    ## le operazioni di classe 
    @abstractmethod
    def popolarita(self,i:datetime):
        pass
    @abstractmethod
    def affidabilita(self):
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



###classe UtentePrivato

class UtentePrivato(Utente):
    def __init__(self, username, registrazione):
        super().__init__(username, registrazione)

        