
from __future__ import annotations

from datetime import date
from custom_types import *

from typing import *


class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # immutabile, noto alla nascita
    _stipendio: Importo # noto alla nascita
    _afferenza: _afferenza | None # da assoc. 'afferenza' [1..1], possibilmente non noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:Importo,
                 dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self.set_link_afferenza(dipartimento_aff, data_afferenza)

    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        if (dipartimento_aff is None) != (data_afferenza is None):
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")


        # Se afferiva a un dipartimento, devo rimuoverlo da esso
        try:
            if self.get_link_afferenza():
                self.get_link_afferenza().dipartimento()._remove_impiegato(self.get_link_afferenza())
        except AttributeError:  # il campo _afferenza non era mai stato settato: questo metodo è stato quindi chiamato dal costruttore
            pass

        if dipartimento_aff: # sono entrambi not None
            self._afferenza = _afferenza(impiegato=self, dipartimento=dipartimento_aff, data_afferenza=data_afferenza)
            dipartimento_aff._add_impiegato(self._afferenza)
        else: # sono entrambi None
            self._afferenza = None

    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def set_cognome(self, cognome:str) -> None:
        self._cognome = cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> Importo:
        return self._stipendio

    def set_stipendio(self, stipendio:Importo) -> None:
        self._stipendio = stipendio



class Progetto:
    _nome: str # noto alla nascita
    _budget: Importo
    _impiegati_prog:dict[Impiegato,ImpiegatoProggetto._link]

    def __init__(self, nome:str, budget:Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)

    def set_nome(self, nome:str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

    def set_budget(self, budget:Importo) -> None:
        self._budget = budget

    def budget(self) -> Importo:
        return self._budget
    
    def coinvolti(self)->frozenset:
        return frozenset(self._impiegati_prog.values())
    


    def is_coinvolto(self,impiegato):
        for coinvolto in self._impiegati_prog:
            if coinvolto.nome()==impiegato:
                return True
            return False
        
        # secondo metodo 
    def is_coinvolto_brutto(self,impiegato)->bool:
        i:ImpiegatoProggetto=ImpiegatoProggetto(self,impiegato,date.today())
        return i in self._impiegati_prog
    
    def __contains__(self,item:Any):
        if not isinstance(item,Impiegato):
            return False
        return self.is_coinvolto(item)
    

    def add_ompiegato(self,impiegato:Impiegato):
        if impiegato in self._impiegati_prog:
            raise KeyError ("Il progetto coinvolge gia l'impiegato")
        i:Impiegato=Impiegato(self,impiegato,date)
        self._impiegati_prog[impiegato]=i

    def remuve_impiegato(self,impiegato:Impiegato):
        try:
            del self._impiegati_prog[impiegato]
        except KeyError:
            raise KeyError("il progetto non coinvolge l'impiegato")
    
    def data_coinvolgimento(self,impiegato:Impiegato):
        try:
            return self._impiegati_prog[impiegato]
        except KeyError:
            raise KeyError("il progetto non coinvolge l'impiegato")
        
    def ultimo_impiegato(self)->Impiegato:
        if not self.coinvolti():
            raise RuntimeError(f"il progetto {self.nome()} non ha impiegati coinvolti")
        data_coinvolg=set[date]=set()

        for i in self._impiegati_prog.values():
            data_coinvolg.add(i.data())
            ultima_data:date=max(data_coinvolg)
            for imp in self._impiegati_prog:
                if self.data_coinvolgimento(imp)==ultima_data:
                    return imp

    

    
class ImpiegatoProggetto:
      class _link:
          _impiegato:Impiegato
          _progetto:Progetto
          _data:date

      def __init__(self,i:Impiegato,p:Progetto,d:date):
          self._impiegato:Impiegato=i
          self._progetto:Progetto=p
          self._data:date=d
      
      def impiegato(self):
          return self._impiegato
      def progetto(self):
          return self._progetto
      def data(self):
          return self._progetto
      

      def __hash__(self)->int:
          return hash(self.impiegato(),self.progetto())
      def __eq__(self, other):
          if type(self)!=type(other) or hash(self)!=hash(other):
              return False
          return (self.impiegato(),self.progetto())==(other.impiegato(),other.progetto())