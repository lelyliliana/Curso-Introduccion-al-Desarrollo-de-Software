def a_binario(numero):
    if type(numero) is not int or numero < 0:
        raise ValueError("Se requiere un entero no negativo")
    if numero == 0:
        return "0"
    residuos = []
    while numero > 0:
        numero, residuo = divmod(numero, 2)
        residuos.append(str(residuo))
    return "".join(reversed(residuos))

if __name__ == "__main__":
    for n in (0, 13, 64):
        print(f"{n} -> {a_binario(n)}")
