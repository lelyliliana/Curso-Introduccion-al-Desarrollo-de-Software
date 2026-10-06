# Listas: índices, cambios y copias

[Recurso anterior](../../unidad-3/16-recursion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/18-diccionarios-y-registros/README.md)

## Objetivo

Administrar una secuencia mutable y resolver suma y extremos.

## Conceptos y explicación

Una lista es una secuencia mutable. Sus índices comienzan en cero; un índice negativo cuenta desde el final. Acceder fuera del rango lanza IndexError. Un slice produce una lista exterior nueva y admite un final excluido. La lista puede contener objetos de distintos tipos, pero este contrato utiliza solamente cantidades enteras.

append agrega un elemento, pop lo retira y devuelve, y remove retira la primera coincidencia de un valor. sort modifica la lista y retorna None; sorted devuelve una lista nueva. Confundir el resultado de sort con la lista ordenada es un error habitual.

Para buscar máximo o mínimo en datos posiblemente negativos se parte del primer elemento, no siempre de cero. Si la colección está vacía, el contrato debe definir qué hacer. El ejemplo requiere al menos un elemento para max y muestra copia y orden sin alterar el orden original. Una lista de Python no es necesariamente un arreglo homogéneo de tamaño fijo.

## Caso resuelto paso a paso

Cantidades[4,0,8]. La posición0 contiene4; la última contiene8. La suma es12 y el máximo8. sorted produce[0,4,8] conservando la lista original.

Si se usara max con[] sin valor predeterminado, se produciría ValueError. Para[-8,-3], inicializar el máximo en0 sería incorrecto:0 no pertenece a los datos.

## Código completo

Archivo: [main.py](main.py).

```python
datos = [4, 0, 8]
print(datos[0], datos[-1])
print(sum(datos), max(datos))
ordenados = sorted(datos)
print(ordenados)
print(datos)
copia = datos[:]
copia.append(2)
print(copia)
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
4 8
12 8
[0, 4, 8]
[4, 0, 8]
[4, 0, 8, 2]
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Predice índices y suma. Ejecuta. Comprueba que sorted no altera original. Prueba una copia con append. Traza el máximo de negativos empezando por el primer valor.

## Errores que conviene detectar

- Asignar el resultado de sort esperando una lista.
- Inicializar máximo en cero cuando todos los datos son negativos.

## Ejercicio para resolver

Escribe resumen(datos) que devuelva total,mínimo,máximo y rechace lista vacía.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Comprueba if not datos: raise ValueError. Usa sum(datos),min(datos),max(datos) o ciclos explícitos. Pruebas[4,0,8]→(12,0,8),[-8,-3]→(-11,-8,-3),[]→error.

</details>

## Preguntas de comprensión

¿sort devuelve una lista ordenada? ¿Qué diferencia hay entre pop y remove? ¿Por qué cero puede ser mal máximo inicial?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/16-recursion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/18-diccionarios-y-registros/README.md)
