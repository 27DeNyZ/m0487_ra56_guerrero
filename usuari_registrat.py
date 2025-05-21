from usuari import Usuari
import hashlib
import getpass

class UsuariRegistrat(Usuari):
    def __init__(self, nom, cognoms, dni, contrasenya, tipus_usuari="lector"):
        """
        Constructor de la classe UsuariRegistrat, que hereta de Usuari.

        Paràmetres:
        - nom: str
        - cognoms: str
        - dni: str
        - contrasenya: str
        - tipus_usuari: str -> 'lector' o 'admin'
        """
        super().__init__(nom, cognoms, dni, tipus_usuari, contrasenya)
        self._contrasenya = contrasenya  
        self.tipus_usuari = tipus_usuari

    def verificar_contrasenya(self, contrasenya):
        import hashlib
        return self._contrasenya == hashlib.sha256(contrasenya.encode()).hexdigest()

    @property
    def contrasenya(self):
        return self._contrasenya

    def _encripta_contrasenya(self, contrasenya):
        """
        Encripta la contrasenya amb l'algorisme SHA-256.
        """
        return hashlib.sha256(contrasenya.encode()).hexdigest()



    def introduir_dades(self):
        """
        Demana les dades de l'usuari, incloent la contrasenya i el tipus d'usuari.
        """
        super().introduir_dades()
        while True:
            contrasenya = getpass.getpass("Contrasenya: ")
            confirmar = getpass.getpass("Repeteix la contrasenya: ")
            if contrasenya == confirmar:
                self._contrasenya = self._encripta_contrasenya(contrasenya)
                break
            print("Les contrasenyes no coincideixen. Torna-ho a intentar.")

        tipus = input("Tipus d'usuari (lector/admin): ").strip().lower()
        if tipus in ["lector", "admin"]:
            self.tipus_usuari = tipus
        else:
            print("Tipus no vàlid. Assignat per defecte com a 'lector'.")
            self.tipus_usuari = "lector"

    def imprimir_dades(self):
        """
        Retorna una cadena amb la informació de l'usuari registrat.
        """
        return f"{self.nom} {self.cognoms} - DNI: {self.dni} - Tipus: {self.tipus_usuari}"
