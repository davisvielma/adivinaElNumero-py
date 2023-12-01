from numeroAleatorio import numero_aletorio
from configuracion import limite_inferior, limite_superior, numero_intentos
import consola

def logica_usuario() -> None:
    intento = 1
    numero = numero_aletorio(limite_inferior, limite_superior)
    #print(numero)

    while intento <= numero_intentos:
        try:
            print()
            numero_usuario = consola.pedir_int(f'Elige un numero entre {limite_inferior} y {limite_superior}: ')
            
            if numero_usuario < limite_inferior or numero_usuario > limite_superior:
                print('antes de entrar en el supuesto error')
                raise ValueError
            
            print()
            intentos_restantes = numero_intentos - intento
            intento_str = 'intentos' if intentos_restantes != 1 and intento != 1 else 'intento'

            if numero_usuario < numero:
                print(f'Tu numero es menor. Te queda {intentos_restantes} {intento_str}.')
            elif numero_usuario > numero:
                print(f'Tu numero es mayor. Te queda {intentos_restantes} {intento_str}.')
            else:
                print(f'\nGanaste!!! El numuero a adivinar era {numero} y lo hiciste en {intento} {intento_str}.')
                break
            
            intento += 1

        except ValueError:
            print(f'\nError!!! Ingrese una opcion valida.')
    else:
        print(f'\nHas perdido!!! El numero a adivinar era {numero}')

def logica_computadora() -> None:
    print('Opcion 2')