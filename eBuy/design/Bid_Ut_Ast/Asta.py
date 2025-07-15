from datetime import datetime
from UtentePrivato import UtentePrivato
from eBuy.design.custom_types import *
from Bid import Bid 

class Asta :
    _scadenza:datetime
    _prezzo_rialzo:FloatGEZ
    _bid_asta:set['Bid'] = set()
    

    def __init__(self,scadenza:datetime,prezzo_rialzo:FloatGEZ):
        self.set_scadenza(scadenza)
        self.set_prezzo_rialzo(prezzo_rialzo)
        


    def scadenza(self):
        return self._scadenza
    
    def set_scadenza(self,v:datetime):
        self._scadenza=v

    
    def prezzo_rialzo(self)->FloatGEZ:
        return self._prezzo_rialzo
    
   
    def set_prezzo_rialzo(self,v:FloatGEZ):
        self._prezzo_rialzo=v
    

    def aggiungi_bid(self,b:Bid):
        self._bid_asta.add(b)
    
    def bids(self)->frozenset:
        return frozenset(self._bid_asta)

    

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


