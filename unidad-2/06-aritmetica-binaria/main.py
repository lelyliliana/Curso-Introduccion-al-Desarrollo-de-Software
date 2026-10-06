a, b = 0b1011, 0b0110
print(f"suma: {a+b:b}")
print(f"resta: {a-b:b}")
print(f"producto: {a*b:b}")
q, r = divmod(a, 0b11)
print(f"cociente: {q:b}; residuo: {r:b}")
