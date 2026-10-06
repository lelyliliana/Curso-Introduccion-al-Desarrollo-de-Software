# Sistema octal y agrupación de bits

[Recurso anterior](../../unidad-2/03-binario-y-conversion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/05-hexadecimal/README.md)

## Objetivo

Relacionar un dígito octal con tres bits.

## Conceptos y explicación

Como 8 = 2³, cada dígito octal corresponde a tres bits. Agrupar la parte entera desde la derecha mantiene el valor posicional. Se pueden añadir ceros a la izquierda para completar un grupo, pero no a la derecha de un entero: eso multiplicaría el valor.

110101₂ se agrupa 110 101 y equivale a 65₈. Cada grupo se interpreta de 0 a 7. Para una fracción, los grupos comienzan desde el separador hacia la derecha; completar con ceros al final de esa parte fraccionaria sí conserva el valor. En este ejemplo el programa trabaja solo con enteros.

En Python `oct` incluye el prefijo 0o y `format(n, 'o')` devuelve los dígitos. El prefijo no pertenece al conjunto de dígitos octales. No es necesario usar octal para todo trabajo: aparece en representaciones y permisos, pero su utilidad depende del contexto.

## Caso resuelto paso a paso

53₁₀ = 110101₂ = 65₈. Expansión octal: 6×8 + 5 = 53. Cada posición octal agrupa tres posiciones binarias.

| Grupo binario | Octal |
|---|---|
| 000 | 0 |
| 011 | 3 |
| 101 | 5 |
| 111 | 7 |

La impresión con ancho 6 conserva ceros iniciales para mostrar grupos completos.

## Código completo

Archivo: [main.py](main.py).

```python
numero = 53
print(format(numero, "06b"))
print(oct(numero))
print(int("65", 8))
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
110101
0o65
53
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Convierte a binario. Agrupa de derecha a izquierda. Traduce cada grupo. Comprueba con expansión octal. Explica los ceros que agregaste.

## Errores que conviene detectar

- Agrupar la parte entera desde la izquierda sin completar el primer grupo.
- Añadir ceros al final de un entero creyendo que conserva su valor.

## Ejercicio para resolver

Convierte 10111₂ a octal y después 72₈ a binario.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

010 111₂ = 27₈. Para 72₈: 7 → 111 y 2 → 010; resulta 111010₂. Añadir el cero izquierdo no alteró 23₁₀ en el primer ejercicio.

</details>

## Preguntas de comprensión

¿Por qué grupos de tres? ¿Es válido el dígito 8? ¿Qué diferencia hay entre completar a la izquierda y a la derecha?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/03-binario-y-conversion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/05-hexadecimal/README.md)
