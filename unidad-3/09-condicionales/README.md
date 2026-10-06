# Condicionales y casos excluyentes

[Recurso anterior](../../unidad-3/08-operadores-y-precedencia/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/10-condicionales-anidados/README.md)

## Objetivo

Construir decisiones que cubran límites sin solapamientos.

## Conceptos y explicación

Un if ejecuta un bloque si su condición es verdadera. elif permite alternativas, y else recoge los casos restantes. En una cadena solo se ejecuta la primera rama verdadera. Varios if separados pueden ejecutar varios bloques; no son equivalentes automáticamente a una cadena.

Las reglas se definen antes que el código. Para stock: cero es agotado; 1 y 2 son bajo; 3 o más es disponible. Los negativos se rechazan antes de clasificar. El orden de condiciones evita que «menor que 3» incluya cantidades inválidas. La indentación sitúa cada instrucción en su rama.

Una prueba útil cubre cada rama y los puntos donde cambia la clasificación: -1,0,1,2,3. No se usan datos arbitrarios solamente del centro de un rango. else no garantiza por sí mismo que la entrada sea válida; el contrato sigue siendo necesario.

## Caso resuelto paso a paso

| Unidades | Rama | Resultado |
|---|---|---|
| -1 | Validación | Rechazo |
| 0 | Primera | agotado |
| 1,2 | Segunda | bajo |
| 3 o más | Tercera | disponible |

La función retorna texto; el bucle principal presenta cada caso. Así se puede comprobar el criterio sin teclado.

## Código completo

Archivo: [main.py](main.py).

```python
def estado(unidades):
    if type(unidades) is not int or unidades < 0:
        raise ValueError("Unidades enteras no negativas")
    if unidades == 0:
        return "agotado"
    elif unidades <= 2:
        return "bajo"
    else:
        return "disponible"

if __name__ == "__main__":
    for n in (0, 1, 2, 3):
        print(f"{n}: {estado(n)}")
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
0: agotado
1: bajo
2: bajo
3: disponible
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Dibuja rangos sin huecos. Escribe validación. Predice cinco casos. Ejecuta. Cambia el umbral de stock bajo y actualiza tabla y pruebas.

## Errores que conviene detectar

- Clasificar un negativo como stock bajo antes de validar.
- Usar if independientes donde las alternativas deben ser excluyentes.

## Ejercicio para resolver

Añade estado abundante para 10 o más. Mantén agotado y bajo y define disponible para 3..9.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Después de validar: if n==0; elif n<=2; elif n<10; else abundante. Prueba 0,2,3,9,10 y negativo. Otra organización equivalente es válida si cubre el dominio completo.

</details>

## Preguntas de comprensión

¿Cuándo conviene elif? ¿Qué detecta probar justo en 3? ¿Puede else esconder datos inválidos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/08-operadores-y-precedencia/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/10-condicionales-anidados/README.md)
