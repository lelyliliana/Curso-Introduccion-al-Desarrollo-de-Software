# Leyes booleanas y simplificación

[Recurso anterior](../../unidad-2/08-logica-y-tablas/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/10-mapas-de-karnaugh/README.md)

## Objetivo

Simplificar expresiones y comprobar equivalencia exhaustiva.

## Conceptos y explicación

Las leyes permiten transformar una expresión sin cambiar su tabla. Identidad: A+0=A y A·1=A. Dominación: A+1=1 y A·0=0. Idempotencia: A+A=A y A·A=A. Complemento: A+A′=1 y A·A′=0. Absorción: A+AB=A. Se aplican en el dominio booleano, no como reglas de números ordinarios.

De Morgan: (AB)′=A′+B′ y (A+B)′=A′B′. Negar «ambas» significa «al menos una no»; negar «alguna» significa «ninguna». Al mover la negación cambia el operador. Los paréntesis evitan depender de una precedencia recordada incorrectamente.

Una equivalencia requiere que ambas expresiones coincidan para todas las entradas pertinentes. Con pocas variables puede comprobarse enumerando la tabla. La simplificación reduce términos y puede facilitar comprensión, pero en software también importan legibilidad y efectos secundarios. No se transforman expresiones con llamadas que modifican estado como si fueran variables matemáticas sin analizar su evaluación.

## Caso resuelto paso a paso

F = A′B + AB = (A′+A)B = 1·B = B. La tabla debe confirmar el resultado. Otra ley: NOT(A AND B) = NOT A OR NOT B.

El programa evalúa cuatro combinaciones para ambas igualdades. Cuenta verificaciones y falla con AssertionError si una igualdad deja de cumplirse.

## Código completo

Archivo: [main.py](main.py).

```python
from itertools import product
contador = 0
for a, b in product((False, True), repeat=2):
    original = ((not a) and b) or (a and b)
    assert original == b
    assert (not (a and b)) == ((not a) or (not b))
    contador += 1
print(f"Equivalencias verificadas en {contador} combinaciones")
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
Equivalencias verificadas en 4 combinaciones
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Escribe una ley por paso. Factoriza B. Usa complemento. Compara tablas. Introduce temporalmente un operador equivocado y observa qué combinación lo detecta.

## Errores que conviene detectar

- Negar ambas variables sin cambiar el operador al aplicar De Morgan.
- Considerar probada una equivalencia con una sola fila.

## Ejercicio para resolver

Simplifica A + A′B y demuestra con cuatro filas. Aplica De Morgan a NOT(A OR B).

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

A + A′B = (A+A′)(A+B) = A+B. La negación de OR es (NOT A) AND (NOT B). Para la primera igualdad las salidas son 0,1,1,1 en orden 00,01,10,11.

</details>

## Preguntas de comprensión

¿Coincidir en una fila prueba equivalencia? ¿Por qué cambia AND por OR al negar? ¿Qué problema generan efectos secundarios?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/08-logica-y-tablas/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/10-mapas-de-karnaugh/README.md)
