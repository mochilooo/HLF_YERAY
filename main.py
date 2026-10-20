"""

Introducción


En esta entrega vas a crear tu propio juego de **Hundir la flota** en Python. Para el desarrollo del programa necesitarás conocimientos de módulos, bucles, funciones,
clases y colecciones de Python. **La entrega deberá constar de  varios scripts de Python (archivos .py), nada de jupyter notebooks**.


¿Cómo funciona el juego?


Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: tú y la máquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria.Ahora bien, puedes empezar colocando los barcos en
unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos,
y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.


Desarrollo


Tendrás que desarrollar lo siguiente:
1. Necesitarás un conjunto de **constantes**, donde tengas inventariados los barcos del juego, dimensiones y demás variables que no vayan a cambiar que tendréis
definidas en archivo de **variables.py**

2. Tendrás que construir **una clase Tablero**. Para facilitar el desarrollo, la mejor opción es desarrollar una clase tablero donde implementes las siguientes
funcionalidades:
    * Cuando se inicialice deberás asignar
        * Un id de jugador, para saber de quién es el tablero.
        * Unas dimensiones de tablero, que en el fondo serán tus constantes 10 x 10.
        * Unos barcos. Los que hayas definido como constantes. Aqui simplemente puedes pasar, por ejemplo, un diccionario donde especifiques el nombre de tus barcos,
        y la eslora de cada uno. Luego ya los colocarás en el tablero.
        * **Un tablero sin barcos, que será una lista de listas** donde posicionarás los barcos. Este tablero está vacío, por lo que lo puedes rellenar de 0s, 1s,
        o el caracter que consideres.
        * Adicionalmente la clase tablero necesitará otra lista de listas, ¿por qué? porque el tablero de la máquina tendrá internamente una lista de listas con sus
        barcos (lo que no vemos) y hará falta otra lista de listas (que sí veremos nosotros) con los disparos efectuados, para saber dónde tenemos que disparar.
    * **Inicializar el tablero**, es decir, colocar los barcos. Puedes pasar por alto el hecho de que tengan que tener espacios entre ellos pero si los colocas
    aleatoriamente, mucho cuidado aquí de poner los barcos dentro del tablero, y de no colocar unos barcos encima de otros :)
    * Necesitarás un método de **disparo coordenada**. Cuando hay un disparo de un jugador en ese tablero, tendrás que comprobar si ahi había un barco, o simplemente
    agua. Acuérdate de marcar en el tablero, tanto si hay un impacto, como si dio agua.
    * NO te ciñas a los métodos que te acabo de mencionar, crea todos los que necesites, introduce en el constructor lo que quieras y desarrolla las funciones que
    consideres oportunas para facilitarte el desarrollo.

3. Una vez ya tienes modelizado tu tablero, hay que montar el programa que se ejecutara desde un **main.py**:
    * El programa no es más que el **típico `while true: `, con una serie de inputs del usuario**. Se está ejecutando constantemente y le pide al usuario coordenadas
    para comprobar si impacta.
    * Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
    * A continuación **inicializa los tableros de ambos jugadores** con los barcos. Estas dos primeras acciones solo se ejecutan una vez!! Que es el comienzo del juego.
    * Después de eso ya comienza el juego. Básicamente **se irá ejecutando iterativamente en el `while`, y le irá preguntando coordenadas al usuario.**
    * Recoges coordenadas, compruebas en el tablero de la máquina si habia barco.
        * Hay barco: marca en el tablero de la maquina el impacto y le vuelve a tocar al usuario
        * No hay barco: le toca a la maquina. O lo que es lo mismo, escoge una coordenada aleatoria, y comprueba en el tablero del usuario si habia barco.
    * **Así hasta que uno de los dos jugadores se quede sin barcos, y termina el juego.**
    * Cuando empiece tu turno deberías imprimir por pantalla tu tablero, para ver cuántos impactos te ha hecho la máquina, así como el tablero con los impactos que has
    hecho tu en el adversario, de manera que te sirva de ayuda para el siguiente disparo.
    * Todas aquellas funciones que puedas construir para la ejecución de este programa deberán estar definidas en un script que se llame **funciones.py**.

Hay infinidad de maneras para resolver este ejercicio, por lo que siéntete libre de implementarlo de la forma que te resulte más cómoda.


Recomendaciones


1. **No es necesario tener una clase barco, aunque puede ser recomendable** con los barcos de cada jugador, cuáles están tocados y demás. Simplemente con llevar un
inventario de las coordenadas con barco es suficiente. Por ejemplo, si el tablero tuviese 2 barcos de 4 posiciones de eslora, es como si tuvieses 8 vidas. Cuando se te
acaban las vidas, pierdes.
2. Para implementar el bucle `while`, puedes usar **sentencias `continue`, `break`**.
3. Se recomienda tener el código separado en **varios scripts**. Por ejemplo:
    * main.py: donde corre todo el programa
    * clases.py: aquí irán las clases
    * funciones.py: aquí irán las funciones
    * variables.py: donde están declaradas las constantes
    * A gusto del desarrollador...
4. Cuando se imprime el tablero por pantalla, básicamente será un `print()` de la lista de listas. Escoge con sentido qué quieres que se imprima por pantalla,
de manera que se vea bien dónde hay barco, donde ha habido impacto, agua... Tendrás los siguients casos:
    * Agua donde no se ha impactado
    * Agua donde se ha impactado
    * Barco donde no se ha impactado
    * Barco donde se ha impactado
5. Se recomienda en la clase tablero manejar dos arrays de 10x10. Uno con las coordenadas de los barcos y los impactos, que será tu tablero, lo que veas tu cuando
imprimes tu tablero por pantalla. Y otro tablero SIN los barcos, únicamente con los impactos, para ver qué impactos has hecho en el tablero de la maquina.
6. Si vas a posicionar los barcos de manera aleatoria, tendrás que escoger unas coordenadas aleatoriamente, y una orientación N/S/E/O, de manera que si tu barco
tiene 3 de eslora y la orientación es N, se posicionará hacia arriba, desde la posición inicial elegida aleatoriamente.

"""


# Crear un Tablero como una lista de listas de 10x10 que contenga caracteres espacio: " "
tablero = []                # Se crea el tablero que sera una lista de listas.

for i in range(10):
    linea = []              # Se crea una lista nueva antes de usarla.
    
    for j in range(10):
        linea.append(" ")   # Se añade un espacio hasta 10 para rellenar la línea.
    tablero.append(linea)   # Cuando se completa la línea se añade otra lista en la siguiente línea en el tablero.


# Insertar dos barcos sustituyendo en el Tablero los espacios en blanco por el caracter "B":
#   Uno de 4 casillas en horizontal: casillas [1][0], [1][1], [1][2], [1][3]

tablero[1][0] = "B"
tablero[1][1] = "B"
tablero[1][2] = "B"
tablero[1][3] = "B"

#   Uno de 3 casillas en vertical:   casillas [3][3], [4][3], [5][3]

tablero[3][3] = "B"
tablero[4][3] = "B"
tablero[5][3] = "B"

#Escribir una celda de código separada de las anteriores para simular que el usuario está efectuando un disparo: 

def disparar():
    coordenada1 = int(input("Introduzca las coordenada fila"))
    while 0 > coordenada1 > 9:
        print("Coordenada no válida")
        coordenada1 = int(input("Introduzca las coordenada fila"))
    coordenada2 = int(input("Introduzca las coordenada columna"))
    while 0 > coordenada2 > 9:
        print("Coordenada no válida")
        coordenada2 = int(input("Introduzca las coordenada columna"))

    if tablero[coordenada1][coordenada2] == " ":
        print("Agua")
        tablero[coordenada1][coordenada2] = "o"
        return False

    elif tablero[coordenada1][coordenada2] == "B":
        print(f"Tocado en posición [{coordenada1}][{coordenada2}] ")
        tablero[coordenada1][coordenada2] = "x"
        return True

    else:
        print("Ya has disparado ahí")


# Para introducir en consola y que el formato se siga viendo en filas y columnas

def imprimirtablero():
    for fila in tablero:
        for columna in fila:
            print(f"[{columna}]", end=" ")
        print(" ")



imprimirtablero()

while True:
    resultado = disparar()
    imprimirtablero()

    if resultado == False:
        break