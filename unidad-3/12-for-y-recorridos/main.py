cantidades = [4, 0, 8]
total = 0
for posicion, cantidad in enumerate(cantidades, start=1):
    total += cantidad
    print(f"Paso {posicion}: {total}")
print(list(range(5, 0, -1)))
