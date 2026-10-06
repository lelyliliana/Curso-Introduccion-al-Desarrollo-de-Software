def total(monto):
    if type(monto) is not int or monto < 0:
        raise ValueError("Monto entero no negativo requerido")
    if monto >= 100000:
        if monto % 10 != 0:
            raise ValueError("Para este ejemplo, el monto con descuento debe ser múltiplo de diez")
        return monto - monto // 10
    return monto

if __name__ == "__main__":
    for monto in (99999, 100000, 100010):
        print(f"{monto} -> {total(monto)}")
