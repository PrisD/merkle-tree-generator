import unittest
from src.arbol_merkle import ArbolMerkle


class TestArbolMerkle(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test para imprimir un separador visual."""
        print("\n" + "=" * 60)

    def test_creacion_arbol_par(self):
        """Prueba la construcción de un árbol con cantidad par de hojas."""
        print("▶ Ejecutando: test_creacion_arbol_par")
        datos = ["Tx1", "Tx2", "Tx3", "Tx4"]
        arbol = ArbolMerkle(datos)

        raiz = arbol.obtener_raiz()
        print(f"  [+] Datos de entrada: {datos}")
        print(f"  [+] Hash Raíz generado: {raiz}")

        self.assertIsNotNone(raiz, msg="La raíz no debería ser None")
        self.assertEqual(len(raiz), 64, msg="El hash SHA-256 debe tener 64 caracteres")
        self.assertFalse(arbol.raiz.es_hoja, msg="La raíz de un árbol con datos no puede ser una hoja")
        print("  ✔ Prueba de árbol par finalizada con éxito.")

    def test_creacion_arbol_impar(self):
        """Prueba que el árbol maneje correctamente una lista impar de datos."""
        print("▶ Ejecutando: test_creacion_arbol_impar")
        datos_impares = ["Tx1", "Tx2", "Tx3"]
        arbol = ArbolMerkle(datos_impares)

        raiz = arbol.obtener_raiz()
        print(f"  [+] Datos impares de entrada (3 elementos): {datos_impares}")
        print(f"  [+] Hash Raíz (con duplicación interna de Tx3): {raiz}")

        self.assertIsNotNone(raiz)
        self.assertEqual(len(raiz), 64)
        print("  ✔ Prueba de árbol impar finalizada con éxito.")

    def test_lista_vacia_lanza_excepcion(self):
        """Prueba que intentar instanciar un árbol vacío lance un ValueError."""
        print("▶ Ejecutando: test_lista_vacia_lanza_excepcion")
        print("  [+] Verificando que lanzar lista vacía [] arroje ValueError...")

        with self.assertRaises(ValueError):
            ArbolMerkle([])

        print("  ✔ Excepción capturada correctamente.")

    def test_efecto_avalancha_raiz(self):
        """Prueba que un cambio mínimo en los datos altere completamente la raíz."""
        print("▶ Ejecutando: test_efecto_avalancha_raiz")
        datos1 = ["Alice paga 10 BTC a Bob", "Bob paga 5 BTC a Charlie"]
        datos2 = ["Alice paga 10 BTC a Bob", "Bob paga 6 BTC a Charlie"]  # Cambió un solo número

        arbol1 = ArbolMerkle(datos1)
        arbol2 = ArbolMerkle(datos2)

        raiz1 = arbol1.obtener_raiz()
        raiz2 = arbol2.obtener_raiz()

        print(f"  [+] Original: {datos1[1]}")
        print(f"      Raíz 1: {raiz1}")
        print(f"  [+] Modificado: {datos2[1]}")
        print(f"      Raíz 2: {raiz2}")

        self.assertNotEqual(raiz1, raiz2, msg="Las raíces no deberían coincidir ante una modificación")
        print("  ✔ Efecto avalancha verificado correctamente (hashes totalmente distintos).")


if __name__ == '__main__':
    unittest.main()