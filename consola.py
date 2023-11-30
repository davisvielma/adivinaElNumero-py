def menu_principal() -> None:
    print('\n1) Usuario adivina el numero.')
    print('2) Computadora adivina el numero.')
    print('3) Salir.')

def pedir_int(mensaje: str) -> int:
    numero = input(mensaje)

    if not numero.isdigit():
        raise ValueError
    
    return int(numero)