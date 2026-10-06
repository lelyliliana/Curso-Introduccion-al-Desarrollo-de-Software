# Diseño, pseudocódigo y prueba de escritorio

[Recurso anterior](../../unidad-3/01-analisis-del-problema/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/03-pruebas-depuracion-y-mantenimiento/README.md)

## Objetivo

Representar una solución antes de codificarla.

## Conceptos y explicación

Un algoritmo especifica pasos para una clase de entradas bajo condiciones definidas. En estos ejercicios se espera que termine y produzca un resultado determinado. No todo sistema que permanece atendiendo eventos se describe como un cálculo finito único: cada operación puede terminar aunque el servicio siga activo.

El pseudocódigo expresa pasos sin depender de la sintaxis exacta de un lenguaje. Debe declarar cómo funcionan asignación, división y condiciones. Un diagrama de flujo muestra secuencia y decisiones. Ninguna representación reemplaza indicar entradas válidas y resultados.

La prueba de escritorio simula cambios de variables. Evalúa la expresión con los valores anteriores y luego registra la asignación. El signo ← representa asignación; = en una ecuación matemática representa igualdad. El programa usa `=` para asignar y `==` para comparar. Una tabla permite localizar el primer paso donde la solución difiere de lo esperado.

## Caso resuelto paso a paso

Se reparten 17 kits entre 5 mesas. Se requiere al menos una mesa y cantidad no negativa.

```text
LEER kits, mesas
SI kits < 0 O mesas <= 0: RECHAZAR
por_mesa ← kits DIV mesas
sobran ← kits MOD mesas
MOSTRAR por_mesa, sobran
```

| Paso | Kits | Mesas | Por mesa | Sobran |
|---|---|---|---|---|
| Entrada | 17 | 5 | — | — |
| División entera | 17 | 5 | 3 | — |
| Residuo | 17 | 5 | 3 | 2 |

Comprobación: 17 = 5×3+2 y 0≤2<5.

## Código completo

Archivo: [main.py](main.py).

```python
def repartir(kits, mesas):
    if type(kits) is not int or type(mesas) is not int or kits < 0 or mesas <= 0:
        raise ValueError("Kits no negativos y mesas positivas, ambos enteros")
    return divmod(kits, mesas)

if __name__ == "__main__":
    por_mesa, sobran = repartir(17, 5)
    print(f"Por mesa: {por_mesa}; sobran: {sobran}")
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
Por mesa: 3; sobran: 2
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Escribe la regla de reparto. Traza la tabla. Ejecuta. Prueba reparto exacto y menos kits que mesas. Explica por qué mesas cero debe rechazarse.

## Errores que conviene detectar

- Permitir mesas=0 antes de dividir.
- Interpretar una asignación como una igualdad algebraica permanente.

## Ejercicio para resolver

Resuelve 20 kits entre 4 mesas y 3 entre 5. Agrega validación de tipos como en la lección anterior.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Resultados: (5,0) y (0,3). Exige type(kits) is int y type(mesas) is int antes de usar divmod. Que haya menos kits no invalida el reparto; produce cero por mesa y el resto permanece sin repartir.

</details>

## Preguntas de comprensión

¿Una asignación crea una ecuación permanente? ¿Qué expresa el residuo? ¿Qué detecta una prueba de escritorio?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/01-analisis-del-problema/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/03-pruebas-depuracion-y-mantenimiento/README.md)
