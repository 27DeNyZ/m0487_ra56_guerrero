import sqlite3
import hashlib
from datetime import date
from usuari_registrat import UsuariRegistrat


class Biblioteca:
    """
    Classe per gestionar la base de dades de la biblioteca.
    """
    def __init__(self):
        self.conn = sqlite3.connect("biblioteca.db")

    def crear_taules(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuaris (
                        dni TEXT PRIMARY KEY, 
                        nom TEXT, 
                        cognoms TEXT,
                        tipus_usuari TEXT,
                        contrasenya TEXT
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
            cursor.execute(
                "INSERT INTO usuaris (dni, nom, cognoms, tipus_usuari, contrasenya) VALUES (?, ?, ?, ?, ?)",
                (usuari.dni, usuari.nom, usuari.cognoms, usuari.tipus_usuari, usuari.contrasenya)
            )
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

        cursor.execute("SELECT COUNT(*) FROM llibres WHERE dni_prestec = ?", (dni,))
        prestats = cursor.fetchone()[0]
        if prestats >= 3:
            print("Aquest usuari ja té 3 llibres en préstec.")
            return

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


    def get_usuari_per_dni(self, dni):
        cursor = self.conn.cursor()
        cursor.execute("SELECT dni, nom, cognoms, tipus_usuari, contrasenya FROM usuaris WHERE dni = ?", (dni,))
        fila = cursor.fetchone()
        if fila:
            usuari = UsuariRegistrat(
                nom=fila[1],
                cognoms=fila[2],
                dni=fila[0],
                contrasenya=fila[4],
                tipus_usuari=fila[3]
            )
            return usuari
        return None


    def crear_admin_per_defecte(self):
        cursor = self.conn.cursor()
        dni_admin = "12345678A"
        cursor.execute("SELECT * FROM usuaris WHERE dni = ?", (dni_admin,))
        if cursor.fetchone() is None:
            contrasenya = self.hashear_contrasenya("admin")
            cursor.execute('''
                INSERT INTO usuaris (dni, nom, cognoms, tipus_usuari, contrasenya)
                VALUES (?, ?, ?, ?, ?)
            ''', (dni_admin, "Admin", "Default", "admin", contrasenya))
            self.conn.commit()


    def hashear_contrasenya(self, contrasenya):
        return hashlib.sha256(contrasenya.encode()).hexdigest()


        