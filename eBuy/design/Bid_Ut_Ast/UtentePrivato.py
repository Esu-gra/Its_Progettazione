from Utente import Utente
from Bid import Bid

class UtentePrivato(Utente):
    
    def __init__(self, username, registrazione):
        super().__init__(username, registrazione)
        self._bid_ut:set[Bid]=[]

    def aggiungi_bid(self,b:Bid):
        self._bid_ut.add(b)

    def bids(self)->frozenset:
        return frozenset(self._bid_ut)



