def repartir(kits, mesas):
    if type(kits) is not int or type(mesas) is not int or kits < 0 or mesas <= 0:
        raise ValueError("Kits no negativos y mesas positivas, ambos enteros")
    return divmod(kits, mesas)

if __name__ == "__main__":
    por_mesa, sobran = repartir(17, 5)
    print(f"Por mesa: {por_mesa}; sobran: {sobran}")
