from __future__ import annotations

from eBuy.design.custom_types import *
from datetime import date

class PosizioneMilitare:
    _nome: str # id immutabile

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

class Persona:
    _nome:str 
    _cognome:str
    _codiceFiscale:CF
    _nascita:date #immutabile

    _is_uomo=bool
    _is_donna=bool
    _maternita=IntGEZ|None
    _posizione_militare= PosizioneMilitare  |None


    def __init__(self, *, nome: str, cognome: str, cf: CF, nascita: date,
                 maternita: IntGEZ|None = None,
                 posizione_militare: PosizioneMilitare | None=None):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self.nascita=nascita
        self.set_attributi_donna(maternita)
        self.set_attributi_uomo(posizione_militare)

        if maternita is not None:
             self.set_attributi_donna(maternita)

        else:
             self.remove_attributi_donna()
        
        if posizione_militare is not None:
             self.set_attributi_uomo(posizione_militare)
        else:
             self.remove_attributi_uomo()

        if not(self.is_uomo() or self.is_donna()):
            raise ValueError("Ogni persona deve essere uomo o donna")



 

    


    def set_nome(self,nome:str)->None:
        self._nome=nome

    def set_cognome(self,cognome:str):
        self._cognome=cognome

    
    def set_cf(self,cf:CF)->None:
        self._codiceFiscale=cf
    


    def is_uomo(self)->bool:
        return self._is_uomo
    
    def is_donna(self)->bool:
        return self._is_donna
    
    def set_attributi_uomo(self,posizione:PosizioneMilitare)->None:
        self._is_uomo=True
        self._posizione_militare=posizione

    def remove_attributi_uomo(self)->None:
        try:
            if not self.is_uomo():
                raise ValueError("La persona non è un uomo")
            
        except AttributeError:
            pass

        self._is_uomo==False
        self._posizione_militare==None

    
    def set_attributi_donna(self,maternita:IntGEZ)->None:
        self._is_donna=True
        self._maternita=maternita
    
    def remove_attributi_donna(self)->None:
        try:
            if not self.is_donna():
                raise ValueError("La persona non è una donna ")
        except AttributeError:
            pass
    
    


        
        
    

        




















