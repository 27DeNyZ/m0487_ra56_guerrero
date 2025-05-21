from biblioteca import Biblioteca
from usuari_registrat import UsuariRegistrat  
from llibre import Llibre


def mostrar_menu():
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Afegir usuari")
    print("2. Llistar usuaris")
    print("3. Eliminar usuari")
    print("4. Afegir llibre")
    print("5. Llistar llibres")
    print("6. Eliminar llibre")
    print("7. Prestar llibre")
    print("8. Tornar llibre")
    print("9. Actualitzar usuari")
    print("10. Actualitzar llibre")
    print("0. Sortir")

def main():
    biblio = Biblioteca()
    biblio.crear_taules()

    while True:
        mostrar_menu()
        opcio = input("Tria una opció: ")

        if opcio == "1":
            usuari = UsuariRegistrat(nom="Anna", cognoms="Serra", dni="12345678A", tipus_usuari="admin")
            usuari.introduir_dades()
            biblio.afegir_usuari(usuari)

        elif opcio == "2":
            biblio.imprimir_usuaris()

        elif opcio == "3":
            dni = input("DNI de l’usuari a eliminar: ")
            biblio.eliminar_usuari(dni)

        elif opcio == "4":
            llibre = Llibre()
            llibre.introduir_dades()
            biblio.afegir_llibre(llibre)

        elif opcio == "5":
            biblio.imprimir_llibres()

        elif opcio == "6":
            titol = input("Títol del llibre a eliminar: ")
            biblio.eliminar_llibre(titol)

        elif opcio == "7":
            titol = input("Títol del llibre a prestar: ")
            dni = input("DNI de l’usuari: ")
            biblio.prestar_llibre(titol, dni)

        elif opcio == "8":
            titol = input("Títol del llibre a tornar: ")
            biblio.tornar_llibre(titol)

        elif opcio == "9":
            dni = input("DNI de l’usuari a actualitzar: ")
            nou_nom = input("Nou nom: ")
            nous_cognoms = input("Nous cognoms: ")
            biblio.actualitzar_usuari(dni, nou_nom, nous_cognoms)

        elif opcio == "10":
            titol = input("Títol del llibre a actualitzar: ")
            nou_autor = input("Nou autor: ")
            biblio.actualitzar_llibre(titol, nou_autor)

        elif opcio == "0":
            print("Sortint del programa...")
            break

        else:
            print("Opció no vàlida. Intenta-ho de nou.")

if __name__ == '__main__':
    main()
