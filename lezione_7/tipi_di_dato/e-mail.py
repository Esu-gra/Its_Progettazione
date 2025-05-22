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


#tipi di dato non standard Email
import re
class Email:
    def __init__(self,email:str):
         if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
              raise ValueError("Email npon valida. ")
         self._email=email

    def __eq__(self, value):
         raise isinstance(value,Email) and self._email==value._email
    
    def __hash__(self):
         return hash(self._email)
    def __str__(self):
         return self._email
        

email=Email("kjned@ed.com")
print(hash(email))
print(email)
emai2=email=Email("kjned@ed.com")
print(hash(emai2))
print(emai2)