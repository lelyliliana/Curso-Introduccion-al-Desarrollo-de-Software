# Álgebra booleana y tablas de verdad

[Recurso anterior](../../unidad-2/07-bits-signo-y-limites/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/09-leyes-y-simplificacion/README.md)

## Objetivo

Evaluar AND, OR, NOT y XOR para todas las entradas.

## Conceptos y explicación

El álgebra booleana trabaja con dos valores, aquí falso/verdadero o 0/1. AND requiere ambas entradas verdaderas; OR requiere al menos una; NOT invierte un valor; XOR requiere entradas diferentes. El OR habitual es inclusivo: también es verdadero cuando ambas entradas lo son.

En expresiones de álgebra booleana se suele escribir AB para AND, A+B para OR y A′ para NOT. Esa notación no es aritmética ordinaria: en OR, 1+1 = 1. En Python se usan `and`, `or`, `not` y una comparación de desigualdad para XOR de booleanos. `^` es XOR bit a bit; no es potencia. `and` y `or` pueden devolver operandos cuando estos no son booleanos, por lo que aquí las entradas se fijan en bool.

Con n entradas binarias una tabla tiene 2ⁿ combinaciones. La tabla de verdad permite comprobar una regla exhaustivamente dentro de ese dominio. Eso no verifica fallos físicos, entradas desconocidas ni reglas omitidas del problema real.

## Caso resuelto paso a paso

Regla de permiso: credencial válida AND equipo disponible. Regla de alerta: temperatura alta OR humo. La segunda debe activarse aunque se presenten ambas condiciones.

El programa enumera 00, 01, 10 y 11. Convertir bool a int imprime 0 o 1. XOR y OR difieren solo en la combinación 11 para dos entradas.

## Código completo

Archivo: [main.py](main.py).

```python
from itertools import product
print("A B AND OR XOR NOT_A")
for a, b in product((False, True), repeat=2):
    valores = (a, b, a and b, a or b, a != b, not a)
    print(" ".join(str(int(v)) for v in valores))
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
A B AND OR XOR NOT_A
0 0 0 0 0 1
0 1 0 1 1 1
1 0 0 1 1 0
1 1 1 1 0 0
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Escribe combinaciones sin omitir ninguna. Evalúa cada operador por separado. Predice la fila 11. Ejecuta. Traduce una regla verbal y comprueba si necesita OR inclusivo o XOR.

## Errores que conviene detectar

- Usar XOR cuando la regla admite ambas entradas verdaderas.
- Interpretar + booleano como suma aritmética ordinaria.

## Ejercicio para resolver

Un usuario accede si tiene clave válida o token válido. Decide entre OR y XOR y elabora su tabla.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Se usa OR si cualquiera basta y presentar ambos también es válido. Tabla 00→0,01→1,10→1,11→1. XOR rechazaría 11 y solo corresponde si la regla exige exactamente uno.

</details>

## Preguntas de comprensión

¿Cuántas filas hay con tres entradas? ¿Por qué el símbolo + no es suma común? ¿Qué fila distingue OR de XOR?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/07-bits-signo-y-limites/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/09-leyes-y-simplificacion/README.md)
