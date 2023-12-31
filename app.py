import consola
from logicaJuego import logica_usuario, logica_computadora

def juego() -> None:
    opcion = 0

    while opcion < 1 or opcion > 3:
        try:
            consola.menu_principal()
            opcion = consola.pedir_int('*Elija una opción: ')
            
            if opcion < 1 or opcion > 3:
                raise ValueError
        
        except ValueError:
            print(f'\nError!!! Ingrese una opción valida.')

    if opcion == 1:
        logica_usuario()
    elif opcion == 2:
        logica_computadora()
    else:
        print('\nFin del juego.')

if __name__ == '__main__':
    print('\n\t\tBienvenido al juego adivina el numero')
    juego()