import sqlite3

class Biblioteca:
    def __init__(self):
        self.conn = sqlite3.connect("biblioteca.db")

    def crear_taules(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuaris (dni TEXT PRIMARY KEY, nom TEXT, cognoms TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS llibres (titol TEXT PRIMARY KEY, autor TEXT, dni_prestec TEXT)''')
        self.conn.commit()

    def afegir_usuari(self, usuari):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO usuaris VALUES (?, ?, ?)", (usuari.dni, usuari.nom, usuari.cognoms))
        self.conn.commit()

    def afegir_llibre(self, llibre):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO llibres VALUES (?, ?, ?)", (llibre.titol, llibre.autor, llibre.dni_prestec))
        self.conn.commit()

    def imprimir_usuaris(self):
        cursor = self.conn.cursor()
        for row in cursor.execute("SELECT * FROM usuaris"):
            print(f"{row[1]} {row[2]} - DNI: {row[0]}")

    def imprimir_llibres(self, filtre="tots"):
        cursor = self.conn.cursor()
        query = "SELECT * FROM llibres"
        for row in cursor.execute(query):
            estat = "Disponible" if row[2] == "None" else f"Préstec per DNI: {row[2]}"
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
        cursor.execute("UPDATE llibres SET dni_prestec = ? WHERE titol = ? AND dni_prestec = 'None'", (dni, titol))
        self.conn.commit()

    def tornar_llibre(self, titol):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE llibres SET dni_prestec = 'None' WHERE titol = ?", (titol,))
        self.conn.commit()
        
def actualitzar_usuari(self, dni, nou_nom, nous_cognoms):
    cursor = self.conn.cursor()
    cursor.execute("UPDATE usuaris SET nom = ?, cognoms = ? WHERE dni = ?", (nou_nom, nous_cognoms, dni))
    self.conn.commit()

def actualitzar_llibre(self, titol, nou_autor):
    cursor = self.conn.cursor()
    cursor.execute("UPDATE llibres SET autor = ? WHERE titol = ?", (nou_autor, titol))
    self.conn.commit()


