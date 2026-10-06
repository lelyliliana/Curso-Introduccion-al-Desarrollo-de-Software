# Ciclo for, range y acumulación

[Recurso anterior](../../unidad-3/11-while-y-terminacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/13-break-continue-y-anidacion/README.md)

## Objetivo

Recorrer secuencias e intervalos sin errores de límite.

## Conceptos y explicación

for recorre elementos de un iterable. No es únicamente un contador numérico. Puede recorrer una lista de cantidades, un texto o un range. El nombre de iteración se asocia a cada elemento; no debes modificarlo para intentar cambiar el próximo elemento producido por range.

range(inicio,fin,paso) excluye fin. range(1,6) produce 1,2,3,4,5. El paso no puede ser cero y puede ser negativo. Un range no materializa todos sus números como una lista, aunque se pueda convertir para inspección. Para recorrer elementos basta for elemento in datos; para conocer posición y elemento puede usarse enumerate.

El acumulador suma cantidades válidas. Si hay posibilidad de una colección vacía, debe decidirse qué significan total y promedio. La suma vacía puede ser 0; el promedio necesita tratamiento especial porque no se puede dividir entre cero.

## Caso resuelto paso a paso

Cantidades [4,0,8] generan totales parciales 4,4,12. enumerate con start=1 produce una numeración de presentación 1,2,3; los índices internos de la lista siguen comenzando en cero.

La función sum ofrece otra manera de comprobar la acumulación. Aquí se usa el ciclo para comprender cada paso antes de abreviar.

## Código completo

Archivo: [main.py](main.py).

```python
cantidades = [4, 0, 8]
total = 0
for posicion, cantidad in enumerate(cantidades, start=1):
    total += cantidad
    print(f"Paso {posicion}: {total}")
print(list(range(5, 0, -1)))
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
Paso 1: 4
Paso 2: 4
Paso 3: 12
[5, 4, 3, 2, 1]
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Predice totales parciales. Ejecuta. Cambia a lista vacía. Compara con sum. Inspecciona range(5,0,-1) y explica su final excluido.

## Errores que conviene detectar

- Incluir el extremo final de range por error.
- Dividir por len(datos) cuando datos está vacío.

## Ejercicio para resolver

Calcula promedio de [4,0,8] y decide qué devolver para lista vacía.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

El promedio es 12/3=4.0. Puede devolverse None si no hay datos o lanzar ValueError, pero debe documentarse la elección. No devuelvas 0 sin explicar, pues confunde ausencia con un promedio real de cero.

</details>

## Preguntas de comprensión

¿fin se incluye en range? ¿enumerate cambia índices de la colección? ¿Qué diferencia hay entre suma y promedio vacío?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/11-while-y-terminacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/13-break-continue-y-anidacion/README.md)
