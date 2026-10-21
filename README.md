# 🚢 Hundir la Flota

## 📌 Descripción

Este proyecto consiste en desarrollar una versión del juego **Hundir la Flota utilizando Python**. El jugador se enfrenta a la máquina mediante un sistema de turnos, realizando disparos sobre un tablero para intentar hundir todos los barcos del oponente.

El juego termina cuando uno de los dos jugadores se queda sin barcos.

## 🎮 Características

- Tableros de 10 filas y 10 columnas.
- Juego por turnos entre el usuario y la máquina.
- Colocación de barcos mediante posiciones definidas en el código.
- Disparos del usuario mediante coordenadas de fila y columna.
- Generación aleatoria de coordenadas para los disparos de la máquina.
- Detección de impactos, disparos al agua y disparos repetidos.
- Comprobación automática de la condición de victoria.
- Validación de las coordenadas introducidas por el usuario.

## 📁 Estructura del proyecto

```text
HLF_YERAY/
├── main.py
├── clases.py
├── funciones.py
├── variables.py
└── README.md
```

### `main.py`

Es el archivo principal del programa. Se encarga de crear los tableros, iniciar la partida, gestionar los turnos y comprobar cuándo termina el juego.

### `clases.py`

Contiene la clase `Tablero`, responsable de inicializar las matrices, colocar los barcos, mostrar los tableros y gestionar los disparos del usuario y de la máquina.

### `funciones.py`

Incluye funciones auxiliares para convertir las letras de las filas en índices numéricos y comprobar si todavía quedan barcos en un tablero.

### `variables.py`

Define las constantes utilizadas en el juego, como las dimensiones del tablero y los símbolos que representan los barcos, los impactos, el agua y las casillas vacías.

## ⚙️ Requisitos

- Python 3.
- No se necesitan librerías externas para la versión actual del proyecto.

## ▶️ Cómo ejecutar el juego

1. Descarga o clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando:

```bash
python3 main.py
```

Sigue las instrucciones que aparecen en la terminal para introducir las coordenadas de tus disparos.

Las filas se identifican mediante letras de la A a la J y las columnas mediante números del 0 al 9.

## 🧠 Conceptos de Python utilizados

Durante el desarrollo del proyecto se han trabajado los siguientes conceptos:

- Programación orientada a objetos mediante clases y métodos.
- Funciones y separación del código en módulos.
- Variables y constantes.
- Listas y matrices bidimensionales.
- Bucles `for` y `while`.
- Condicionales `if`, `elif` y `else`.
- Gestión de errores mediante `try` y `except`.
- Conversión y validación de datos introducidos por el usuario.
- Generación de números aleatorios con el módulo `random`.
- Valores de retorno como `True`, `False` y `None`.

## 🚀 Posibles mejoras

- Colocar los barcos de forma aleatoria.
- Evitar que la máquina repita disparos.
- Mejorar la visualización de los tableros.
- Añadir un sistema para detectar cuándo un barco completo ha sido hundido.
- Incorporar pruebas para comprobar el funcionamiento de las distintas partes del programa.

## 👨‍💻 Autor

Proyecto desarrollado como ejercicio de aprendizaje de Python en el ámbito de Data Science & AI.
