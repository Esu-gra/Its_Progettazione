from typing import Any
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classi.Bid import Bid
    from classi.Utente import UtentePrivato


class bid_ut:

    class _link:
        _bid:'Bid'
        _utente_priv:UtentePrivato

    def __init__(self,bid:'Bid',up:UtentePrivato)->None:
        self._bid:'Bid'=bid
        self._utente_priv:UtentePrivato=up
    
    def bid(self)->'Bid':
        return self._bid
    
    def utente_priv(self)->UtentePrivato:
        return self._utente_priv
    def __hash__(self):
        return hash((self.bid(),self.utente()))
    
    def __eq__(self, other:Any):
        if type(self)!=type(other) or hash(self)!=hash(other):
            return False
        return (self.bid(),self.utente_priv())==(other.bid(),other.utente_priv())
        
    def __repr__(self):
        return f"bid_ut(bid={self.bid()},utente_priv={self.utente_priv()})"