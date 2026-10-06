# Operaciones básicas en distintas bases

[Recurso anterior](../../unidad-2/05-hexadecimal/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/07-bits-signo-y-limites/README.md)

## Objetivo

Realizar suma, resta, multiplicación y división binaria.

## Conceptos y explicación

Las operaciones representan las mismas relaciones entre cantidades en cualquier base. Cambian los dígitos y las reglas para transportar o prestar una unidad. En base 2, 1+1 = 10₂: se escribe 0 y se transporta 1. Con un transporte adicional, 1+1+1 = 11₂.

Para restar, cuando 0 necesita restar 1 se toma una unidad de la posición siguiente, equivalente a dos unidades de la actual. La multiplicación por 10₂ desplaza un lugar y equivale a multiplicar por 2. Una multiplicación de varios bits suma productos parciales. La división entera produce cociente y residuo: a = b×q + r.

No confundas la operación matemática con límites de hardware. Python usa enteros de precisión arbitraria sujetos a memoria; un registro de ocho bits no. El programa calcula valores enteros y los presenta en binario. No implementa un circuito bit a bit, pero permite verificar los cálculos manuales.

## Caso resuelto paso a paso

1011₂ + 0110₂ = 10001₂ (11 + 6 = 17). La resta es 1011₂−0110₂ = 0101₂. El producto es 1000010₂ (66). División: 1011₂ entre 11₂ produce cociente 11₂ y residuo 10₂, porque 11 = 3×3 + 2.

Comprueba cada operación primero en binario y luego convirtiendo sus operandos a decimal. Dos procedimientos independientes ayudan a encontrar errores de transporte.

### Transportes en octal y hexadecimal

En octal,7+1=10₈: se transporta al llegar a8. Por eso65₈+13₈=100₈. Columna de unidades:5+3=8₁₀, se escribe0 y se transporta1; siguiente columna:6+1+1=8₁₀, se repite el transporte. Comprobación:53+11=64₁₀.

En hexadecimal,2A₁₆+17₁₆=41₁₆. Unidades:A+7=17₁₀=11₁₆, se escribe1 y se transporta1; siguiente columna:2+1+1=4. Comprobación:42+23=65₁₀. Los transportes siguen la base, no siempre el umbral decimal10.

## Código completo

Archivo: [main.py](main.py).

```python
a, b = 0b1011, 0b0110
print(f"suma: {a+b:b}")
print(f"resta: {a-b:b}")
print(f"producto: {a*b:b}")
q, r = divmod(a, 0b11)
print(f"cociente: {q:b}; residuo: {r:b}")
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
suma: 10001
resta: 101
producto: 1000010
cociente: 11; residuo: 10
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Realiza la suma por columnas. Anota cada transporte. Haz la resta con préstamos. Multiplica con productos parciales. Verifica división con divisor×cociente+residuo.

## Errores que conviene detectar

- Olvidar el transporte de 1+1 al sumar en binario.
- Dar el cociente como resultado completo cuando se pide también el residuo.

## Ejercicio para resolver

Calcula 111₂+1₂, 1000₂−1₂ y 101₂×11₂. Indica qué sucede si solo se guardan tres bits del primer resultado.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Resultados: 1000₂, 111₂ y 1111₂. Tres bits no bastan para 1000₂; truncar produciría 000 y perdería información. En Python el entero no se trunca automáticamente.

</details>

## Preguntas de comprensión

¿El transporte es parte del resultado final? ¿Por qué dividir necesita considerar el residuo? ¿Qué diferencia hay entre entero Python y registro de bits?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/05-hexadecimal/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/07-bits-signo-y-limites/README.md)
