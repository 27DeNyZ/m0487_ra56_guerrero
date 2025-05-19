class Llibre:
    def __init__(self, titol="None", autor="None", dni_prestec="None"):
        self.titol = titol
        self.autor = autor
        self.dni_prestec = dni_prestec

    def imprimir_dades(self):
        estat = "Disponible" if self.dni_prestec == "None" else f"En préstec per DNI: {self.dni_prestec}"
        return f"{self.titol} - {self.autor} ({estat})"

    def introduir_dades(self):
        self.titol = input("Títol: ")
        self.autor = input("Autor: ")
