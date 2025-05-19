import sqlite3
from datetime import date


class Biblioteca:
    """
    Classe per gestionar la base de dades de la biblioteca.
    """
    def __init__(self):
        self.conn = sqlite3.connect("biblioteca.db")

    def crear_taules(self):
        """
        Crea les taules de la base de dades si no existeixen.
        """
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuaris (
                            dni TEXT PRIMARY KEY, 
                            nom TEXT, 
                            cognoms TEXT
                          )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS llibres (
                            titol TEXT PRIMARY KEY, 
                            autor TEXT, 
                            dni_prestec TEXT, 
                            data_prestec TEXT
                          )''')
        self.conn.commit()

    def afegir_usuari(self, usuari):
        cursor = self.conn.cursor()
    try:
        cursor.execute("INSERT INTO usuaris VALUES (?, ?, ?)", (usuari.dni, usuari.nom, usuari.cognoms))
        self.conn.commit()
    except sqlite3.IntegrityError:
        print("L'usuari ja existeix a la base de dades.")


    def afegir_llibre(self, llibre):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO llibres VALUES (?, ?, ?, ?)", (llibre.titol, llibre.autor, llibre.dni_prestec, None))
        self.conn.commit()

    def imprimir_usuaris(self):
        cursor = self.conn.cursor()
        for row in cursor.execute("SELECT * FROM usuaris"):
            print(f"{row[1]} {row[2]} - DNI: {row[0]}")

    def imprimir_llibres(self, filtre="tots"):
        cursor = self.conn.cursor()
        for row in cursor.execute("SELECT * FROM llibres"):
            estat = "Disponible" if row[2] == "None" or row[2] is None else f"Préstec per DNI: {row[2]}"
            print(f"{row[0]} - {row[1]} ({estat})")

    def eliminar_usuari(self, dni):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuaris WHERE dni = ?", (dni,))
        self.conn.commit()

    def eliminar_llibre(self, titol):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM llibres WHERE titol = ?", (titol,))
        self.conn.commit()

    def prestar_llibre(self, titol, dni):
        cursor = self.conn.cursor()

        # Comprovar si l'usuari ja té 3 llibres
        cursor.execute("SELECT COUNT(*) FROM llibres WHERE dni_prestec = ?", (dni,))
        prestats = cursor.fetchone()[0]
        if prestats >= 3:
            print("Aquest usuari ja té 3 llibres en préstec.")
            return

        # Comprovar disponibilitat del llibre
        avui = date.today().isoformat()
        cursor.execute(
            "UPDATE llibres SET dni_prestec = ?, data_prestec = ? WHERE titol = ? AND (dni_prestec = 'None' OR dni_prestec IS NULL)",
            (dni, avui, titol)
        )

        if cursor.rowcount == 0:
            print("El llibre no està disponible o no existeix.")
        else:
            print("Préstec realitzat correctament.")

        self.conn.commit()

    def tornar_llibre(self, titol):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE llibres SET dni_prestec = 'None', data_prestec = NULL WHERE titol = ?", (titol,))
        self.conn.commit()

    def actualitzar_usuari(self, dni, nou_nom, nous_cognoms):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE usuaris SET nom = ?, cognoms = ? WHERE dni = ?", (nou_nom, nous_cognoms, dni))
        self.conn.commit()

    def actualitzar_llibre(self, titol, nou_autor):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE llibres SET autor = ? WHERE titol = ?", (nou_autor, titol))
        self.conn.commit()
