from numeroAleatorio import numero_aletorio
from configuracion import limite_inferior, limite_superior, numero_intentos
import consola

def logica_usuario() -> None:
    intento = 1
    numero = numero_aletorio(limite_inferior, limite_superior)

    while intento <= numero_intentos:
        try:
            numero_usuario = consola.pedir_int(f'\n*Elige un numero entre {limite_inferior} y {limite_superior}: ')
            
            if numero_usuario < limite_inferior or numero_usuario > limite_superior:
                raise ValueError
            
            intentos_restantes = numero_intentos - intento
            intento_str = 'intentos' if intentos_restantes != 1 and intento != 1 else 'intento'

            if numero_usuario < numero:
                print(f'\nTu numero es menor. Te queda {intentos_restantes} {intento_str}.')
            elif numero_usuario > numero:
                print(f'\nTu numero es mayor. Te queda {intentos_restantes} {intento_str}.')
            else:
                print(f'\nGanaste!!! El numuero a adivinar era {numero} y lo hiciste en {intento} {intento_str}.')
                break
            
            intento += 1
        except ValueError:
            print(f'\nError!!! Ingrese una opcion valida.')
    else:
        print(f'\nHas perdido!!! El numero a adivinar era {numero}.')

def logica_computadora() -> None:
    intento = 1
    numero_usuario = None
    l_i = limite_inferior
    l_s = limite_superior
    n_i = numero_intentos + 3

    while intento <= n_i:
        try:
            if not numero_usuario:
                numero_usuario = consola.pedir_int(f'\n*Elige un numero a adivinar entre {limite_inferior} y {limite_superior}: ')

                if numero_usuario < limite_inferior or numero_usuario > limite_superior:
                    raise ValueError
        
            numero = numero_aletorio(l_i, l_s)
            intentos_restantes = n_i - intento
            intento_str = 'intentos' if intentos_restantes != 1 and intento != 1 else 'intento'
            
            if numero < numero_usuario:
                l_i = numero + 1
                print(f'\nEl numero {numero} es menor. Le queda a la computadora {intentos_restantes} {intento_str}.')
            elif numero > numero_usuario:
                l_s = numero - 1
                print(f'\nEl numero {numero} es mayor. Le queda a la computadora {intentos_restantes} {intento_str}.')
            else:
                print(f'\nGano la computadora!!! El numuero a adivinar era {numero_usuario} y lo hizo en {intento} {intento_str}.')
                break

            intento += 1
        except ValueError:
            numero_usuario = None
            print(f'\nError!!! Ingrese una opcion valida.')
    else:
        print(f'\nHa perdido la computadora!!! El numero a adivinar era {numero_usuario}.')