def complemento(numero, bits):
    if type(bits) is not int or bits <= 0:
        raise ValueError("Ancho positivo requerido")
    if type(numero) is not int or not -(2**(bits-1)) <= numero < 2**(bits-1):
        raise ValueError("Fuera de rango")
    patron = numero if numero >= 0 else 2**bits + numero
    return format(patron, f"0{bits}b")

if __name__ == "__main__":
    for n in (-128, -5, -1, 0, 127):
        print(f"{n}: {complemento(n, 8)}")
