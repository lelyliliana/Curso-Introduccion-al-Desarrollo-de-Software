def buscar(matriz, objetivo):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == objetivo:
                return i, j
    return None

if __name__ == "__main__":
    total = 0
    for n in (4, -1, 0, 8):
        if n < 0:
            continue
        total += n
    print(total)
    print(buscar([[4, 0], [8, 2]], 8))
    print(buscar([[4, 0], [8, 2]], 9))
