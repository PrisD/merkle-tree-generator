import sys
from src.models.nodo_hoja import NodoHoja
from src.arbol_merkle import ArbolMerkle


def mostrar_menu():
    print("\n=== Árbol de Merkle ===")
    print("1. Crear un árbol de Merkle")
    print("2. Mostrar árbol de Merkle")
    print("3. Consultar la raíz del árbol")
    print("4. Consultar el hash de un dato específico")
    print("5. Salir")


def crear_arbol():
    datos = []
    print("\nIngrese los datos para el árbol de Merkle (deje vacío y presione Enter para finalizar):")
    while True:
        dato = input("Dato: ").strip()
        if not dato:
            break
        datos.append(dato)

    if not datos:
        print("No se ingresaron datos. No se puede crear un árbol vacío.")
        return None

    try:
        arbol = ArbolMerkle(datos)
        print("Árbol de Merkle creado.")
        return arbol
    except ValueError as e:
        print(f"Error al crear el árbol: {e}")
        return None


def consultar_hash_dato(arbol: ArbolMerkle):
    dato = input("Ingrese el dato para consultar su hash: ").strip()
    if not dato:
        print("No se ingresó ningún dato.")
        return
    nodo_hoja_temporal = NodoHoja(dato)
    hash_dato = nodo_hoja_temporal.calcular_hash
    print(f"Hash del dato '{dato}': {hash_dato}")


def main():
    arbol_actual = None 

    while True:
        mostrar_menu()
        opcion = input("Selecione una opción (1-5): ").strip()

        if opcion == "1":
            arbol_actual = crear_arbol()

        elif opcion == "2":
            print("\n--- Estructura Gráfica del Árbol de Merkle ---")
            if arbol_actual is None:
                print("Primero debe crear un Árbol de Merkle (Opción 1).")
            else:
                print(arbol_actual.mostrar_grafico())

        elif opcion == "3":
            print("\n--- Raíz del Árbol de Merkle ---")
            if arbol_actual is None:
                print("Primero debe crear un Árbol de Merkle (Opción 1).")
            else:
                print(f"Hash de la raíz: {arbol_actual.obtener_raiz}")

        elif opcion == "4":
            print("\n--- Consultar Hash de un Dato Específico ---")
            if arbol_actual is None:
                print("Primero debe crear un Árbol de Merkle (Opción 1).")
            else:
                consultar_hash_dato(arbol_actual)


        elif opcion == "5":
            print("\nSaliendo...")
            sys.exit(0)

        else:
            print("Opción no válida. Ingrese un número entre 1 y 5.")


if __name__ == '__main__':
    main()