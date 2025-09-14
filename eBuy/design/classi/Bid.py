from __future__ import annotations
from typing import TYPE_CHECKING, Any, Self, Tuple
from classi.bid_ut import bid_ut
from classi.asta_bid import asta_bid
from classi.OggettoDelPost import Asta
from classi.Utente import UtentePrivato

import datetime


if TYPE_CHECKING:
    from Index import Index



class Bid:
    _istante:datetime               #<<imm>>
    _asta_bid_link:asta_bid._link   #<<imm>>, certamente noto alla nascita 
    _bid_ut:bid_ut._link            #<<imm>>, certamente noto alla nascita 
    _index:Index[Tuple[datetime.datetime,int],Self]=Index[Tuple[datetime.datetime,int],Self]('Bid')

    def __init__(self,*,asta: Asta, utente_priv: UtentePrivato)->None:
        self._istante=datetime.now()
        self._add_link_asta_bid(asta)
        self._add_link_bid_ut(utente_priv)
        self._set_id(self._istante,asta.id()) #da controllare 
    
    @classmethod
    def all(cls):
        return cls._index.all()
    
    @classmethod
    def get(self,Key:Any)->Self|None:
        return self._index.get(Key)
    

    def _set_id(self,i:datetime,asta:int)->None:
        self._index.add((i,asta),self)
        self._id=(i,asta)


    def istante(self)->datetime:
        return self._istante
    
    def bid_ut(self)->bid_ut._link:
        return self._bid_ut_link
    
    def _add_link_asta_bid(self,asta:Asta)->None:
        l=asta_bid._link(asta,self)
        self._asta_bid_link=l
        asta._add_asta_bid(l)
    
    def _add_link_bid_ut(self,up:UtentePrivato)->None:
        l=bid_ut._link(self,up)
        self._bid_ut_link=l
        self._add_link_bid_ut(l)
    
    def __repr__(self)->str:
        return f"Bid(istante={self.istante()},\n\
                 utente_privato={self._bid_ut_link._utente_priv()},\n\
                 asta={self._asta_bid_link._asta})"
        
