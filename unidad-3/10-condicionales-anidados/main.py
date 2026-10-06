inventario = {"K01": 4, "K02": 0}
def permiso(codigo):
    if codigo in inventario:
        if inventario[codigo] > 0:
            return "Se puede prestar"
        else:
            return "Agotado"
    else:
        return "No existe"

if __name__ == "__main__":
    for codigo in ("K01", "K02", "K99"):
        print(f"{codigo}: {permiso(codigo)}")
