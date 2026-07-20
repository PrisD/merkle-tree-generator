from abc import ABC, abstractmethod

""" Interfaz para los nodos del árbol de Merkle """

class NodoInterface(ABC):
    @property
    @abstractmethod
    def esHoja(self) -> bool:
        pass

    @property    
    @abstractmethod
    def calcularHash(self) -> str:
        pass