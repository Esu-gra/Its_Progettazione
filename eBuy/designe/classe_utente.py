from abc import ABC
from datetime import *


class Utente(ABC):
    _username:str #immutabile
    _registrazione:datetime  #immutabile

    @
    def __init__(self,username:str,registrazione:datetime):
        self.username=username
        self._registrazione=registrazione

        super().__init__()
        