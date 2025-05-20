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


#tipi di dato non standard PartitaIva

class PartitaIva:
    def __init__(self,p_iva:str):
        if not (p_iva.isdigit() and len(p_iva)==11):
            raise ValueError("Partita IVA non valida , deve contenere 11 cifre ")
        self._p_iva=p_iva

    def __str__(self):
        return self._p_iva
    def __eq__(self, value):
        return isinstance(value,PartitaIva) and self._p_iva==value._p_iva
    def __hash__(self):
        return hash(self._p_iva)

piva = PartitaIva("12345678931")
print(piva.__str__())
piva1 = PartitaIva("12345678931")

print(hash(piva))

print(hash(piva1))