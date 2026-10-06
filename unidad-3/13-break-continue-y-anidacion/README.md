# break, continue y ciclos anidados

[Recurso anterior](../../unidad-3/12-for-y-recorridos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/14-funciones-y-contratos/README.md)

## Objetivo

Controlar interrupción, omisión y recorridos de dos dimensiones.

## Conceptos y explicación

break termina el ciclo envolvente más cercano. continue omite el resto de la vuelta actual y continúa con la siguiente. No son intercambiables: filtrar un dato y terminar toda la búsqueda tienen objetivos distintos. En un while, la actualización necesaria debe ocurrir aunque se ejecute continue.

Un ciclo anidado recorre combinaciones. Con r filas y c columnas, visitar toda una matriz regular requiere r×c visitas. Un break en el ciclo interno no termina automáticamente el externo. Para una búsqueda puede usarse una función con return al encontrar el resultado, evitando una bandera cuando el contrato lo permite.

No se modifica una colección mientras se recorre sin analizar qué ocurre con los índices. Para filtrar conviene producir una colección nueva. El ejemplo muestra filtrado de cantidades negativas y búsqueda de la primera posición de un valor en una matriz rectangular pequeña.

## Caso resuelto paso a paso

Lista [4,-1,0,8] incluye -1 como dato a descartar bajo esta regla del ejemplo; continue omite su suma y el total es12. La matriz [[4,0],[8,2]] tiene 4 posiciones; la primera aparición de8 está en fila1,columna0.

Esta práctica no convierte silenciosamente cualquier negativo de un inventario en aceptable: en el proyecto final los negativos se rechazan. Filtrar es una decisión explícita del caso.

## Código completo

Archivo: [main.py](main.py).

```python
def buscar(matriz, objetivo):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == objetivo:
                return i, j
    return None

if __name__ == "__main__":
    total = 0
    for n in (4, -1, 0, 8):
        if n < 0:
            continue
        total += n
    print(total)
    print(buscar([[4, 0], [8, 2]], 8))
    print(buscar([[4, 0], [8, 2]], 9))
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
12
(1, 0)
None
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Traza qué instrucciones se omiten. Ejecuta. Busca un valor ausente. Cambia la matriz y repite. Explica el alcance de return frente a break interno.

## Errores que conviene detectar

- Creer que break interno termina ambos ciclos.
- Usar continue antes de una actualización necesaria en while.

## Ejercicio para resolver

Escribe una búsqueda que use break y una bandera en lugar de return temprano. Verifica presente y ausente.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Guarda posicion=None antes de recorrer. Al encontrar, asigna (fila,columna), rompe el interno y después comprueba la bandera para romper el externo. Return temprano dentro de una función resulta más directo para este contrato.

</details>

## Preguntas de comprensión

¿continue termina el ciclo? ¿break interno termina ambos? ¿Por qué la regla de filtrado debe declararse?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/12-for-y-recorridos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/14-funciones-y-contratos/README.md)
