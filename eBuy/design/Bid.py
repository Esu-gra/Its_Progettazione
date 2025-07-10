from datetime import datetime
from Asta import Asta
from UtentePrivato import UtentePrivato


class Bid:
    _istante:datetime #immutabile
    _asta:Asta # come lo posso rappresentare? {id}
    _utente:UtentePrivato

    def __init__(self,istante:datetime):
        self._istante:datetime=istante
    
    def istnte(self)->datetime:
        return self._istante
    
    def asta(self)->Asta:
        return self._asta
    
    def utente(self)->UtentePrivato:
        return self._utente