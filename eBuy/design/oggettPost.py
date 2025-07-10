from abc import *
from datetime import *
from custom_types import *


class OggettoDelPost(ABC):
    _descrizione:str
    _anni_garanzia:IntGEZ
    _pubblicazione:datetime #immutabile#
    _prezzo:FloatGEZ

    
    @abstractmethod
    def __init__(self,descrizione:str,anni_garanzia:IntGEZ,pubblicazione:datetime,prezzo:FloatGEZ):
        super().__init__()
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione=pubblicazione
        self.set_prezzo(prezzo)
       

        #   get e set 
    @property
    def descrizione(self)->str:
        return self._descrizione
    

    @descrizione.setter
    def set_descrizione(self,v:str):
        self._descrizione=v
    

    @property
    def anni_garanzia(self)->IntGEZ:
        return self._anni_garanzia
    

    @anni_garanzia.setter
    def set_anni_garanzia(self,v:IntGEZ):
        self._anni_garanzia=v


    @property
    def pubblicazione(self)->datetime:
        return self.pubblicazione
    @property
    def prezzo(self):
        return self._prezzo
    
    @prezzo.setter
    def set_prezzo(self,v:FloatGEZ):
        self._prezzo=v





    



