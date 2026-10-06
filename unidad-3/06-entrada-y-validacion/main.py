def cantidad_desde_texto(texto):
    try:
        cantidad = int(texto)
    except ValueError as error:
        raise ValueError("Escribe un entero") from error
    if not 0 <= cantidad <= 10:
        raise ValueError("Cantidad de 0 a 10")
    return cantidad

if __name__ == "__main__":
    try:
        cantidad = cantidad_desde_texto(input("Cantidad: "))
        print(f"Registradas: {cantidad}")
    except ValueError as error:
        print(f"Error: {error}")
