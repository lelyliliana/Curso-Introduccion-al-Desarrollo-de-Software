def estado(unidades):
    if type(unidades) is not int or unidades < 0:
        raise ValueError("Unidades enteras no negativas")
    if unidades == 0:
        return "agotado"
    elif unidades <= 2:
        return "bajo"
    else:
        return "disponible"

if __name__ == "__main__":
    for n in (0, 1, 2, 3):
        print(f"{n}: {estado(n)}")
