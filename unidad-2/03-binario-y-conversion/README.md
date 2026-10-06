# Sistema binario y divisiones sucesivas

[Recurso anterior](../../unidad-2/02-decimal-y-fracciones/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/04-octal/README.md)

## Objetivo

Convertir enteros no negativos a binario con residuos.

## Conceptos y explicación

Para convertir un entero no negativo a base 2, divide sucesivamente entre 2 y conserva el residuo de cada división. El residuo vale 0 cuando el dividendo es par y 1 cuando es impar. No se invierte esa regla. Los residuos aparecen del bit menos significativo al más significativo, por lo que se leen en orden inverso.

El algoritmo termina cuando el cociente llega a cero. El caso cero requiere una representación explícita «0», pues el ciclo no ejecutaría ninguna vuelta. Para enteros negativos aquí se rechaza la entrada: representarlos con un signo o con complemento a dos son problemas diferentes.

Una prueba de escritorio registra dividendo, cociente y residuo. La conversión inversa por suma de pesos permite comprobar el resultado sin depender únicamente del mismo algoritmo. Un bit es una unidad abstracta de dos estados; los dispositivos usan codificaciones físicas que no siempre equivalen a «tensión presente = 1».

## Caso resuelto paso a paso

| Dividendo | Cociente | Residuo |
|---|---|---|
| 13 | 6 | 1 |
| 6 | 3 | 0 |
| 3 | 1 | 1 |
| 1 | 0 | 1 |

Lectura inversa: 1101₂. Comprobación: 8 + 4 + 1 = 13. Para 64 se obtiene 1000000, con un 1 y seis ceros.

## Código completo

Archivo: [main.py](main.py).

```python
def a_binario(numero):
    if type(numero) is not int or numero < 0:
        raise ValueError("Se requiere un entero no negativo")
    if numero == 0:
        return "0"
    residuos = []
    while numero > 0:
        numero, residuo = divmod(numero, 2)
        residuos.append(str(residuo))
    return "".join(reversed(residuos))

if __name__ == "__main__":
    for n in (0, 13, 64):
        print(f"{n} -> {a_binario(n)}")
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
0 -> 0
13 -> 1101
64 -> 1000000
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Traza las divisiones antes de ejecutar. Revisa el caso cero. Ejecuta y compara con format. Comprueba la expansión posicional. Prueba entrada negativa y explica el contrato.

## Errores que conviene detectar

- Invertir la regla del residuo: un dividendo par deja 0.
- Olvidar que cero necesita una representación aunque el ciclo no ejecute vueltas.

## Ejercicio para resolver

Convierte 18 y 0 manualmente. Modifica la función para producir un signo menos y el valor absoluto de un negativo, sin afirmar que es complemento a dos.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

18 produce residuos 0,1,0,0,1 y se escribe 10010. Cero produce 0. Para negativos puede devolverse "-" + a_binario(-numero); eso es una representación con signo visible, no un patrón de bits de ancho fijo.

</details>

## Preguntas de comprensión

¿Qué residuo tiene un número par? ¿Por qué invertir el orden? ¿Cuántas vueltas realiza el caso cero?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/02-decimal-y-fracciones/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/04-octal/README.md)
