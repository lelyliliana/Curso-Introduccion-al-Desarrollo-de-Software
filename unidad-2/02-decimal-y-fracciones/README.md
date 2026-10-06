# Sistema decimal y posiciones fraccionarias

[Recurso anterior](../../unidad-2/01-valor-posicional/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/03-binario-y-conversion/README.md)

## Objetivo

Explicar pesos negativos y conversiones de fracciones exactas.

## Conceptos y explicación

A la derecha del separador, los pesos son b⁻¹, b⁻² y sucesivos. En decimal 56.1 = 5×10 + 6 + 1/10. En binario 10011.01 = 16 + 2 + 1 + 1/4 = 19.25. El punto empleado en código Python es un separador de representación; en textos cotidianos puede usarse coma decimal según la convención.

Una fracción tiene expansión finita en una base cuando, una vez reducida, los factores primos de su denominador están entre los factores de esa base. 1/4 termina en base 2; 1/10 no, porque su denominador reducido contiene 5. Esto explica por qué algunas fracciones decimales no se almacenan exactamente en un float binario.

`Fraction` representa racionales exactamente como numerador y denominador. `Decimal` permite aritmética decimal con una precisión y reglas de redondeo. Ninguno sustituye decidir qué precisión necesita el problema. Usar `Fraction(1, 10)` evita introducir primero la aproximación de un float.

## Caso resuelto paso a paso

10011.01₂ se separa en parte entera y fraccionaria. Los bits fraccionarios tienen peso 1/2 y 1/4. Aquí el primero vale 0 y el segundo 1; por eso el total es 19 + 0 + 1/4. El programa usa Fraction para conservar esa exactitud.

| Representación | Expansión | Valor |
|---|---|---|
| 0.1₂ | 1/2 | 0.5₁₀ |
| 0.01₂ | 1/4 | 0.25₁₀ |
| 0.11₂ | 1/2 + 1/4 | 0.75₁₀ |

### Conversión fraccionaria por multiplicaciones

Para convertir 0.625₁₀ a binario, multiplica la fracción por2. La parte entera de cada producto es el siguiente bit; continúa con la fracción restante.

| Fracción | Producto por2 | Bit | Nueva fracción |
|---|---|---|---|
| 0.625 | 1.25 | 1 | 0.25 |
| 0.25 | 0.5 | 0 | 0.5 |
| 0.5 | 1.0 | 1 | 0 |

La lectura conserva el orden de aparición:0.101₂. No se invierte como en las divisiones de la parte entera. Comprueba1/2+1/8=0.625. Para0.1₁₀ la fracción no llega a cero: debes declarar un límite de bits y una política de aproximación si necesitas terminar el procedimiento.

## Código completo

Archivo: [main.py](main.py).

```python
from fractions import Fraction
valor = 1 * 2**4 + 1 * 2**1 + 1 + Fraction(1, 4)
print(valor)
print(float(valor))
print(Fraction(1, 2) + Fraction(1, 4))
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
77/4
19.25
3/4
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Separa parte entera y fracción. Asigna pesos desde el separador. Suma términos. Comprueba con Fraction. Distingue el racional exacto de una impresión decimal aproximada.

## Errores que conviene detectar

- Asignar peso 2¹ al primer bit fraccionario en vez de 2⁻¹.
- Confundir impresión redondeada con valor almacenado exacto.

## Ejercicio para resolver

Convierte 101.101₂ a decimal y justifica si 0.2₁₀ tiene expansión binaria finita.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

101.101₂ = 5 + 1/2 + 1/8 = 5.625. 0.2₁₀ = 1/5 no tiene expansión binaria finita porque 5 no divide ninguna potencia de 2.

</details>

## Preguntas de comprensión

¿Por qué aparece un exponente negativo? ¿Imprimir dos decimales hace exacto un float? ¿Qué ventaja tiene construir Fraction con enteros?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/01-valor-posicional/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/03-binario-y-conversion/README.md)
