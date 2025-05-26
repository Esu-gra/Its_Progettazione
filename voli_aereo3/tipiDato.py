#Implementazione dei tipi di dati specializzati
from datetime import date



class IntGZ(int):
    def __new__(cls,v):
        valore:int=super().__new__(cls,v)
        if valore<=0:
            raise ValueError(f"Il valore deve essere maggiore di zero , valore dato: {v}")
        else:
            return valore
        
    def  __sottrazione__(self,other:int|str|float|bool):
        other_int:int=int(other)
        try:
            result:int=int(self)-other_int
            return IntGZ(result)
        except ValueError:
            raise ValueError(f"Risultato della differenza non valido è minore o uguale a zero")
        

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



