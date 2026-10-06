# Funciones, parámetros, argumentos y retorno

[Recurso anterior](../../unidad-3/13-break-continue-y-anidacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/15-alcance-y-mutabilidad/README.md)

## Objetivo

Separar cálculo y presentación con funciones comprobables.

## Conceptos y explicación

Una función define una operación con un nombre. Sus parámetros son nombres en la definición; los argumentos son valores suministrados al llamarla. return entrega un resultado y termina esa llamada. print presenta un mensaje, pero no devuelve ese valor al llamador. Una función sin return explícito devuelve None.

Un contrato describe entradas, resultado y errores. Una docstring puede resumirlo. El contrato no se cumple por escribirla: la implementación y las pruebas deben coincidir. Separar cálculo de presentación permite reutilizar la función y probarla sin capturar consola.

Los argumentos pueden darse por posición o por nombre. Evita valores predeterminados mutables cuando cada llamada necesita una colección nueva; se estudia esa relación en las listas. En estos ejemplos la función devuelve un nuevo resultado sin alterar datos externos. Una función pequeña no necesita leer teclado si ya recibe el dato como argumento.

## Caso resuelto paso a paso

La función costo recibe cantidad y precio. costo(3,12000) y costo(precio=12000,cantidad=3) producen36000. Mostrar el resultado es responsabilidad del bloque principal.

| Concepto | En el ejemplo |
|---|---|
| Parámetros | cantidad, precio |
| Argumentos | 3,12000 |
| Retorno | 36000 |
| Presentación | print del llamador |

## Código completo

Archivo: [main.py](main.py).

```python
def costo(cantidad, precio):
    """Devuelve costo entero; rechaza tipos incorrectos y valores negativos."""
    if type(cantidad) is not int or type(precio) is not int or cantidad < 0 or precio < 0:
        raise ValueError("Enteros no negativos requeridos")
    return cantidad * precio

if __name__ == "__main__":
    resultado = costo(3, 12000)
    print(resultado)
    print(costo(precio=12000, cantidad=3))
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
36000
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Identifica parámetros. Ejecuta por posición y nombre. Guarda el retorno en una variable. Cambia print dentro de una versión experimental y observa que no sustituye return. Mantén validaciones del contrato.

## Errores que conviene detectar

- Mostrar con print cuando el llamador necesita un retorno.
- Confundir nombres de parámetros con valores de argumentos.

## Ejercicio para resolver

Escribe disponible(total,prestadas), exige 0<=prestadas<=total y devuelve total-prestadas.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Valida ambos como enteros, total>=0 y0<=prestadas<=total. Devuelve la resta. Casos (5,2)→3,(5,5)→0,(5,6)→error. La función no modifica inventario ni muestra mensajes.

</details>

## Preguntas de comprensión

¿print y return cumplen la misma función? ¿Qué diferencia hay entre parámetro y argumento? ¿Quién debe manejar la interacción?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/13-break-continue-y-anidacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/15-alcance-y-mutabilidad/README.md)
