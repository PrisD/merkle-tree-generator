from dataclasses import dataclass
import hashlib
from src.nodo_interface import NodoInterfaz

@dataclass
class NodoInterno(NodoInterfaz):
    hijoIzquierdo: NodoInterfaz
    hijoDerecho: NodoInterfaz

    @property
    def esHoja(self) -> bool:
        return False
    
    @property
    def calcularHash(self) -> str:
        hash_hijo_izquierdo = self.hijoIzquierdo.calcularHash()
        hash_hijo_derecho = self.hijoDerecho.calcularHash()
        concatenated_hashes = hash_hijo_izquierdo + hash_hijo_derecho
        return hashlib.sha256(concatenated_hashes.encode('utf-8')).hexdigest()