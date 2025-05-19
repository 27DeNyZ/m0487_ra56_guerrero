import unittest
from usuari import Usuari
from biblioteca import Biblioteca

class TestUsuari(unittest.TestCase):
    def test_creacio_usuari(self):
        u = Usuari("Anna", "Martínez", "12345678A")
        self.assertEqual(u.nom, "Anna")
        self.assertEqual(u.dni, "12345678A")

    def test_dni_valid(self):
        u = Usuari()
        self.assertTrue(u.dni_valid("12345678A"))
        self.assertFalse(u.dni_valid("1234"))
        self.assertFalse(u.dni_valid("ABCDEFGH1"))


if __name__ == '__main__':
    unittest.main()
