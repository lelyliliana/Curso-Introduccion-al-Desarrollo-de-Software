from itertools import product
print("A B AND OR XOR NOT_A")
for a, b in product((False, True), repeat=2):
    valores = (a, b, a and b, a or b, a != b, not a)
    print(" ".join(str(int(v)) for v in valores))
