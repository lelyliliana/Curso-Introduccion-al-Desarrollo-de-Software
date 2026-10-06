from pathlib import Path
import json
import sys


def validar_texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} debe ser texto no vacío")
    valor = valor.strip()
    if any(ord(c) < 32 for c in valor):
        raise ValueError(f"{campo} no admite caracteres de control")
    return valor


def alta(inventario, codigo, nombre, unidades):
    codigo = validar_texto(codigo, "Código")
    nombre = validar_texto(nombre, "Nombre")
    if type(unidades) is not int or unidades < 0:
        raise ValueError("Unidades deben ser un entero no negativo")
    if codigo in inventario:
        raise ValueError("Código duplicado")
    inventario[codigo] = {"nombre": nombre, "unidades": unidades}


def consultar(inventario, codigo):
    codigo = validar_texto(codigo, "Código")
    registro = inventario.get(codigo)
    return None if registro is None else registro.copy()


def actualizar(inventario, codigo, unidades):
    codigo = validar_texto(codigo, "Código")
    if codigo not in inventario:
        raise ValueError("Código inexistente")
    if type(unidades) is not int or unidades < 0:
        raise ValueError("Unidades deben ser un entero no negativo")
    inventario[codigo]["unidades"] = unidades


def documento(inventario):
    return {"version": 1, "kits": [
        {"codigo": codigo, **registro} for codigo, registro in sorted(inventario.items())
    ]}


def guardar(inventario, ruta):
    ruta = Path(ruta)
    texto = json.dumps(documento(inventario), ensure_ascii=False, indent=2)
    # La carga de validación evita escribir una estructura fuera del contrato.
    desde_documento(json.loads(texto))
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto + "\n", encoding="utf-8")


def desde_documento(datos):
    if not isinstance(datos, dict) or set(datos) != {"version", "kits"}:
        raise ValueError("Estructura de documento inválida")
    if type(datos["version"]) is not int or datos["version"] != 1:
        raise ValueError("Versión no soportada")
    if not isinstance(datos["kits"], list):
        raise ValueError("Kits debe ser una lista")
    candidato = {}
    for numero, registro in enumerate(datos["kits"], start=1):
        if not isinstance(registro, dict) or set(registro) != {"codigo", "nombre", "unidades"}:
            raise ValueError(f"Registro {numero}: campos inválidos")
        try:
            alta(candidato, registro["codigo"], registro["nombre"], registro["unidades"])
        except ValueError as error:
            raise ValueError(f"Registro {numero}: {error}") from error
    return candidato


def pares_unicos(pares):
    resultado = {}
    for clave, valor in pares:
        if clave in resultado:
            raise ValueError(f"Clave JSON repetida: {clave}")
        resultado[clave] = valor
    return resultado


def cargar(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    datos = json.loads(texto, object_pairs_hook=pares_unicos)
    return desde_documento(datos)


def mostrar(inventario):
    if not inventario:
        print("Inventario vacío")
    for codigo, registro in sorted(inventario.items()):
        print(f"{codigo} | {registro['nombre']} | {registro['unidades']}")


def demostracion():
    inventario = {}
    alta(inventario, "K01", "Sensores", 4)
    alta(inventario, "K02", "Cables", 8)
    mostrar(inventario)
    print(f"Consulta K01: {consultar(inventario, 'K01')['unidades']}")
    guardar(inventario, Path("salida") / "inventario.json")
    recuperado = cargar(Path("salida") / "inventario.json")
    print(f"Recuperados: {len(recuperado)}")


def menu():
    inventario = {}
    ruta = Path("salida") / "inventario.json"
    while True:
        print("1 Alta | 2 Consultar | 3 Actualizar | 4 Listar | 5 Guardar | 6 Cargar | 0 Salir")
        try:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                print("Fin")
                return
            elif opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                unidades = int(input("Unidades: "))
                alta(inventario, codigo, nombre, unidades)
                print("Kit registrado")
            elif opcion == "2":
                registro = consultar(inventario, input("Código: "))
                print("No existe" if registro is None else f"{registro['nombre']}: {registro['unidades']}")
            elif opcion == "3":
                codigo = input("Código: ")
                unidades = int(input("Unidades: "))
                actualizar(inventario, codigo, unidades)
                print("Cantidad actualizada")
            elif opcion == "4":
                mostrar(inventario)
            elif opcion == "5":
                guardar(inventario, ruta)
                print("Inventario guardado")
            elif opcion == "6":
                candidato = cargar(ruta)
                inventario = candidato
                print("Inventario cargado")
            else:
                print("Opción inválida")
        except (ValueError, OSError, UnicodeError) as error:
            print(f"Error: {error}")
        except EOFError:
            print("Fin de entrada")
            return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        demostracion()
    elif sys.argv[1:] == ["--menu"]:
        menu()
    else:
        raise SystemExit("Uso: main.py [--menu]")
