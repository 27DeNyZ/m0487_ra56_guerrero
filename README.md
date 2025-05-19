# m0487_ra56_guerrero

### V1

# NOTACIÓ
Fran, he creat una nova branca que es diu actualització ja que m'havia oblidat de fer diferents coses com el menú i altres tests. Faig el merge però era per deixar-ho clar, ja que pot ser una mica lios.


# Biblioteca - Gestió de Llibres i Usuaris amb SQLite3
Aquest projecte implementa una biblioteca digital que permet gestionar llibres i usuaris fent servir una base de dades SQLite3.
Permet afegir, eliminar i llistar llibres i usuaris, així com gestionar préstecs i tornades de llibres.

## Funcionalitats
### Gestió de llibres:

    -Afegir, llistar i eliminar llibres.

    -Assignar un llibre en préstec a un usuari.

    -Tornar un llibre a la biblioteca.

### Gestió d'usuaris:

    -Afegir, llistar i eliminar usuaris.

### Ús de base de dades SQLite3:

    -Els llibres i usuaris es guarden a biblioteca.db.
    -Les taules es creen automàticament si no existeixen.
    -Es fan consultes SQL per gestionar la informació.

### Control d'errors:

    -Validació de dades amb try-except.
    -Control d'errors per a DNIs repetits.
    -Evita introduir dades incorrectes o buides.

### Instal·lació i ús
    -Utilitzar un repositori github i Visual Studio Code
    -Executa el programa: 
        python biblioteca.py
    -Segueix el menú per gestionar la biblioteca.

### Base de dades SQLite3
El programa fa servir una base de dades anomenada biblioteca.db amb dues taules principals:

    -Taula usuaris

id	nom	cognoms	dni
1	Paco	Ross	12345678A
2	Maria	Tendas	87654321B

    -Taula llibres

id	titol	autor	dni_prestec
1	1984	Orwell	12345678A
2	Dune	Herbert	0
Si dni_prestec = "0", el llibre està disponible.

Si dni_prestec conté un DNI, el llibre està en préstec.

### Menú principal
Quan executes el programa, veuràs aquest menú:

1) Llistar Llibres
2) Introduir Llibres
3) Eliminar Llibres
4) Llistar Usuaris
5) Introduir Usuaris
6) Eliminar Usuaris
7) Prèstec Llibres
8) Tornar Llibres
0) Sortir del programa
    -Introdueix un número i segueix les instruccions.

### Tecnologies utilitzades
    -Python 3 
    -SQLite3 
    -Try-Except per control d'errors
    -Unittest

### Millores possibles:
    -Actualitzar dades de llibre i usuaris.
    -Que el dni compleixi el patró d'un DNI convencional.
    -Tenir en compte el temps (màxim un mes) i la quantitat (màxim 3 llibres)
    -Realitzar unittest per les diferents classes i metodes.

    -Afegir una interfície gràfica amb Tkinter.
    -Implementar una API REST amb FastAPI.
    -Permetre exportar i importar dades a CSV o JSON.




### V2

# Afegim herència a usuari comprovant l'usuari registrat
Realitzem l'herència de la classe Usuari amb una nova classe anomenada UsuariResgistrat

## Funcionalitats
### Gestió de llibres:

    -Afegir, llistar i eliminar llibres.

    -Assignar un llibre en préstec a un usuari.

    -Tornar un llibre a la biblioteca.

### Gestió d'usuaris:

    -Afegir, llistar i eliminar usuaris.

### Ús de Hashlib i getpass

    - Fem ús del hashlib i del getpass pel control de contrasenyes, codificació, etc.

### Control d'errors:

    - Executem testing del nostre programa

### Instal·lació i ús
    -Utilitzar un repositori github i Visual Studio Code
    -Executa el programa: 
        python menu.py
    -Segueix el menú per gestionar la biblioteca.

### Menú principal
Quan executes el programa, veuràs aquest menú:

1) Llistar Llibres
2) Introduir Llibres
3) Eliminar Llibres
4) Llistar Usuaris
5) Introduir Usuaris
6) Eliminar Usuaris
7) Prèstec Llibres
8) Tornar Llibres
0) Sortir del programa
    -Introdueix un número i segueix les instruccions.

### Tecnologies utilitzades
    -Python 3 
    -SQLite3 
    -Try-Except per control d'errors
    -Unittest
    -Hashlib
    -Getpass

### Millores possibles:
    -Actualitzar dades de llibre i usuaris.
    -Que el dni compleixi el patró d'un DNI convencional.
    -Tenir en compte el temps (màxim un mes) i la quantitat (màxim 3 llibres)
    -Realitzar unittest per les diferents classes i metodes.

    -Afegir una interfície gràfica amb Tkinter.
    -Implementar una API REST amb FastAPI.
    -Permetre exportar i importar dades a CSV o JSON.


### Crèdits
Creat per [Denís Guerrero Rodríguez], 2025.
El Teu GitHub: https://github.com/27DeNyZ/m0487_ra56_guerrero.git