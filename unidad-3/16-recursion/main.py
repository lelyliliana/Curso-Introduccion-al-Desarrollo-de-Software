def factorial(n):
    if type(n) is not int or not 0 <= n <= 100:
        raise ValueError("Entero de 0 a 100 requerido")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    for n in (0, 3, 5):
        print(f"{n}! = {factorial(n)}")
