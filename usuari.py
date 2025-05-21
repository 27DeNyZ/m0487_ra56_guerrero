import re

class Usuari:
    def __init__(self, nom="None", cognoms="None", dni="None"):
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni

    def imprimir_dades(self):
        return f"{self.nom} {self.cognoms} - DNI: {self.dni}"

    def introduir_dades(self):
        self.nom = input("Nom: ")
        self.cognoms = input("Cognoms: ")

        while True:
            self.dni = input("DNI (format 12345678A): ")
            if self.dni_valid(self.dni):
                break
            print("DNI no vàlid. Ha de tenir 8 números seguits d'una lletra.")

    def dni_valid(self, dni):
        return bool(re.match(r'^\d{8}[A-Za-z]$', dni))
