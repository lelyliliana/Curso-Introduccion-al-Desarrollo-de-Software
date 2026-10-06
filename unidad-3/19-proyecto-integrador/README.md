# Proyecto integrador: inventario local de kits

[Recurso anterior](../../unidad-3/18-diccionarios-y-registros/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../docs/cierre.md)

## Objetivo

Integrar requisitos, funciones, colecciones, persistencia y pruebas.

## Conceptos y explicación

El proyecto implementa el caso definido en la unidad 1. Permite alta de kits, consulta por código, actualización de cantidad, listado y guardado/carga en un archivo JSON UTF-8. Todos los datos de práctica son ficticios. El código conserva reglas de unicidad, textos no vacíos y cantidades enteras no negativas.

La estructura central es un diccionario: código → registro. Las reglas no leen teclado, lo que permite probarlas directamente. El menú reúne la interacción y presenta errores esperados. La consulta devuelve una copia del registro para evitar modificaciones indirectas. True se rechaza como cantidad aunque Python lo considere un subtipo de int.

La carga construye un candidato completo y solo lo retorna si todos los registros pasan validación. El menú sustituye el inventario después del éxito. Así un archivo con un registro inválido no deja una carga parcial en el estado activo. Se rechazan campos inesperados, versiones distintas, códigos duplicados y claves JSON repetidas. La escritura es directa: un fallo durante ella puede dejar el archivo incompleto, por lo que no equivale a una transacción ni a un respaldo automático.

El costo de alta y consulta por clave es O(1) promedio bajo el modelo habitual del diccionario, no una garantía para todos los casos. Listar y guardar ordenan códigos: O(n log n) comparaciones en el modelo de claves de tamaño acotado. La memoria del inventario, documento y candidato crece con n. La primera versión lee el archivo completo y no tiene límites de tamaño para archivos ajenos; se usa solamente con los archivos pequeños de práctica.

## Caso resuelto paso a paso

| Requisito | Función | Prueba pertinente |
|---|---|---|
| R1 Código único | alta | Duplicado preserva estado |
| R2 Cantidad válida | alta/actualizar | -1 y True se rechazan; 0 se acepta |
| R3 Consulta | consultar | Copia independiente y ausencia |
| R4 Persistencia | guardar/cargar | Ida y vuelta con acentos |
| R5 Carga consistente | desde_documento/cargar | Registro inválido no sustituye activos |
| R6 Actualización | actualizar | Código ausente y rango |

Demostración: K01/Sensores/4 y K02/Cables/8. La carpeta salida se crea en la carpeta desde la que ejecutas el programa. El formato incluye version=1 y una lista kits. No registra préstamos, no autentica personas y no sirve como sistema de producción.

## Código completo

Archivo: [main.py](main.py).

```python
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
```

## Ejecución

Abre una terminal en la carpeta de esta lección. Si aún no tienes Python, sigue la [guía de ambiente](../../docs/ambiente-y-herramientas.md).

Windows (PowerShell):

```powershell
python main.py
```

Ubuntu y macOS:

```bash
python3 main.py
```

### Salida esperada

```text
K01 | Sensores | 4
K02 | Cables | 8
Consulta K01: 4
Recuperados: 2
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

Para el menú usa `python main.py --menu` en Windows o `python3 main.py --menu` en Ubuntu/macOS. Opciones: 1 alta, 2 consulta, 3 actualización, 4 listado, 5 guardar, 6 cargar y 0 salir. Los cambios no guardados se pierden al cerrar. El guardado sustituye `salida/inventario.json`; conserva otra copia antes de experimentar con el formato.

## Práctica guiada

Ejecuta la demostración y examina salida/inventario.json. Ejecuta main.py --menu. Registra K03, consulta y actualiza a0. Guarda y reinicia: el menú empieza vacío; usa Cargar para recuperar. Haz una copia del JSON antes de editarlo. Introduce un registro negativo y comprueba que se informa error sin sustituir el estado activo. Ejecuta las pruebas del repositorio.

## Errores que conviene detectar

- Sustituir inventario durante la lectura antes de validar todo el documento.
- Confundir la escritura directa con una operación a prueba de interrupciones.

## Ejercicio para resolver

Añade eliminación por código. Define si eliminar un código ausente produce error o devuelve False. Implementa la regla fuera del menú, documenta y prueba ausencia, primer registro y último registro.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Una opción: eliminar devuelve bool; valida código, comprueba pertenencia, elimina y retorna True o retorna False si falta. El menú presenta el resultado. Prueba eliminar K01 conservando K02, repetir K01 y eliminar el último hasta inventario vacío. Guardar/cargar debe conservar el nuevo estado sin crear registros inexistentes.

</details>

## Preguntas de comprensión

¿Por qué cargar crea un candidato? ¿Qué protege una copia de consulta? ¿Qué limitación tiene la escritura directa? ¿Qué requisito necesita cambiar para introducir préstamos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/18-diccionarios-y-registros/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../docs/cierre.md)
