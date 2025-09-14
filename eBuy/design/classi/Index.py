from typing import *
from weakref import WeakKeyDictionary


KeyType=TypeVar('KeyType')
ValueType=TypeVar('ValueType')


class Index(Generic[KeyType,ValueType]):
    _name:str
    _objects:WeakKeyDictionary[KeyType,ValueType]


    def __init__(self,name:str):
        self._name:str=name
        self._objects:WeakKeyDictionary[KeyType,ValueType]=WeakKeyDictionary()

    def name(self)->str:
        return self._name

    def __str__(self)->str:
        return f"Index {self.name()}:\n - lenght: {len(self._objects)}\n - keys = {[k for k in self._objects.keys()]}"
    
    def add(self,_id:KeyType,obj:ValueType)->None:
        if _id in self._objects:
            raise KeyError(f"Doppia chiave {_id} per la classe {type(obj)}")
        self._objects[_id]=obj

    def remove(self,_id:KeyType)->None:
        if _id is not None:
            del self._objects[_id]
    
    def get(self,_id:KeyType)->ValueType|None:
        return self._objects.get(_id,None)


    def all(self)->Generator[ValueType,None ,None]:
        return self._objects.values()
    

    def all_keys(self)->Generator[KeyType,None,None]:
        return self._objects.keys()
    
    def __len__(self)->int:
        return len(self._objects)







#classe di prova 

class Studente:
    def __init__(self, nome):
        self.nome = nome


index_student=Index[str,Studente]("studenti")


s1=Studente("Anna")
s2=Studente("Mario")

index_student.add(s1,"A1")


print(index_student.name())