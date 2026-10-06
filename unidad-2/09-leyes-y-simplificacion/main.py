from itertools import product
contador = 0
for a, b in product((False, True), repeat=2):
    original = ((not a) and b) or (a and b)
    assert original == b
    assert (not (a and b)) == ((not a) or (not b))
    contador += 1
print(f"Equivalencias verificadas en {contador} combinaciones")
