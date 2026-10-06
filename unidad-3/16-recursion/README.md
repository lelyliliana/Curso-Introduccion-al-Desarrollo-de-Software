# Recursión, caso base y progreso

[Recurso anterior](../../unidad-3/15-alcance-y-mutabilidad/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/17-listas-y-recorridos/README.md)

## Objetivo

Explicar llamadas recursivas y reconocer sus límites.

## Conceptos y explicación

Una función recursiva se llama a sí misma directa o indirectamente. Necesita un caso base y una reducción hacia ese caso. Para factorial de n no negativo: 0!=1 y n!=n×(n−1)! para n>0. Rechazar negativos evita una reducción que nunca llega a cero.

Cada llamada conserva información para terminar su operación al regresar. factorial(3) espera factorial(2), que espera factorial(1), que espera factorial(0). El retorno resuelve la cadena de adentro hacia afuera. No basta con saber que aparece una llamada: hay que demostrar que progresa.

Python tiene un límite de profundidad y no elimina automáticamente llamadas recursivas de cola. Para un cálculo repetitivo sencillo, una versión iterativa evita esa dependencia. No se aumenta el límite como primera solución. El ejemplo restringe n a0..100 para ser una práctica pequeña; no es una biblioteca numérica general.

## Caso resuelto paso a paso

Traza factorial(3): 3×factorial(2),2×factorial(1),1×factorial(0),caso base1. Retornos1,1,2,6.

| n | Factorial |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 3 | 6 |
| 5 | 120 |

Una comprobación adicional puede usar math.factorial para esos valores. El costo de multiplicar enteros crecientes también aumenta; contar llamadas no equivale a medir todo el tiempo.

## Código completo

Archivo: [main.py](main.py).

```python
def factorial(n):
    if type(n) is not int or not 0 <= n <= 100:
        raise ValueError("Entero de 0 a 100 requerido")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    for n in (0, 3, 5):
        print(f"{n}! = {factorial(n)}")
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
0! = 1
3! = 6
5! = 120
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Dibuja la cadena de llamadas para3. Marca caso base. Ejecuta0,3,5. Explica la validación. Reescribe iterativamente y compara resultados.

## Errores que conviene detectar

- Omitir el caso base o no acercarse a él.
- Aumentar el límite de recursión en lugar de analizar una alternativa iterativa.

## Ejercicio para resolver

Implementa factorial iterativo para0..100 y comprueba coincidencia con la función recursiva.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Inicializa resultado=1 y recorre range(2,n+1) multiplicando. Reutiliza la validación. Cero y uno no recorren valores y conservan1. Compara todos los valores del rango permitido.

</details>

## Preguntas de comprensión

¿Qué garantiza llegar al caso base? ¿Por qué validar negativos? ¿Cuándo conviene iterar?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/15-alcance-y-mutabilidad/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/17-listas-y-recorridos/README.md)
