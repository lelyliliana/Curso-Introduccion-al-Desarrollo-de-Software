# Pruebas, depuración, documentación y mantenimiento

[Recurso anterior](../../unidad-3/02-diseno-y-algoritmos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/04-python-y-ejecucion/README.md)

## Objetivo

Localizar un defecto y conservar pruebas que lo detecten.

## Conceptos y explicación

Un error de sintaxis impide interpretar correctamente el archivo; una excepción ocurre durante la ejecución; un defecto lógico puede producir un resultado incorrecto sin lanzar una excepción. La depuración busca la causa, no solo una modificación que esconda el síntoma.

Una estrategia es reproducir el problema, reducir las entradas, comparar resultado esperado y obtenido y seguir el estado hasta la primera diferencia. Leer el traceback ayuda a localizar dónde se detectó la excepción, aunque la causa puede estar antes. Los puntos de interrupción de un depurador permiten inspeccionar valores sin agregar muchas impresiones.

La documentación describe uso, contratos, decisiones y límites. El mantenimiento corrige defectos, adapta el programa a cambios y mejora su estructura. Una prueba de regresión conserva el caso que fallaba para que el defecto no vuelva inadvertidamente. El módulo unittest de la biblioteca estándar permite escribir comparaciones y pruebas de excepciones.

## Caso resuelto paso a paso

Defecto inicial imaginado: una función de descuento usa `monto > 100000` cuando la regla exige `monto >= 100000`. Probar 120000 no detecta el error; 100000 sí.

| Monto | Regla | Esperado |
|---|---|---|
| 99999 | Sin descuento | 99999 |
| 100000 | 10% | 90000 |
| 100010 | 10% | 90009 |

El ejemplo opera con múltiplos de diez en los casos con descuento. La función rechaza montos que producirían fracciones bajo esa regla de enteros: el contrato debe decidir redondeo antes de ampliarse.

## Código completo

Archivo: [main.py](main.py).

```python
def total(monto):
    if type(monto) is not int or monto < 0:
        raise ValueError("Monto entero no negativo requerido")
    if monto >= 100000:
        if monto % 10 != 0:
            raise ValueError("Para este ejemplo, el monto con descuento debe ser múltiplo de diez")
        return monto - monto // 10
    return monto

if __name__ == "__main__":
    for monto in (99999, 100000, 100010):
        print(f"{monto} -> {total(monto)}")
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
99999 -> 99999
100000 -> 90000
100010 -> 90009
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Ejecuta los casos. Cambia >= por > y observa el fallo. Restaura. Añade un caso negativo. Escribe qué regla protegió cada prueba. Documenta cómo tratar cantidades no divisibles por diez.

## Errores que conviene detectar

- Probar solo 120000 y omitir el umbral exacto 100000.
- Cambiar redondeo sin definirlo en el contrato.

## Ejercicio para resolver

Reemplaza la restricción de múltiplos de diez por una regla que permita Decimal. Define redondeo y conserva pruebas del umbral.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Puede representarse el monto con Decimal desde texto y redondear a dos decimales con una política acordada, por ejemplo ROUND_HALF_UP. No conviertas primero a float. El umbral conserva casos inferior, igual y superior; añade uno que obligue a redondear.

</details>

## Preguntas de comprensión

¿Un traceback siempre señala la causa original? ¿Qué es una prueba de regresión? ¿Por qué un umbral exige casos a ambos lados?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/02-diseno-y-algoritmos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/04-python-y-ejecucion/README.md)
