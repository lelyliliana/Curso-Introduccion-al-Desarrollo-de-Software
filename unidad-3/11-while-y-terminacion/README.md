# Ciclo while, progreso y terminación

[Recurso anterior](../../unidad-3/10-condicionales-anidados/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/12-for-y-recorridos/README.md)

## Objetivo

Relacionar condición, actualización e invariante de un ciclo.

## Conceptos y explicación

while repite mientras una condición sea verdadera, evaluándola antes de cada vuelta. Puede ejecutar cero veces. Para un cálculo que debe terminar, identifica una medida que progrese hacia una condición de salida y evita que continue omita su actualización.

Un contador mide repeticiones; un acumulador reúne resultados. En este ejemplo i cuenta números incluidos y total acumula su suma. La propiedad después de cada vuelta es total=1+...+i. Esa propiedad ayuda a verificar el algoritmo. La condición i<n y la actualización i+=1 aseguran que se incorporen exactamente los números 1..n.

Un ciclo infinito puede ser accidental por falta de progreso o deliberado en un menú que termina con break. En cualquier caso debe entenderse cómo se detiene. Ctrl+C permite interrumpir una práctica que se queda ejecutando, pero no corrige el defecto. No se presenta un ciclo infinito como archivo predeterminado de este curso.

## Caso resuelto paso a paso

Para n=3:

| Vuelta | i después de incrementar | total |
|---|---|---|
| Inicial | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

Al evaluar 3<3 la repetición termina. Para n=0 no hay vueltas y la suma es 0.

## Código completo

Archivo: [main.py](main.py).

```python
def sumar_hasta(n):
    if type(n) is not int or n < 0:
        raise ValueError("Entero no negativo requerido")
    i = total = 0
    while i < n:
        i += 1
        total += i
    return total

if __name__ == "__main__":
    for n in (0, 3, 5):
        print(f"{n}: {sumar_hasta(n)}")
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
0: 0
3: 6
5: 15
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Traza n=3. Señala la actualización que da progreso. Ejecuta n=0 y3. Comprueba con n(n+1)/2. Explica qué sucede si quitas el incremento sin ejecutar indefinidamente.

## Errores que conviene detectar

- Omitir el incremento de i y perder progreso.
- Sumar antes de incrementar sin revisar el intervalo incluido.

## Ejercicio para resolver

Construye una cuenta regresiva desde n hasta 1 y explica la medida que disminuye.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Usa i=n, while i>0: mostrar i y luego i-=1. La medida i es un entero no negativo que disminuye; para n=0 no imprime. Valida n entero no negativo antes de empezar.

</details>

## Preguntas de comprensión

¿while ejecuta siempre una vuelta? ¿Qué propiedad conserva el acumulador? ¿Por qué Ctrl+C no es una solución?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/10-condicionales-anidados/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/12-for-y-recorridos/README.md)
