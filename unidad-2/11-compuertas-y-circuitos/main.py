from itertools import product
print("A B C S")
for a, b in product((0, 1), repeat=2):
    suma = a ^ b
    transporte = a & b
    assert a + b == 2 * transporte + suma
    print(a, b, transporte, suma)
