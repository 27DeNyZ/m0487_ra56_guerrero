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
        self.dni = input("DNI: ")
