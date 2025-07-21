from __future__ import annotations
from typing import TYPE_CHECKING
from abc import *

#popolarita importo Popolarita
#affidabilita importo FloatGZ

import datetime


if TYPE_CHECKING:
    from classi.Bid import Bid 
    from classi.bid_ut import bid_ut


class Utente(ABC):
    _username:str #<<imm>>
    _registrazione:datetime #<<imm>>


    @abstractmethod
    def __init__(self,username:str)->None:
        self.set_username(username) 
        self._registrazione=datetime.datetime.now()

    def username(self)->str:
        return self._username

    def set_username(self,un:str)->None:
        self._username=un

    def __repr__(self):
        return f"Utente(username={self.username()},registrazione={self._registrazione})"  
       


    def affidabilita(self):
        pass


    def popolarita(self):
        pass



class UtentePrivato(Utente):
    _bid_ut_link:dict['Bid','bid_ut._link']={}

    def __init__(self, username:str)-> None:
        super().__init__(username)
        
    
    def _add_bid_ut_link(self,l:'bid_ut')->None:
        if l.utente_priv() is not self:
            raise ValueError("Link non riguarda me ")
        
        if l.bid() in self._bid_ut_link:
            raise KeyError("Gia esiste il link")
        
        self._bid_ut_link[l.bid()]=l


    def __repr__(self):
        return f"UtentePrivato{super().__repr__()}"