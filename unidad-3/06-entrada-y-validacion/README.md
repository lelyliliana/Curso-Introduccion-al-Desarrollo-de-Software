# Entrada, conversión y validación

[Recurso anterior](../../unidad-3/05-variables-y-asignacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/07-tipos-y-precision/README.md)

## Objetivo

Convertir texto de consola y separar formato de dominio.

## Conceptos y explicación

`input` devuelve texto y retira el salto de línea final. No determina automáticamente si una entrada es número. `int` convierte una representación válida de entero; `float` interpreta un número de punto flotante. `int("3.5")` no redondea: falla porque ese texto no representa un entero.

La validación tiene al menos dos partes: formato y dominio. "tres" falla en formato para int; "-3" se convierte pero viola el dominio si se exige cantidad no negativa. Capturar ValueError en la frontera de entrada permite informar el problema. No se captura cualquier excepción indiscriminadamente, pues escondería errores de programación.

Este ejemplo exige cantidad de 0 a 10, sin repetir preguntas. Una versión posterior con menú podrá solicitar nuevamente. La función de conversión recibe texto y se prueba por separado de input. Los ejemplos guardan entradas reproducibles cuando necesitan teclado. No se usa eval para interpretar datos escritos por usuarios.

## Caso resuelto paso a paso

| Texto | Conversión | Resultado de dominio |
|---|---|---|
| "3" | 3 | Válido |
| "-1" | -1 | Rechazo |
| "11" | 11 | Rechazo |
| "tres" | Error | No llega a dominio |

El ejemplo con entrada 3 informa 3 unidades. La entrada automatizada reproduce esa interacción sin requerir escritura manual.

## Código completo

Archivo: [main.py](main.py).

```python
def cantidad_desde_texto(texto):
    try:
        cantidad = int(texto)
    except ValueError as error:
        raise ValueError("Escribe un entero") from error
    if not 0 <= cantidad <= 10:
        raise ValueError("Cantidad de 0 a 10")
    return cantidad

if __name__ == "__main__":
    try:
        cantidad = cantidad_desde_texto(input("Cantidad: "))
        print(f"Registradas: {cantidad}")
    except ValueError as error:
        print(f"Error: {error}")
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

Cuando aparezca `Cantidad:`, escribe `3` y pulsa Enter. La [entrada reproducible](entrada.txt) contiene ese valor.

### Salida esperada

```text
Cantidad: Registradas: 3
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Ejecuta y escribe 3. Prueba 0,10,-1,11 y tres. Clasifica el error. Revisa que el programa termina de manera informada. Cambia el rango y actualiza sus pruebas.

## Errores que conviene detectar

- Suponer que input devuelve un número.
- Confundir formato inválido con entero fuera del rango.

## Ejercicio para resolver

Acepta solo cantidades de 1 a 5 y mejora el mensaje para distinguir formato de rango.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Mantén int(texto) dentro de un try específico y convierte su ValueError en "Escribe un entero". Después comprueba 1<=cantidad<=5 y lanza "Cantidad de 1 a 5" si falla. Prueba ambos errores por separado.

</details>

## Preguntas de comprensión

¿Qué tipo devuelve input? ¿Convertir demuestra que el dato cumple el problema? ¿Por qué evitar eval?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/05-variables-y-asignacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/07-tipos-y-precision/README.md)
