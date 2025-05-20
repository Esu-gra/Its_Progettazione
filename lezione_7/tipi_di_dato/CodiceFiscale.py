'''
Considerare lo schema concettuale di alcune esercitazioni 
già svolte e ristrutturare il diagramma delle classi progettando 
una corrispondenza dei tipi di dato 
concettuali in Python.
Realizzare in Python opportune class 
che implementano alcuni di questi tipi di dato, 
e testarle per bene assicurandosi che si comportino 
come previsto (ovvero, oggetti distinti che rappresentano 
lo stesso valore siano riconosciuti come uguali anche in 
collezioni come "set").

Consegnare il diagramma UML delle classi ristrutturato
ed un link ad un proprio repository GIT pubblico dove è 
stato salvato il codice.
'''

#Tipi di dato non standard CF
import re
class CF:
    def __init__(self,cf:str):
        if not re.fullmatch(r'[A-Z0-9]{16}',cf.upper()):
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

c=CF("LPADFK36T26D932S")
print(c.get_cf())
print(hash(c))
c1=CF("LPADFK36T26D932S")
print(hash(c1))