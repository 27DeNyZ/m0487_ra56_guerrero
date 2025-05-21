from usuari import Usuari
import hashlib
import getpass

class UsuariRegistrat(Usuari):
    def __init__(self, tipus_usuari="lector", **kwargs):
        """
        Constructor de la classe UsuariRegistrat, que hereta de Usuari.

        Paràmetres:
        - tipus_usuari: str -> 'lector' o 'admin'
        - **kwargs: dict -> altres atributs heretats de Usuari (nom, cognoms, dni)
        """
        super().__init__(**kwargs)
        self._contrasenya = None
        self.tipus_usuari = tipus_usuari


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
