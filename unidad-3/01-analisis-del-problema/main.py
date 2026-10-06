def costo(cantidad, precio):
    if type(cantidad) is not int or type(precio) is not int:
        raise ValueError("Cantidad y precio deben ser enteros")
    if cantidad < 0 or precio < 0:
        raise ValueError("No se aceptan valores negativos")
    return cantidad * precio

if __name__ == "__main__":
    print(costo(3, 12000))
    print(costo(0, 12000))
