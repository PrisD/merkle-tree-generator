from abc import ABC, abstractmethod

""" Interfaz para los nodos del árbol de Merkle """

class NodoInterfaz(ABC):
    @property
    @abstractmethod
    def es_hoja(self) -> bool:
        pass

    @property    
    @abstractmethod
    def calcular_hash(self) -> str:
        pass