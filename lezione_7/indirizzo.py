'''
Considerare lo schema concettuale di alcune esercitazioni già svolte e ristrutturare il diagramma delle classi progettando una corrispondenza dei tipi di dato 
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
#ORIDINI E FATTURE

#tipi di dato non standard Indirizzo
class Indirizzo:
    def __init__(self, via: str, civico: str, cap: str):
        if not via or not civico:
            raise ValueError("Via e civico non possono essere vuoti.")
        if not (cap.isdigit() and len(cap) == 5):
            raise ValueError("CAP deve essere una stringa di 5 cifre numeriche.")

        self._via = via
        self._civico = civico
        self._cap = cap

    def via(self): return self._via
    def civico(self): return self._civico
    def cap(self): return self._cap

    def __eq__(self, other):
        return isinstance(other, Indirizzo) and \
               (self._via, self._civico, self._cap) == (other._via, other._civico, other._cap)

    def __hash__(self):
        return hash((self._via, self._civico, self._cap))

    def __str__(self):
        return f"{self._via}, {self._civico}, {self._cap}"

i1 = Indirizzo("Via Roma", "12", "00100")
i2 = Indirizzo("Via Roma", "12", "00100")
       
print(hash(i1))            
print(i1) 
print(hash(i2))  
print(i1)