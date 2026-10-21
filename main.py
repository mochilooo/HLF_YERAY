"""
HUNDIR LA FLOTA

"""

from clases import Tablero  # Importamos la clase Tablero
from funciones import quedan_barcos, convertir_fila  # Importamos las funciones necesarias

# Creamos los tableros de los dos jugadores
tablero_usuario = Tablero("Usuario")
tablero_maquina = Tablero("Máquina")

# Colocamos los barcos en ambos tableros
tablero_usuario.colocar_barcos()
tablero_maquina.colocar_barcos()

turno = "usuario"  # El usuario empieza la partida

while True:  # Repetimos los turnos hasta que alguien gane

    if turno == "usuario":  # Comprobamos si le toca jugar al usuario

        print("\n--- TU TURNO ---")

        try:
            fila_letra = input("Fila (A-J): ").upper()  # Pedimos la fila como letra
            columna = int(input("Columna (0-9): "))  # Pedimos la columna como número
        except ValueError:
            print("Error: introduce una letra y un número.")  # Avisamos del error
            continue  # Volvemos a pedir las coordenadas

        fila = convertir_fila(fila_letra)  # Convertimos la letra en número

        if fila is None:  # Comprobamos si la letra es válida
            print("Fila incorrecta. Introduce una letra de la A a la J.")
            continue  # Volvemos a pedir las coordenadas

        if columna < 0 or columna > 9:  # Comprobamos si la columna es válida
            print("Columna incorrecta. Introduce un número del 0 al 9.")
            continue  # Volvemos a pedir las coordenadas

        resultado = tablero_maquina.disparar(fila, columna)  # Disparamos a la máquina

        print("\nTus disparos:")
        tablero_maquina.imprimirtablero(tablero_maquina.disparos)  # Mostramos tus disparos

        if not quedan_barcos(tablero_maquina):  # Comprobamos si quedan barcos de la máquina
            print("¡Has ganado! Has hundido todos los barcos.")
            break  # Terminamos la partida

        if resultado is False:  # Si fallamos, termina nuestro turno
            turno = "maquina"  # Le toca jugar a la máquina

    else:  # Si no es el turno del usuario, juega la máquina

        print("\n--- TURNO DE LA MÁQUINA ---")

        resultado = tablero_usuario.disparo_maquina(tablero_usuario)  # La máquina dispara

        if not quedan_barcos(tablero_usuario):  # Comprobamos si quedan barcos del usuario
            print("¡La máquina ha ganado! Ha hundido todos tus barcos.")
            break  # Terminamos la partida

        if resultado is False:  # Si la máquina falla, termina su turno
            turno = "usuario"  # Vuelve a jugar el usuario


# Mostramos los tableros al terminar la partida
print("Tablero real de la máquina:")
tablero_maquina.imprimirtablero(tablero_maquina.tablero)

print("Disparos registrados:")
tablero_maquina.imprimirtablero(tablero_maquina.disparos)
