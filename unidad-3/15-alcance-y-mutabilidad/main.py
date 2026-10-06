def aumentar_local(numero):
    numero += 1
    return numero

def agregar(datos):
    datos.append(8)

if __name__ == "__main__":
    numero = 4
    print(aumentar_local(numero), numero)
    datos = [4]
    agregar(datos)
    copia = datos.copy()
    copia.append(2)
    print(datos)
    print(copia)
