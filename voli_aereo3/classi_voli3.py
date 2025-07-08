from tipiDato import IntGZ
from tipiDato import DataGE1895
from datetime import timedelta
from citta_nazione import *


class Volo :
    def __init__(self,codice:str,durata_min):
        self.__codice= codice #immutabile
        self.set_durata(durata_min)

    def get_codice(self)->str:
        return self.__codice
    
    def get_durata(self) -> timedelta:
       return timedelta(minutes=self._durata_min)

    def set_durata(self,v:IntGZ):
       try:
           self._durata_min=IntGZ(v)
       except ValueError:
           raise ValueError(f"Valore non valido per la durata")


#copmagnia

class CompagniaAerea:
    def __init__(self,nome:str,anno_fondazione:DataGE1895):
        self.__nome=nome
        self.__anno=DataGE1895(anno_fondazione)
    
    def get_nome(self)->str:
        return self.__nome
    
    def get_anno_fondazione(self):
        return self.__anno
    
    def set_nome(self,valore:str):
         self.__nome=valore


#Aeroporto.

class Aeroporto:
    def __init__(self,codice:str,nome:str):
        self.__codice=codice #immutabile
        self._nome=nome

    def get_nome(self)->str:
        return self._nome
    

    def get_codice(self)->str:
        return self.__codice
    
    def set_nome(self,valore:str):
        self._nome=valore

#citta


class Citta:
    def __init__(self,nome,num_abitanti:IntGZ):
        self._nome=nome
        self._abitanti=num_abitanti
    
    def get_nome(self)->str:
        return self._nome

    def get_abitanti(self)->IntGZ:
        return self._abitanti
    
    def set_abbitanti(self,valore:IntGZ):
        self._abitanti=IntGZ(valore)

    def set_nome(self,valore:str):
        self._nome=valore


# class Nazione:
#     _name:str
#     citta:CittaNazione._Link
    

#     def get_nome(self):
#         return self._name
    
#     def set_nome(self,v:str):
#         self._name=v
        
#     def __init__(self,nome:str):
#         self.get_nome()

    





durata =90
v = Volo("AZ001", durata)

print("Codice volo:", v.get_codice())         
print("Durata (min):", v.get_durata())        
print("Tipo:", type(v.get_durata()))           
