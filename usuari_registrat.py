from usuari import Usuari
import hashlib
import getpass

class UsuariRegistrat(Usuari):
    """
    Classe que representa un usuari registrat, que hereta de la classe Usuari.
    Afegeix gestió de contrasenya i tipus d'usuari (lector o admin).
    """
    
    def __init__(self, nom="None", cognoms="None", dni="None", tipus_usuari="lector"):
        super().__init__(nom, cognoms, dni)
        self._contrasenya = None
        self.tipus_usuari = tipus_usuari if tipus_usuari in ["lector", "admin"] else "lector"

    def _encripta_contrasenya(self, contrasenya):
        """
        Encripta la contrasenya amb l'algorisme SHA-256.
        """
        return hashlib.sha256(contrasenya.encode()).hexdigest()

    def verificar_contrasenya(self, contrasenya):
        """
        Comprova si la contrasenya introduïda coincideix amb la encriptada.
        """
        return self._contrasenya == self._encripta_contrasenya(contrasenya)

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
