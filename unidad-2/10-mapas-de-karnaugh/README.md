# Mapas de Karnaugh de dos y tres variables

[Recurso anterior](../../unidad-2/09-leyes-y-simplificacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/11-compuertas-y-circuitos/README.md)

## Objetivo

Agrupar minterminos adyacentes y comprobar una simplificación.

## Conceptos y explicación

Un mapa de Karnaugh reorganiza la tabla de verdad de modo que celdas adyacentes difieran en una sola variable. El orden Gray 00,01,11,10 para dos variables de columna evita que dos bits cambien entre columnas contiguas. Con tres variables hay ocho celdas, no cuatro.

Para una forma suma de productos se agrupan unos en rectángulos de tamaño 1,2,4 u 8; los grupos pueden superponerse y los bordes se consideran adyacentes. No se agrupan diagonales. En cada grupo se conservan variables que permanecen constantes y se eliminan las que cambian. Se deben cubrir todos los unos sin incluir ceros. Las condiciones indiferentes requieren una justificación del problema; aquí no se usan.

Un grupo de cuatro que ocupa todas las columnas de una fila elimina las dos variables de columna. La simplificación debe comprobarse después contra la tabla original. El mapa es una técnica para pocas variables, no una demostración automática de cualquier expresión escrita junto a él.

## Caso resuelto paso a paso

F(A,B,C) = A′BC′ + A′BC + ABC′ + ABC.

| AB \ C | 0 | 1 |
|---|---|---|
| 00 | 0 | 0 |
| 01 | 1 | 1 |
| 11 | 1 | 1 |
| 10 | 0 | 0 |

Las cuatro celdas centrales forman un rectángulo. A y C cambian; B se conserva en 1. Resultado: F=B. Las filas AB usan orden Gray. El programa confirma las ocho combinaciones.

## Código completo

Archivo: [main.py](main.py).

```python
from itertools import product
for a, b, c in product((False, True), repeat=3):
    f = ((not a) and b and (not c)) or ((not a) and b and c) or (a and b and (not c)) or (a and b and c)
    assert f == b
print("Mapa comprobado: 8 combinaciones, F = B")
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
Mapa comprobado: 8 combinaciones, F = B
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Construye primero la tabla. Coloca entradas en orden Gray. Marca unos. Agrupa rectángulos permitidos. Conserva variables constantes. Verifica las ocho filas con la expresión reducida.

## Errores que conviene detectar

- Usar orden binario en vez de Gray en filas o columnas.
- Agrupar diagonales o rectángulos que contienen ceros.

## Ejercicio para resolver

Simplifica F=A′B′C + A′BC + AB′C + ABC con un mapa de tres variables.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Todos los términos tienen C=1 y cubren todas las combinaciones de A y B. Se agrupa la columna C=1 de cuatro celdas y resulta F=C. Una tabla de ocho filas confirma la equivalencia.

</details>

## Preguntas de comprensión

¿Por qué 00,01,10,11 no sirve como orden lineal de columnas? ¿Qué cambia al cruzar un borde? ¿Por qué una diagonal no forma grupo?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/09-leyes-y-simplificacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/11-compuertas-y-circuitos/README.md)
