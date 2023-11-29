import consola

def juego() -> None:
    opcion = 0

    while opcion != 3:
        try:
            consola.menu_principal()
            opcion = consola.pedir_int('Elija una opcion: ')

            if opcion == 1:
                print('\nOpcion 1')
            elif opcion == 2:
                print('\nOpcion 2')
            elif opcion == 3:
                continue
            else:
                raise ValueError
        
        except ValueError:
            print(f'\nError!!! Ingrese una opcion valida.')


if __name__ == '__main__':
    print('\n\t\tBienvenido al juego adivina el numero')
    juego()