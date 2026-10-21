
import random  # Importamos la librería para generar números aleatorios
from variables import FILAS, COLUMNAS, BARCO, TOCADO, AGUA, VACIO  # Importamos las variables del juego


class Tablero:  # Definimos la clase que representa el tablero de cada jugador

    def __init__(self, jugador):  # Inicializamos el tablero de un jugador
        self.jugador = jugador  # Guardamos el nombre del jugador
        self.tablero = []  # Creamos una lista vacía para guardar los barcos y el estado del tablero

        self.disparos = []  # Creamos una lista vacía para registrar los disparos recibidos

        for i in range(FILAS):  # Recorremos todas las filas del tablero de disparos
            fila = []  # Creamos una fila vacía

            for j in range(COLUMNAS):  # Recorremos todas las columnas de esa fila
                fila.append(VACIO)  # Añadimos una casilla vacía

            self.disparos.append(fila)  # Añadimos la fila completa al tablero de disparos

        # Creamos el tablero donde guardaremos los barcos
        for i in range(FILAS):  # Recorremos todas las filas del tablero
            fila = []  # Creamos una fila vacía

            for j in range(COLUMNAS):  # Recorremos todas las columnas de esa fila
                fila.append(VACIO)  # Añadimos una casilla vacía

            self.tablero.append(fila)  # Añadimos la fila completa al tablero


    def imprimirtablero(self, tablero):  # Método que muestra un tablero por consola
        letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # Letras que identifican las filas

        print("    ", end="")  # Preparamos la cabecera sin saltar de línea
        for columna in range(COLUMNAS):  # Recorremos las columnas
            print(f" {columna} ", end="")  # Mostramos el número de cada columna
        print()  # Saltamos de línea después de la cabecera

        for numero_fila, fila in enumerate(tablero):  # Recorremos cada fila y obtenemos su índice
            print(f" {letras[numero_fila]}  ", end="")  # Mostramos la letra correspondiente a la fila

            for casilla in fila:  # Recorremos las casillas de la fila
                print(f"[{casilla}]", end="")  # Mostramos cada casilla entre corchetes

            print()  # Saltamos de línea al terminar cada fila


    def colocar_barcos(self):  # Método que coloca los barcos en posiciones predeterminadas

        # Colocamos 4 barcos de una casilla
        self.tablero[7][7] = BARCO  # Barco en la fila 7, columna 7
        self.tablero[7][9] = BARCO  # Barco en la fila 7, columna 9
        self.tablero[5][9] = BARCO  # Barco en la fila 5, columna 9
        self.tablero[9][9] = BARCO  # Barco en la fila 9, columna 9

        # Colocamos 3 barcos de dos casillas
        self.tablero[3][6] = BARCO  # Primera casilla del primer barco
        self.tablero[4][6] = BARCO  # Segunda casilla del primer barco

        self.tablero[8][6] = BARCO  # Primera casilla del segundo barco
        self.tablero[9][6] = BARCO  # Segunda casilla del segundo barco

        self.tablero[6][7] = BARCO  # Primera casilla del tercer barco
        self.tablero[6][8] = BARCO  # Segunda casilla del tercer barco

        # Colocamos 2 barcos de tres casillas
        self.tablero[3][2] = BARCO  # Primera casilla del primer barco
        self.tablero[4][2] = BARCO  # Segunda casilla del primer barco
        self.tablero[5][2] = BARCO  # Tercera casilla del primer barco

        self.tablero[3][1] = BARCO  # Primera casilla del segundo barco
        self.tablero[4][1] = BARCO  # Segunda casilla del segundo barco
        self.tablero[5][1] = BARCO  # Tercera casilla del segundo barco

        # Colocamos 1 barco de cuatro casillas
        self.tablero[1][5] = BARCO  # Primera casilla del barco
        self.tablero[2][5] = BARCO  # Segunda casilla del barco
        self.tablero[3][5] = BARCO  # Tercera casilla del barco
        self.tablero[4][5] = BARCO  # Cuarta casilla del barco


    def disparar(self, fila, columna):  # Método que realiza un disparo en las coordenadas indicadas

        # Comprobamos si ya se ha disparado en esta posición
        if self.disparos[fila][columna] != VACIO:  # Si la casilla ya tiene una marca
            print("Ya habías disparado aquí")  # Avisamos de que ya se había disparado
            return None  # Indicamos que el disparo no se ha realizado

        # Comprobamos si hay un barco en la posición elegida
        if self.tablero[fila][columna] == BARCO:  # Si la casilla contiene un barco

            print("¡Tocado!")  # Indicamos que el disparo ha acertado

            self.tablero[fila][columna] = TOCADO  # Marcamos el impacto en el tablero real
            self.disparos[fila][columna] = TOCADO  # Registramos el impacto en el tablero de disparos

            return True  # Devolvemos True para indicar que hemos acertado

        else:  # Si la casilla no contiene un barco

            print("Agua")  # Indicamos que el disparo ha fallado

            self.tablero[fila][columna] = AGUA  # Marcamos el agua en el tablero real
            self.disparos[fila][columna] = AGUA  # Registramos el agua en el tablero de disparos

            return False  # Devolvemos False para indicar que hemos fallado


    def disparo_maquina(self, tablero_usuario):  # Método que realiza el disparo de la máquina
        fila = random.randint(0, FILAS - 1)  # Elegimos una fila aleatoria
        columna = random.randint(0, COLUMNAS - 1)  # Elegimos una columna aleatoria

        print(f"La máquina dispara a la fila {fila}, columna {columna}")  # Mostramos las coordenadas elegidas

        resultado = tablero_usuario.disparar(fila, columna)  # La máquina dispara contra el tablero del usuario

        print("\nTablero de tu flota:")  # Mostramos el título del tablero del usuario
        tablero_usuario.imprimirtablero(tablero_usuario.tablero)  # Mostramos el tablero después del disparo

        return resultado  # Devolvemos el resultado para que main.py pueda gestionar el turno
