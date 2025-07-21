from abc import abstractmethod,ABC

from typing import TYPE_CHECKING
from custom_types import IntGEZ,FloatGEZ,Condizioni


if TYPE_CHECKING:
    from Bid import Bid 
    from asta_bid import asta_bid
    from Utente import UtentePrivato


import datetime
from datetime import timedelta

class OggettoDelPost(ABC):
    _descrizione:str
    _anni_garanzia:IntGEZ
    _pubblicazione:datetime #immutabile#
    _prezzo:FloatGEZ
    _is_nuovo:bool
    _condizioni:Condizioni  #Condizioni

    
    @abstractmethod
    def __init__(self,descrizione:str,anni_garanzia:IntGEZ,prezzo:FloatGEZ,is_nuovo:bool,condizioni:Condizioni)->None:
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione=datetime.datetime.now()
        self.set_prezzo(prezzo)
        self.set_is_nuovo(is_nuovo)
        self.set_condizioni(condizioni)
       

    

    #get and set 
    def descrizione(self)->str:
        return self._descrizione
    

    def set_descrizione(self,descrizione:str):
        self._descrizione=descrizione
    


    def anni_garanzia(self)->IntGEZ:
        return self._anni_garanzia
    

    def set_anni_garanzia(self,v:IntGEZ):
        self._anni_garanzia=v


    def pubblicazione(self)->datetime:
        return self._pubblicazione
   
    def prezzo(self):
        return self._prezzo

    def set_prezzo(self,v:FloatGEZ):
        self._prezzo=v

    def is_nuovo(self)->bool:
        return self._is_nuovo
    
    def set_is_nuovo(self,is_nuovo:bool)->None:
        self._is_nuovo=is_nuovo
    
    def condizioni(self)->Condizioni:
        return self._condizioni
    
    def set_condizioni(self,condizioni:Condizioni)->None:
        self._condizioni=condizioni

       #__repr__

    def __repr__(self):
        return f"OggettoDelPost(descrizione={self.descrizione()},\n\
                 anni_garanzia={self.anni_garanzia()},\n \
                 pubblicazione={self.pubblicazione()},\n\
                 prezzo={self.prezzo()},\n\
                 Nuovo={self.is_nuovo()},\n\
                 conndizioni={self.condizioni()})"

class Asta(OggettoDelPost):
    _scadenza:datetime=None
    _prezzo_rialzo:FloatGEZ=None
    _bids:dict['Bid','asta_bid.link']={}


     
   
        
        
        
    def __init__(self, descrizione:str,
                 anni_garanzia:IntGEZ, 
                 prezzo:FloatGEZ,
                 is_nuovo:bool, 
                 condizioni:Condizioni,
                _scadenza:datetime,
                 prezzo_rialzo:FloatGEZ)->None:
        super().__init__(descrizione, anni_garanzia, prezzo, is_nuovo, condizioni)
        self.set_anni_garanzia(anni_garanzia)
        self.set_descrizione(descrizione)
        self.set_prezzo(prezzo)
        self.set_scadenza(_scadenza)
        self.set_prezzo_rialzo(prezzo_rialzo)
        
    


    def set_scadenza(self,scadenza:datetime)->None:
        self._scadenza=scadenza

    def scadenza(self)->datetime:
        return self._scadenza
    
    def set_prezzo_rialzo(self,rialzo:FloatGEZ)->None:
        self._prezzo_rialzo=rialzo

    def prezzo_rialzo(self)->FloatGEZ:
        return self._prezzo_rialzo

    def add_bid(self,u:'UtentePrivato')->None:
        from Bid import Bid
        Bid(asta=self,up=u)

    
    def _add_asta_bid(self,l:'asta_bid')->None:
        if l.asta() is not self:
            raise KeyError("Link non riguarda me")
        
        if l.bid() in self._bids:
            raise KeyError("Link gia esistente")
    
        self._bids[l.bid()]=l
    

    #operazioni di classe 
    def __repr__(self):
        return f"Asta(OggettoDelPost={super().__repr__()},\n"\
        f"scdenza={self._scadenza},\n"\
        f"prezzo_rialzo={self._prezzo_rialzo},\n"\
        f"bids={self._bids})"
    






def test_asta_base():
    print("▶️ Inizio test Asta")

    descrizione = "Laptop Lenovo i7"
    anni_garanzia = IntGEZ(2)
    prezzo = FloatGEZ(999.99)
    is_nuovo = True
    condizioni = Condizioni.NUOVO  # Supponiamo sia un Enum

    scadenza = datetime.datetime.now() + timedelta(days=7)
    rialzo = FloatGEZ(20)

    asta = Asta(descrizione, anni_garanzia, prezzo, is_nuovo, condizioni, scadenza, rialzo)