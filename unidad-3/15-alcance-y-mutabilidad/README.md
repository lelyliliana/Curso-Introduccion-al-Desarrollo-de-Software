# Ámbito de nombres y mutabilidad

[Recurso anterior](../../unidad-3/14-funciones-y-contratos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/16-recursion/README.md)

## Objetivo

Distinguir reasignación local y modificación de un objeto compartido.

## Conceptos y explicación

El ámbito determina dónde se resuelve un nombre. Un parámetro es local a la función; asignarle otro valor no reasigna automáticamente el nombre del llamador. Python pasa argumentos asociando parámetros con los objetos suministrados. La expresión «todo se pasa por referencia» sin matices induce errores: debe distinguirse entre cambiar el objeto y reasignar el nombre local.

Un int es inmutable; una list es mutable. La función puede modificar una lista recibida y el llamador observar el cambio. Puede también reasignar el parámetro a otra lista, lo que no cambia la asociación externa. La copia superficial crea una lista nueva, pero elementos mutables anidados pueden seguir compartidos.

Para evitar efectos inesperados, el contrato indica si una función modifica sus argumentos. Cuando se necesita una salida independiente, se construye una colección nueva. Las variables globales hacen dependencias menos visibles; se prefieren argumentos y retornos para reglas pequeñas. No es necesario usar global para resolver cada ejercicio.

## Caso resuelto paso a paso

aumentar_local recibe el entero4, calcula5 localmente y lo retorna; el nombre original conserva4 hasta que el llamador lo reasigna. agregar modifica una lista de cantidades añadiendo8; el cambio se observa fuera.

La copia de la lista simple contiene enteros inmutables: modificar su estructura no afecta la original. Esa conclusión no se extiende automáticamente a listas de listas.

## Código completo

Archivo: [main.py](main.py).

```python
def aumentar_local(numero):
    numero += 1
    return numero

def agregar(datos):
    datos.append(8)

if __name__ == "__main__":
    numero = 4
    print(aumentar_local(numero), numero)
    datos = [4]
    agregar(datos)
    copia = datos.copy()
    copia.append(2)
    print(datos)
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
5 4
[4, 8]
[4, 8, 2]
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Traza asociaciones antes y después de la llamada. Ejecuta. Captura el retorno de aumentar_local. Haz una copia y modifica su estructura. Explica qué comparte una copia superficial de una matriz.

## Errores que conviene detectar

- Confundir reasignar el nombre local con modificar el objeto compartido.
- Creer que una copia superficial independiza elementos mutables anidados.

## Ejercicio para resolver

Escribe una función que devuelva una lista nueva con un elemento añadido y conserve la original.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

def con_elemento(datos,elemento): return datos + [elemento]. Crea nueva lista exterior. Prueba datos=[4], nueva=con_elemento(datos,8): datos sigue[4] y nueva es[4,8]. Elementos mutables interiores seguirían compartidos.

</details>

## Preguntas de comprensión

¿Reasignar un parámetro cambia el nombre externo? ¿Qué significa mutable? ¿Una copia superficial independiza todos los niveles?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/14-funciones-y-contratos/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/16-recursion/README.md)
