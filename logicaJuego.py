from numeroAleatorio import numero_aletorio
from configuracion import limite_inferior, limite_superior, numero_intentos
import consola

def logica_usuario() -> None:
    numero = numero_aletorio(limite_inferior, limite_superior)
    print(numero)

    numero_usuario = consola.pedir_int(f'Elige un numero entre {limite_inferior} y {limite_superior}: ')
    print(numero_usuario)

def logica_computadora() -> None:
    print('Opcion 2')