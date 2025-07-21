
from __future__ import annotations
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classi.Bid import Bid
    from classi.OggettoDelPost import Asta

class asta_bid:

    
    class _link:
        _bid:'Bid'
        _asta:'Asta'
    
    def __init__(self,bid:'Bid',asta:Asta):
        self._bid:'Bid'=bid
        self._asta:Asta=asta


    def bid(self)->'Bid':
        return self._bid
    

    def asta(self)->Asta:
        return self._asta
    


    def __hash__(self)->int:
        return hash((self.bid(),self.asta()))
    def __eq__(self, value:Any):
        if type(self)!=type(value) or hash(self)!=hash(value):
            return False
        return (self.bid(),self.asta()==(value.bid(),value.asta()))
        
    def __repr__(self):
        return f"bid_ut(bid={self.bid()},asta={self.asta()})"