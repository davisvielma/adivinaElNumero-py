# Adivina el numero  

Es un juego de adivinanzas de números, donde interactúan dos partes. La primera escoge un numero entre un rango previamente establecido y la segunda intenta adivinar el numero en una serie de intentos determinados.

## Nuestro programa

Como se menciono anteriormente el juego consiste en adivinar un numero, se ha establecido dos modalidades de juego:

1. Usuario :man:: el actor principal (usuario), adivina el numero que aleatoriamente elija la computadora.
2. Computadora :computer:: el usuario elije un numero dentro del rango y la computadora intentara adivinar dicho numero.

**Nota**: el la modalidad *computadora* esta tendrá 3 intentos mas que la modalidad *usuario*.

## Configuraciones :wrench:
Hemos escrito un archivo *configuraciones.py*, donde se definen el numero de intentos establecidos en 10 y el rango de números a adivinar en este caso de 1 a 1000.