def sumar_hasta(n):
    if type(n) is not int or n < 0:
        raise ValueError("Entero no negativo requerido")
    i = total = 0
    while i < n:
        i += 1
        total += i
    return total

if __name__ == "__main__":
    for n in (0, 3, 5):
        print(f"{n}: {sumar_hasta(n)}")
