import unittest
from usuari import Usuari

class TestUsuari(unittest.TestCase):
    def test_creacio_usuari(self):
        usuari = Usuari("Marc", "Pérez", "12345678A")
        self.assertEqual(usuari.nom, "Marc")
        self.assertEqual(usuari.cognoms, "Pérez")
        self.assertEqual(usuari.dni, "12345678A")

    def test_dni_valid_correcte(self):
        usuari = Usuari()
        self.assertTrue(usuari.dni_valid("12345678A"))

    def test_dni_valid_incorrecte(self):
        usuari = Usuari()
        self.assertFalse(usuari.dni_valid("1234"))
        self.assertFalse(usuari.dni_valid("ABCDEFGH1"))
        self.assertFalse(usuari.dni_valid("87654321"))

if __name__ == '__main__':
    unittest.main()
