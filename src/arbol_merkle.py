from typing import List
from src.nodo_interface import NodoInterfaz
from src.models.nodo_hoja import NodoHoja
from src.models.nodo_interno import NodoInterno

""" Clase que representa un árbol de Merkle """

class ArbolMerkle:

    def __init__(self, datos: List[str]):
        if not datos:
            raise ValueError("La lista de datos no puede estar vacía.")
        self.datos = datos
        self.raiz: NodoInterfaz = self._construir_arbol(datos) 

    def _construir_arbol(self, datos: List[str]) -> NodoInterfaz:
        capa_actual: List[NodoInterfaz] = [NodoHoja(dato) for dato in datos]

        while len(capa_actual) > 1:
            if len(capa_actual) % 2 != 0:
                capa_actual.append(capa_actual[-1])

            nueva_capa: List[NodoInterfaz] = []

            for i in range(0, len(capa_actual), 2):
                hijo_izquierdo = capa_actual[i]
                hijo_derecho = capa_actual[i + 1]
                
                nodo_padre = NodoInterno(hijoIzquierdo=hijo_izquierdo, hijoDerecho=hijo_derecho)
                nueva_capa.append(nodo_padre)

            capa_actual = nueva_capa

        return capa_actual[0]

    def obtener_raiz(self) -> str:
        return self.raiz.calcular_hash