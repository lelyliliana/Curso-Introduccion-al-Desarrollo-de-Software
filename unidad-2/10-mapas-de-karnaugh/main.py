from itertools import product
for a, b, c in product((False, True), repeat=3):
    f = ((not a) and b and (not c)) or ((not a) and b and c) or (a and b and (not c)) or (a and b and c)
    assert f == b
print("Mapa comprobado: 8 combinaciones, F = B")
