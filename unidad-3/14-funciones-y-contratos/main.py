def costo(cantidad, precio):
    """Devuelve costo entero; rechaza tipos incorrectos y valores negativos."""
    if type(cantidad) is not int or type(precio) is not int or cantidad < 0 or precio < 0:
        raise ValueError("Enteros no negativos requeridos")
    return cantidad * precio

if __name__ == "__main__":
    resultado = costo(3, 12000)
    print(resultado)
    print(costo(precio=12000, cantidad=3))
