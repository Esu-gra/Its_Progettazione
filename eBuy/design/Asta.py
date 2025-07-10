from datetime import datetime
import UtentePrivato
from custom_types import *
from Bid import Bid 

class Asta :
    _scadenza:datetime
    _prezzo_rialzo:FloatGEZ
    

    def __init__(self,scadenza:datetime,prezzo_rialzo:FloatGEZ):
        self.scadenza(scadenza)
        self.prezzo_rialzo(prezzo_rialzo)
        

    @property
    def scadenza(self):
        return self._scadenza
    
    @scadenza.setter
    def set_scadenza(self,v:datetime):
        self._scadenza=v

    @property
    def prezzo_rialzo(self)->FloatGEZ:
        return self._prezzo_rialzo
    
    @prezzo_rialzo.setter
    def set_prezzo_rialzo(self,v:FloatGEZ):
        self._prezzo_rialzo=v

    

    @classmethod
    def prezzo(i:datetime)->FloatGEZ:
        pass


    @classmethod
    def ultimo_bid(i:datetime)->Bid:
        pass
    
    @classmethod
    def vincitore()->UtentePrivato:
        pass

    @classmethod
    def conclusa()->bool:
        pass


