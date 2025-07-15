from datetime import datetime
from typing import TYPE_CHECKING
from UtentePrivato import UtentePrivato
from Asta import Asta




#responsabilità doppia , gestione asimmetrica da Bid 
class Bid:
    _istante:datetime #immutabile
    _asta:Asta 
    _utente:UtentePrivato
    _registro_bid=set()

    def __init__(self,istante:datetime,asta:Asta,utente:UtentePrivato):
        self.istante(istante)
        
        self.asta(asta)
        self.utente(utente)  #da aggiungere il vincolo che un 
                              #utente privato non puo fare bid su aste pubblicate da lui 
    
        self._utente.aggiungi_bid(self)
        self._asta.aggiungi_bid(self)


        
    
    def istante(self)->datetime:
        return self._istante
    
    def asta(self)->Asta:
        return self._asta
    
    def utente(self)->UtentePrivato:
        return self._utente
    
    def set_asta(self,a:Asta):
        if not a: raise ValueError("l'asta non deve essere None")
        self._asta=a
    
    def set_utente(self,u:UtentePrivato):
        if not u: raise ValueError("l' utente non deve essere None")
        self._utente=u
    





