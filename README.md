# merkle-tree-generator

## Proyecto Final: Árboles de Merkle

**Materia:** Lenguajes, computabilidad y Aplicaciones Modernas

**Institución:** Universidad Tecnológica Nacional - Facultad Regional Delta

**Proyecto selecconado:** N°27 Árboles de Merkle y Blockchain

**Lenguaje:** Python 3.12.1 - Enfoque POO

**Alumna:** Priscila Belén Della Vecchia

---

## Descripción

Este proyecto implementa una simulación de una **Blockchain simplificada** cuyo mecanismo de integridad de datos se basa en la construcción de **Árboles de Merkle**.El desarrollo adopta un enfoque puramente **Orientado a Objetos (POO)**, aplicando patrones de diseño para estructurar jerárquicamente las transacciones, la raíz criptográfica de los árboles y la cadena inmutable de bloques.

---

## Objetivos

1.  **Construcción y verificación de árboles de Merkle** - Generación del árbol desde las hojas hasta la raíz
2.  **Simulación de Blockhain** - Modelado de bloques que contendrán marcas de tiempo, la raíz del Arbol de Merkle asociada a susansacciones y el hash de enlace con el bloque anterior
3.  **Demostración de inmutabilidad** - Validación de la integridad matemática de toda la cadena

---

## Arquitectura

TBD  
Voy a utilizar el patrón de diseño **Composite** en donde se facilitará la identificación de los nodos interno y de las hojas del árbol, permitiendo la construcción de la raíz a partir de las hojas y la verificación de la integridad de los datos.

La idea es la siguiente:

1.  Todos los nodos del árbol comparten ua interfaz común capaz de responder a la pregunta de si es un nodo interno o una hoja, y de calcular su hash.
2.  La hoja calcula el hash del dato que almacena Hash\_Hoja=SHA256(dato)
3.  El nodo interno calcula el hash de sus hijos Hash\_Nodo=SHA256(Hash\_Hijo1+Hash\_Hijo2)

## Estructua del repositorio (Tentativo)

```
├── src/
│   ├── __init__.py
│   ├── merkle_tree.py    
│   └── blockchain.py     
├── main.py               
├── tests/
│   └── test_blockchain.py
└──README.md              
```