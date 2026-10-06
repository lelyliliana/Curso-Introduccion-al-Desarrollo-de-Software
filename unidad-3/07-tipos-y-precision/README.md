# Tipos de datos y precisión numérica

[Recurso anterior](../../unidad-3/06-entrada-y-validacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/08-operadores-y-precedencia/README.md)

## Objetivo

Distinguir int, float, str, bool y decisiones de precisión.

## Conceptos y explicación

Los tipos definen valores y operaciones. int representa enteros, float aproxima ciertos valores reales con precisión finita, str representa texto Unicode y bool representa dos valores lógicos. None señala ausencia de un valor en muchos contratos. No debe confundirse "False" con False: una cadena no vacía se considera verdadera en un contexto booleano.

Los enteros no tienen un límite fijo pequeño en Python, pero consumen memoria. Los float suelen usar representación binaria de doble precisión y no representan exactamente muchos decimales. La igualdad exacta entre resultados aproximados puede fallar. `math.isclose` compara con tolerancias; sus valores deben elegirse según escala y necesidad, no como fórmula universal.

Para dinero del ejercicio se pueden usar unidades enteras o Decimal construido desde texto. Para mediciones puede ser adecuado float con tolerancia y unidades documentadas. En texto, `len` cuenta puntos de código de Python y no necesariamente los símbolos visuales percibidos: una letra con marca combinada puede ocupar más de un punto de código.

## Caso resuelto paso a paso

El programa muestra que 0.1+0.2 no es exactamente 0.3 como float, pero es cercano bajo la tolerancia predeterminada de isclose. Decimal("0.1")+Decimal("0.2") produce 0.3 exactamente con la precisión suficiente para esta suma.

La salida bool("False") es True porque el texto no está vacío. Convertir texto a booleano exige una regla explícita como comparar contra "sí", no llamar bool sin analizarlo.

## Código completo

Archivo: [main.py](main.py).

```python
from decimal import Decimal
from math import isclose
print(0.1 + 0.2 == 0.3)
print(isclose(0.1 + 0.2, 0.3))
print(Decimal("0.1") + Decimal("0.2"))
print(bool("False"), bool(""))
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
False
True
0.3
True False
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Predice cada línea. Ejecuta. Explica la diferencia entre igualdad y cercanía. Cambia texto vacío y no vacío. Documenta unidades y tolerancia de una medición.

## Errores que conviene detectar

- Comparar resultados float como si todos los decimales fueran exactos.
- Convertir "False" con bool y esperar False.

## Ejercicio para resolver

Para tres precios 0.10, 0.20 y 0.30, calcula suma con Decimal y con unidades de centavos. Explica la conversión a presentación.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Decimal desde textos suma Decimal("0.60"). En centavos: 10+20+30=60; presentar 60/100 con formato puede servir para estas cantidades pequeñas, pero para evitar float en general divide y toma residuo de 100 al construir el texto.

</details>

## Preguntas de comprensión

¿Por qué float no representa todos los reales? ¿"False" es falso? ¿Una tolerancia adecuada depende del problema?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/06-entrada-y-validacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/08-operadores-y-precedencia/README.md)
