from dataclasses import dataclass
import hashlib
from src.nodo_interface import NodoInterfaz

@dataclass
class NodoHoja(NodoInterfaz):
    dato: str

    @property
    def esHoja(self) -> bool:
        return True
    
    @property
    def calcularHash(self) -> str:
        return hashlib.sha256(self.dato.encode('utf-8')).hexdigest()