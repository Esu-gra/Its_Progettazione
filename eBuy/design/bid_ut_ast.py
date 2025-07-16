
from datetime import datetime,timedelta

from abc import ABC, abstractmethod
from custom_types import FloatGEZ






class Asta:
    _scadenza:datetime
    _prezzo_rialzo:FloatGEZ



    def __init__(self, scadenza: datetime, prezzo_rialzo: FloatGEZ):
        
        self._scadenza = scadenza
        self._prezzo_rialzo = prezzo_rialzo

        #asta_bid
        self._bid_asta: set['Bid'] = set()
        
    def aggiungi_bid(self, b: 'Bid'):
        self._bid_asta.add(b)


     #get
    def get_scadenza(self)->datetime:
        return self._scadenza

    def get_prezzo_rialzo(self)->FloatGEZ:
        return self._prezzo_rialzo

    def bid_asta(self)->frozenset['Bid']:
        return frozenset(self._bid_asta)
    

     #set
    def scadenza(self,d:datetime):
        if not d:
            raise ValueError("la data non puo essere None")
        self._scadenza=d
    
    def prezzo_rialzo(self,p:FloatGEZ):
        if not p:
            raise ValueError("il prezzo non puo essere None")
        self._prezzo_rialzo=p


    
    def __str__(self)->str:
        return f"Asta con scadenza il {self._scadenza}, prezzo rialzo: €{self._prezzo_rialzo:.2f}, numero di bid: {len(self._bid_asta)}"
    
     # cosi ritorno il set di bid  e non il suo indirizzo
   
    
   
    







class Utente(ABC):
    _username:str #<<imm>>
    _registrazione:datetime


    @abstractmethod
    def __init__(self, username: str, registrazione: datetime):
        self._username = username #<<imm>>
        self.set_registrazione(registrazione)

    def get_username(self)->str:
        return self._username

    def set_registrazione(self, d: datetime):
        if not d:
          raise ValueError("La data non può essere None")
        self._registrazione = d
       

    def get_registrazione(self)->datetime:
        return self._registrazione


    @classmethod
    def affidabilita(self):
        pass




class UtentePrivato(Utente):
    bid_ut:set

    def __init__(self, username:str, registrazione:datetime):
        super().__init__(username, registrazione)
        self._bid_ut: set['Bid'] = set()

    def aggiungi_bid(self, b: 'Bid'):
        self._bid_ut.add(b)
    

    #ritorno il set di bid 
    def bids(self)->frozenset['Bid']:
        return 

    def __str__(self)->str:
        return f"{self.get_username()} (registrato il {self.get_registrazione()})"

     

    

class Bid:
    _asta:Asta
    _istante:datetime #<<imm>>
    _utente:UtentePrivato

    def __init__(self, istante: datetime, asta: Asta, utente: UtentePrivato):


        self._istante = istante
        self._asta=asta
        self._utente=utente

        self._utente.aggiungi_bid(self)
        self._asta.aggiungi_bid(self)


        if not asta:
         raise ValueError("Asta non valida")
        if not utente:
          raise ValueError("Utente non valido")
        if istante > asta.get_scadenza():
          raise ValueError("Non è possibile fare un'offerta dopo la scadenza dell'asta.")
        if istante < utente.get_registrazione():
          raise ValueError("Un utente non può fare offerte prima della propria registrazione.")

    def get_istante(self)->datetime:
        return self._istante

    def get_asta(self)->Asta:
        return self._asta

    def get_utente(self)->UtentePrivato:
        return self._utente
    
    def __eq__(self, other):
         return isinstance(other, Bid) and self._istante == other._istante and self._utente == other._utente and self._asta == other._asta
 
    def __hash__(self):
        return hash((self._istante, self._utente, self._asta))

    def __str__(self)->str:
        return f"Bid di {self._utente.get_username()} su asta con rialzo €{self._asta.get_prezzo_rialzo():.2f} il {self._istante}"
    


d=datetime.now()

registrazione = datetime(2024, 8, 1,23, 55, 59, 342380)
u = UtentePrivato("Esu", registrazione)
a = Asta(datetime(2024, 8, 31), FloatGEZ(100))
b = Bid(datetime(2024, 8, 21), a, u)




print(f"Utente: {u.get_username()}")
print(f"Registrazione: {u.get_registrazione()}")
print(f"Bid effettuato il: {b.get_istante()}")
print(f"Prezzo rialzo asta: €{b.get_asta().get_prezzo_rialzo():.2f}")
print(f"Bid: {b}")
print(f"Asta: {b.get_asta()}")


