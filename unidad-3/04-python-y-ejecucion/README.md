# Python: archivos, intérprete y primer programa

[Recurso anterior](../../unidad-3/03-pruebas-depuracion-y-mantenimiento/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/05-variables-y-asignacion/README.md)

## Objetivo

Ejecutar y modificar un programa Python guardado en UTF-8.

## Conceptos y explicación

Python es un lenguaje de propósito general con tipos dinámicos y varias formas de organizar programas. En el curso se empieza con programación estructurada y funciones. Los tipos pertenecen a los objetos; un nombre puede asociarse a objetos distintos, aunque cambiar arbitrariamente su significado dificulta leer el programa.

Un archivo .py guarda código fuente. La consola interactiva permite probar expresiones y suele mostrar el indicador >>>; ese indicador no se copia a un archivo. Ejecutar un archivo y escribir una expresión en la consola no producen exactamente la misma presentación: en un archivo se usa print para mostrar algo.

La indentación delimita bloques. Se usan cuatro espacios por nivel y se evita mezclar tabulaciones con espacios. Los comentarios explican una decisión del código cuando hace falta. El código del curso se guarda como UTF-8 y utiliza f-strings para construir mensajes. El comando específico para lanzar Python está en la guía de ambiente.

## Caso resuelto paso a paso

El programa define nombre y unidades y construye un mensaje. Los caracteres acentuados muestran que el archivo se interpreta con su codificación esperada. No se requiere instalar paquetes.

| Elemento | Papel |
|---|---|
| nombre | Nombre asociado a texto |
| unidades | Nombre asociado a entero |
| print | Presentación en consola |
| f-string | Inserta valores en un texto |

El punto de partida es comprender qué ejecuta la terminal, antes de depender del botón de un editor.

## Código completo

Archivo: [main.py](main.py).

```python
nombre = "Sensores"
unidades = 4
print(f"Kit: {nombre}")
print(f"Unidades disponibles: {unidades}")
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
Kit: Sensores
Unidades disponibles: 4
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Abre main.py. Predice el mensaje. Ejecuta desde la carpeta. Cambia nombre y unidades y guarda. Ejecuta nuevamente. Comprueba que una expresión sola no se imprime automáticamente en un archivo.

## Errores que conviene detectar

- Copiar el indicador >>> dentro del archivo .py.
- Ejecutar una copia distinta o no guardar el archivo modificado.

## Ejercicio para resolver

Crea un programa que muestre el nombre de una sala ficticia y su capacidad, primero en una línea y después en dos.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Usa sala="Laboratorio A" y capacidad=12. print(f"{sala}: {capacidad} puestos") produce una línea. Dos llamadas print separan nombre y capacidad. Conserva capacidad como entero para poder operar con ella.

</details>

## Preguntas de comprensión

¿Qué diferencia hay entre consola y archivo? ¿Qué delimita un bloque? ¿Por qué guardar antes de ejecutar?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/03-pruebas-depuracion-y-mantenimiento/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/05-variables-y-asignacion/README.md)
