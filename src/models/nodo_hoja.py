from dataclasses import dataclass
import hashlib
from src.nodo_interface import NodoInterfaz

@dataclass
class NodoHoja(NodoInterfaz):
    dato: str

    @property
    def es_hoja(self) -> bool:
        return True
    
    @property
    def calcular_hash(self) -> str:
        return hashlib.sha256(self.dato.encode('utf-8')).hexdigest()
    
    def mostrar_grafico(self, prefijo: str = "", es_ultimo: bool = True) -> str:
        conector = "└── " if es_ultimo else "├── "
        hash_corto = self.calcular_hash[:8] if callable(self.calcular_hash) else self.calcular_hash[:8]
        return f"{prefijo}{conector}🍃 [HOJA] Datos: '{self.dato}' | Hash: {hash_corto}...\n"