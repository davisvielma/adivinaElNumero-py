import consola
from logicaJuego import logica_usuario, logica_computadora

def juego() -> None:
    opcion = 0

    while opcion < 1 or opcion > 3:
        try:
            consola.menu_principal()
            opcion = consola.pedir_int('*Elija una opcion: ')
            
            if opcion < 1 or opcion > 3:
                raise ValueError
        
        except ValueError:
            print(f'\nError!!! Ingrese una opcion valida.')

    if opcion == 1:
        logica_usuario()
    elif opcion == 2:
        logica_computadora()
    else:
        print('\nFin del juego.')

    # while opcion != 3:
    #     try:
    #         consola.menu_principal()
    #         opcion = consola.pedir_int('Elija una opcion: ')
    #         print()
            
    #         if opcion == 1:
    #             logica_usuario()
    #         elif opcion == 2:
    #             logica_computadora()
    #         elif opcion == 3:
    #             continue
    #         else:
    #             raise ValueError
        
    #     except ValueError:
    #         print(f'\nError!!! Ingrese una opcion valida.')


if __name__ == '__main__':
    print('\n\t\tBienvenido al juego adivina el numero')
    juego()