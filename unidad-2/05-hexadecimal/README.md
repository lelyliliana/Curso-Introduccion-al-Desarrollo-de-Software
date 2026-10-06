# Sistema hexadecimal y agrupación de bits

[Recurso anterior](../../unidad-2/04-octal/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/06-aritmetica-binaria/README.md)

## Objetivo

Usar hexadecimal como representación compacta de bits.

## Conceptos y explicación

Como 16 = 2⁴, cada dígito hexadecimal representa cuatro bits. Los valores 10 a 15 se escriben A, B, C, D, E y F. No son letras arbitrarias: 2A₁₆ = 2×16 + 10 = 42₁₀. Python acepta mayúsculas o minúsculas al interpretar texto hexadecimal.

Un byte de ocho bits se representa con dos dígitos hexadecimales, de 00 a FF, cuando se usa ancho fijo. La representación hexadecimal no cambia los datos: ofrece una forma más corta de inspeccionarlos. El contexto determina si un patrón es cantidad, código de carácter, dirección u otro dato.

`format(n, '02X')` da mayúsculas y al menos dos posiciones, pero no impone un límite de byte. Para restringir a 0..255 se necesita validación. Usar un formato con ancho no recorta automáticamente un entero grande ni demuestra que quepa en la memoria asignada.

## Caso resuelto paso a paso

171₁₀ = 10101011₂ = AB₁₆. Agrupación: 1010 → A y 1011 → B. Para 5 se imprime 05; el cero indica ancho y no cambia el valor.

| Hexadecimal | Decimal | Binario de 4 bits |
|---|---|---|
| A | 10 | 1010 |
| B | 11 | 1011 |
| F | 15 | 1111 |

## Código completo

Archivo: [main.py](main.py).

```python
for numero in (5, 171, 255, 256):
    print(f"{numero}: {numero:02X} / {numero:b}")
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
5: 05 / 101
171: AB / 10101011
255: FF / 11111111
256: 100 / 100000000
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Agrupa bits en bloques de cuatro. Traduce cada bloque. Comprueba por potencias de 16. Prueba el caso 5 y explica el relleno. Compara un valor de 256 para ver que el ancho mínimo no limita el tamaño.

## Errores que conviene detectar

- Tratar A a F como variables en una representación hexadecimal.
- Suponer que un ancho de impresión de dos dígitos restringe el valor a un byte.

## Ejercicio para resolver

Escribe 255 y 256 en hexadecimal. Decide cuál cabe en un byte sin signo.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

255 = FF₁₆ y cabe; 256 = 100₁₆ y necesita nueve bits. El límite sin signo de ocho bits es 2⁸−1 = 255.

</details>

## Preguntas de comprensión

¿Por qué un byte usa dos dígitos hexadecimales? ¿AB representa siempre un carácter? ¿El ancho de impresión valida el rango?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/04-octal/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/06-aritmetica-binaria/README.md)
