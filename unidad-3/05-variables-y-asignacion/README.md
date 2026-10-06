# Variables, nombres y asignación

[Recurso anterior](../../unidad-3/04-python-y-ejecucion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/06-entrada-y-validacion/README.md)

## Objetivo

Seguir asociaciones de nombres y explicar actualización de valores.

## Conceptos y explicación

En Python un nombre se asocia a un objeto mediante asignación. La expresión de la derecha se evalúa antes de asociar el resultado con el nombre de la izquierda. `unidades = unidades - 1` utiliza el valor anterior; no es una igualdad matemática contradictoria.

Los nombres distinguen mayúsculas y minúsculas, no empiezan por un dígito y no deben ser palabras reservadas. Se prefieren nombres que indiquen significado, como unidades_disponibles, en lugar de x cuando el propósito ya se conoce. Python permite caracteres Unicode, pero en identificadores de estos ejercicios se evita depender de acentos para facilitar escritura; en los textos sí se conserva español.

Una constante de aplicación puede nombrarse PRECIO_UNITARIO por convención; las mayúsculas no impiden reasignarla. Asignar b=a no crea una relación algebraica permanente ni necesariamente copia un objeto. Con enteros, reasignar a no cambia b. Con listas, ambos nombres pueden referirse a la misma colección, tema que se estudia más adelante.

## Caso resuelto paso a paso

Estado inicial: unidades=4, copia=4. Después unidades -= 1, unidades=3 y copia=4. La segunda asignación no transforma copia porque un entero es inmutable y el nombre unidades se asocia a otro resultado.

| Paso | unidades | copia |
|---|---|---|
| Asignación inicial | 4 | — |
| copia = unidades | 4 | 4 |
| unidades -= 1 | 3 | 4 |

El intercambio `a,b=b,a` evalúa ambos valores anteriores antes de asignar.

## Código completo

Archivo: [main.py](main.py).

```python
unidades = 4
copia = unidades
unidades -= 1
print(unidades, copia)
a, b = 2, 7
a, b = b, a
print(a, b)
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
3 4
7 2
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Completa la tabla sin ejecutar. Comprueba. Cambia -= por += y vuelve a trazar. Intercambia dos nombres. Explica por qué la copia del valor anterior no se actualiza.

## Errores que conviene detectar

- Esperar que copia cambie después de reasignar unidades.
- Suponer que las mayúsculas impiden reasignar una constante.

## Ejercicio para resolver

Traza a=2; b=a; a=a+5; b=b*3. Escribe los valores finales y propone nombres más claros para un inventario.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Final: a=7 y b=6. Si representan inventario: unidades_actuales y unidades_iniciales, aunque multiplicar las iniciales debe justificarse por el problema. Elegir nombres no cambia el comportamiento.

</details>

## Preguntas de comprensión

¿Las mayúsculas vuelven inmutable un objeto? ¿Qué se evalúa primero? ¿Por qué b=a no crea una fórmula dinámica?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/04-python-y-ejecucion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/06-entrada-y-validacion/README.md)
