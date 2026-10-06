# Diccionarios, claves y registros

[Recurso anterior](../../unidad-3/17-listas-y-recorridos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/19-proyecto-integrador/README.md)

## Objetivo

Organizar datos por clave sin perder unicidad ni independencia.

## Conceptos y explicación

Un diccionario relaciona claves hashables con valores. Cada clave aparece una sola vez. Asignar una clave existente reemplaza el valor; si la regla exige rechazar duplicados se debe comprobar antes. Los diccionarios preservan orden de inserción en Python moderno, pero ese orden no significa que estén ordenados alfabéticamente.

Un registro puede representarse como diccionario con campos acordados. Aquí cada código apunta a nombre y unidades. La clave de búsqueda y el campo de un registro cumplen papeles diferentes. La función de alta valida datos y no sobreescribe silenciosamente un código existente.

Una copia del diccionario exterior sigue compartiendo registros mutables interiores. Para una captura independiente de esta estructura se copia cada registro interior, pues sus campos son texto y enteros inmutables. Estructuras más profundas necesitan revisar los niveles o usar una copia profunda apropiada. Ninguna copia reemplaza la validación de reglas.

## Caso resuelto paso a paso

Inventario: K01 → {nombre:Sensores,unidades:4}. El segundo alta de K01 se rechaza. K02 se añade sin afectar K01. La captura copia campos y modificarla no cambia unidades en el inventario.

| Operación | Riesgo sin regla |
|---|---|
| Alta | Reemplazar duplicado |
| Consulta | KeyError si no existe |
| Copia exterior | Compartir registros |
| Actualización | Aceptar negativo |

## Código completo

Archivo: [main.py](main.py).

```python
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
{'nombre': 'Sensores', 'unidades': 4}
['K01', 'K02']
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Identifica clave y campos. Ejecuta alta. Intenta duplicado. Construye captura independiente. Modifica captura y comprueba original. Distingue sorted(claves) del orden de inserción.

## Errores que conviene detectar

- Sobreponer una clave duplicada cuando la regla exige rechazarla.
- Copiar solo el diccionario exterior y exponer registros interiores mutables.

## Ejercicio para resolver

Implementa consulta que devuelva una copia del registro o None, sin permitir modificar el inventario indirectamente.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

registro=inventario.get(codigo); return None if registro is None else registro.copy(). Con campos inmutables basta esa copia. Prueba ausente y modifica el resultado de una consulta presente para confirmar independencia.

</details>

## Preguntas de comprensión

¿Asignar clave existente lanza error automáticamente? ¿Qué comparte copy exterior? ¿Orden de inserción es orden alfabético?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/17-listas-y-recorridos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/19-proyecto-integrador/README.md)
