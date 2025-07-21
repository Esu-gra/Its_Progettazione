from typing import Self
import re
from datetime import date


class Importo(float):
	def __new__(cls, v:int|float|str)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be >= 0")
		return float.__new__(cls, v)

class Telefono(str):
	def __new__(cls, v:str)->Self:
		if not re.fullmatch(r'\+?[0-9]+', v):
			raise ValueError(f"Value v == {v} does not satisfy the standard")
		return str.__new__(cls, v)
	




class CF:
    def __init__(self,cf:str):
        if not re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-EHLMPR-T][0-9]{2}[A-Z][0-9]{3}[A-Z]$",cf.upper()):
            raise ValueError("Codice fiscale non valido , deve essere lungo 16 carartteri alfanumerici.")
        
        self._cf=cf.upper()
    
    def get_cf(self):
        return self._cf
    
    def __eq__(self, value):
        return isinstance(value,CF) and self._cf==value._cf
    
    def __hash__(self):
        return hash(self._cf)
    
    def __str__(self):
        return self._cf





class IntGZ(int):
    def __new__(cls,v):
        valore:int=super().__new__(cls,v)
        if valore<=0:
            raise ValueError(f"Il valore deve essere maggiore di zero , valore dato: {v}")
        else:
            return valore


class IntGEZ(int):
    def __new__(cls,v):
        valore:int=super().__new__(cls,v)
        if valore<0:
            raise ValueError(f"Il valore deve essere maggiore di zero ")
        else:
            return valore
        
    def  __sottrazione__(self,other:int|str|float|bool):
        other_int:int=int(other)
        try:
            result:int=int(self)-other_int
            return IntGZ(result)
        except ValueError:
            raise ValueError(f"Risultato della differenza non valido è minore di zero")
        

class DataGE1895(date):
    def __new__(cls,year,month,day):
        if year < 1895:
            raise ValueError("Anno non valido deve essere maggioreo uguale a  1895")
        return super().__new__(cls,year,month,day)
    




class URL(str):
   def __new__(cls,v:str|Self)->Self:
        if not re.search("(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?",v):
             raise ValueError(f"{v} non è un URL valido.")
        return  int.__new__(cls,v)



class FloatGEZ(float):
    def __new__(cls,v:int|float|Self)->Self:
         if v<0:
              raise ValueError(f"Il valore di {v} deve essere >=0.")
         return float.__new__(cls,v)

class FloatGZ(float):
    def __new__(cls,v:int|float|Self)->Self:
         if v<=0:
              raise ValueError(f"Il valore di {v} deve essere > 0.")
         return float.__new__(cls,v)
    
