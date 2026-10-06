def alta(inventario, codigo, nombre, unidades):
    if not isinstance(codigo, str) or not codigo.strip() or not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("Código y nombre no vacíos")
    codigo, nombre = codigo.strip(), nombre.strip()
    if type(unidades) is not int or unidades < 0:
        raise ValueError("Unidades enteras no negativas")
    if codigo in inventario:
        raise ValueError("Código duplicado")
    inventario[codigo] = {"nombre": nombre, "unidades": unidades}

if __name__ == "__main__":
    inventario = {}
    alta(inventario, "K01", "Sensores", 4)
    alta(inventario, "K02", "Cables", 8)
    captura = {c: registro.copy() for c, registro in inventario.items()}
    captura["K01"]["unidades"] = 0
    print(inventario["K01"])
    print(sorted(inventario))
