# Condicionales anidados y claridad

[Recurso anterior](../../unidad-3/09-condicionales/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/11-while-y-terminacion/README.md)

## Objetivo

Separar condiciones dependientes y evitar anidación innecesaria.

## Conceptos y explicación

Una condición anidada se evalúa dentro de otra rama. Es útil cuando la segunda pregunta solo tiene sentido después de la primera. Para prestar un kit primero importa que el código exista y después su cantidad. Consultar directamente un código ausente puede producir un error de acceso.

No se anida por costumbre. Las cláusulas de salida temprana pueden expresar validaciones y reducir profundidad. Dos estilos pueden ser equivalentes si conservan el orden y la regla. La legibilidad se juzga por la facilidad de verificar casos, no solo por tener menos líneas.

La ausencia de un código y una cantidad cero son situaciones diferentes. Una función que devuelve 0 para ambos pierde información. El ejemplo usa pertenencia al diccionario para distinguir existencia antes de consultar el valor. El diccionario se estudia formalmente más adelante; aquí representa la tabla de códigos del caso.

## Caso resuelto paso a paso

K01 tiene 4 unidades, K02 tiene 0, K99 no existe.

| Código | Existe | Unidades positivas | Mensaje |
|---|---|---|---|
| K01 | Sí | Sí | Se puede prestar |
| K02 | Sí | No | Agotado |
| K99 | No | No se consulta | No existe |

No se modifica el inventario; este ejemplo decide si una solicitud sería admisible.

## Código completo

Archivo: [main.py](main.py).

```python
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
K01: Se puede prestar
K02: Agotado
K99: No existe
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Evalúa existencia. Si existe, evalúa stock. Traza las tres rutas. Ejecuta. Reescribe con return temprano y compara resultados sin cambiar la regla.

## Errores que conviene detectar

- Consultar una clave antes de comprobar existencia.
- Representar clave ausente y cantidad cero con el mismo resultado sin aclaración.

## Ejercicio para resolver

Agrega una cantidad solicitada. Debe ser entero positivo y no superar disponibilidad. Identifica el orden de validaciones.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Primero formato y dominio de cantidad, luego existencia, después cantidad<=stock. Rechazar no modifica datos. Con K01: pedir 4 se permite,5 se rechaza; K02 pedir1 se rechaza; K99 informa ausencia.

</details>

## Preguntas de comprensión

¿Qué evita preguntar existencia primero? ¿Por qué cero no significa ausencia? ¿Qué cambia al usar salidas tempranas?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/09-condicionales/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/11-while-y-terminacion/README.md)
