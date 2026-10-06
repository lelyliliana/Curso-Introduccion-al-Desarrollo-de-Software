# Solución de problemas: análisis y contrato

[Recurso anterior](../../unidad-2/11-compuertas-y-circuitos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/02-diseno-y-algoritmos/README.md)

## Objetivo

Definir entradas, salidas y reglas antes de programar.

## Conceptos y explicación

Resolver un problema empieza por comprenderlo. Una descripción informal debe convertirse en entradas, resultados esperados, restricciones y casos. El contrato explica qué recibe una operación, qué produce y cómo responde ante datos inválidos. No basta con reemplazar palabras del enunciado por nombres de variables.

El proceso incluye análisis, diseño, codificación, pruebas, documentación y mantenimiento. Estos pasos pueden revisitarse. Una prueba que descubre una regla omitida produce nuevo análisis. Se separa la lógica de una función y la interacción de consola para comprobar casos sin repetir manualmente una sesión.

Caso del curso: calcular el costo de kits solicitados usando cantidades enteras y precio en unidades monetarias enteras. El precio es un dato del ejercicio, no una tarifa vigente. El contrato admite cantidad cero, rechaza negativos y evita confundir True con una cantidad: en Python bool es subclase de int, por eso se comprueba el tipo exacto para este contrato.

## Caso resuelto paso a paso

Entradas: cantidad y precio unitario, ambos enteros no negativos. Salida: costo total = cantidad×precio. Errores: tipo distinto de int o valor negativo.

| Cantidad | Precio | Resultado |
|---|---|---|
| 3 | 12000 | 36000 |
| 0 | 12000 | 0 |
| -1 | 12000 | Rechazo |

El análisis incluye cero y negativo antes de escribir el código. Esta práctica evita inventar reglas cuando el programa ya está hecho.

## Código completo

Archivo: [main.py](main.py).

```python
def costo(cantidad, precio):
    if type(cantidad) is not int or type(precio) is not int:
        raise ValueError("Cantidad y precio deben ser enteros")
    if cantidad < 0 or precio < 0:
        raise ValueError("No se aceptan valores negativos")
    return cantidad * precio

if __name__ == "__main__":
    print(costo(3, 12000))
    print(costo(0, 12000))
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
36000
0
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Enumera entradas y unidades. Calcula dos casos a mano. Define validación. Ejecuta la función con los casos válidos. Explica qué excepción corresponde al inválido.

## Errores que conviene detectar

- Multiplicar una cantidad negativa sin decidir su validez.
- Confundir una tarifa ficticia del ejercicio con un precio vigente.

## Ejercicio para resolver

Añade un costo fijo de transporte no negativo. Decide si se cobra cuando cantidad es cero y actualiza el contrato y tres casos.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Una regla posible: transporte solo si cantidad>0. Salida = cantidad×precio + transporte cuando hay pedido, y 0 cuando no. Casos 3,12000,5000→41000; 0,12000,5000→0; transporte negativo→rechazo. La decisión debe acordarse, no deducirse del nombre del dato.

</details>

## Preguntas de comprensión

¿Por qué declarar las unidades? ¿Es cero inválido por defecto? ¿Qué diferencia hay entre un supuesto y una regla?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-2/11-compuertas-y-circuitos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/02-diseno-y-algoritmos/README.md)
