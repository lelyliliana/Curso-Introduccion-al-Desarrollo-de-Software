# Bits, representación con signo y límites

[Recurso anterior](../../unidad-2/06-aritmetica-binaria/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/08-logica-y-tablas/README.md)

## Objetivo

Distinguir ancho, rango, signo y desbordamiento.

## Conceptos y explicación

Con n bits hay 2ⁿ patrones posibles. Sin signo representan de 0 a 2ⁿ−1. En complemento a dos de n bits representan de −2ⁿ⁻¹ a 2ⁿ⁻¹−1. Un mismo patrón puede significar cantidades diferentes según la convención; 11111111 de ocho bits es 255 sin signo y −1 con complemento a dos.

Para codificar un negativo válido en complemento a dos se puede sumar 2ⁿ al valor y escribir el resultado en n bits. Para decodificar, si el bit más alto es 1, se resta 2ⁿ al valor sin signo. El ancho debe declararse antes de aplicar la regla. «−101» es una notación con signo visible, no complemento a dos.

Un byte son ocho bits. Las unidades decimales kB/MB usan potencias de 1000; KiB/MiB usan potencias de 1024. Los enteros Python crecen según la necesidad, pero los archivos y protocolos pueden imponer rangos. Por eso el programa valida antes de codificar y no oculta un desbordamiento con una máscara.

## Caso resuelto paso a paso

Rango de ocho bits con signo: −128..127. Para −5: 256−5 = 251; 251 se escribe 11111011. Al leer ese patrón, 251−256 = −5. El primer bit señala aquí que debe aplicarse la resta, bajo esta convención.

| Convención de ocho bits | Mínimo | Máximo |
|---|---|---|
| Sin signo | 0 | 255 |
| Complemento a dos | −128 | 127 |

## Código completo

Archivo: [main.py](main.py).

```python
def complemento(numero, bits):
    if type(bits) is not int or bits <= 0:
        raise ValueError("Ancho positivo requerido")
    if type(numero) is not int or not -(2**(bits-1)) <= numero < 2**(bits-1):
        raise ValueError("Fuera de rango")
    patron = numero if numero >= 0 else 2**bits + numero
    return format(patron, f"0{bits}b")

if __name__ == "__main__":
    for n in (-128, -5, -1, 0, 127):
        print(f"{n}: {complemento(n, 8)}")
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
-128: 10000000
-5: 11111011
-1: 11111111
0: 00000000
127: 01111111
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Declara ancho y convención. Verifica rango. Codifica con la suma de 2ⁿ para negativos. Comprueba decodificando. Prueba los dos extremos y el primer valor que queda fuera.

## Errores que conviene detectar

- Decodificar un patrón con signo sin declarar su ancho.
- Usar una máscara para esconder un dato que no cabe en el rango.

## Ejercicio para resolver

Representa −1 y −128 en complemento a dos de ocho bits. Explica por qué 128 no cabe con signo.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

−1 → 11111111; −128 → 10000000. 128 supera el máximo 127. El patrón 10000000 ya representa −128 con signo; no puede representar ambos a la vez bajo la misma convención.

</details>

## Preguntas de comprensión

¿Un patrón tiene significado sin contexto? ¿Por qué hay un negativo más que positivos no nulos? ¿Un entero Python grande evita límites de formatos externos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/06-aritmetica-binaria/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/08-logica-y-tablas/README.md)
