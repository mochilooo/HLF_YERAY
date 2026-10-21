def quedan_barcos(tablero):
    # Recorrer todas las filas del tablero
    for fila in tablero.tablero:

        # Recorrer todas las casillas de cada fila
        for casilla in fila:

            # Si encuentra una casilla con un barco, devuelve True
            if casilla == "B":
                return True

    # Si termina de recorrer el tablero y no encuentra barcos, devuelve False
    return False


def convertir_fila(fila_letra):
    # Convertir la letra de la fila en su índice numérico
    match fila_letra:
        case "A":
            return 0  # La fila A corresponde al índice 0
        case "B":
            return 1  # La fila B corresponde al índice 1
        case "C":
            return 2  # La fila C corresponde al índice 2
        case "D":
            return 3  # La fila D corresponde al índice 3
        case "E":
            return 4  # La fila E corresponde al índice 4
        case "F":
            return 5  # La fila F corresponde al índice 5
        case "G":
            return 6  # La fila G corresponde al índice 6
        case "H":
            return 7  # La fila H corresponde al índice 7
        case "I":
            return 8  # La fila I corresponde al índice 8
        case "J":
            return 9  # La fila J corresponde al índice 9
        case _: 
            return None  # Si la letra no es válida, devuelve None