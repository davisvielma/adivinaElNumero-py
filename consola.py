def menu_principal() -> None:
    print('\n1) Adivina el numero de la computadora.')
    print('2) La computadora adivina tu numero.')
    print('3) Salir.')

def pedir_int(mensaje: str) -> int:
    numero = input(mensaje)

    if not numero.isdigit():
        raise ValueError
    
    return int(numero)