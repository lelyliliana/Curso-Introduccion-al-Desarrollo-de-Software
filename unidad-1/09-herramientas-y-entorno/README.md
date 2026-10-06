# Herramientas y entorno de desarrollo

[Recurso anterior](../../unidad-1/08-dominios-de-aplicacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/10-versiones-pruebas-y-calidad/README.md)

## Objetivo

Elegir herramientas por tarea y reproducir un entorno sencillo.

## Conceptos y explicación

Un editor modifica texto; un entorno integrado de desarrollo reúne edición, navegación, ejecución y depuración. El intérprete o entorno de ejecución permite ejecutar programas. Un compilador transforma una representación del programa en otra; un lenguaje puede tener implementaciones con diferentes combinaciones de compilación e interpretación. CPython normalmente compila a bytecode y lo ejecuta en su máquina virtual, por lo que «Python no compila» es una simplificación incorrecta.

Las herramientas apoyan tareas: modelado, construcción, pruebas, control de versiones, revisión y entrega. Las llamadas herramientas CASE asisten actividades de ingeniería de software, pero esa denominación no obliga a utilizar una suite específica. Instalar muchas herramientas no reemplaza comprender el problema.

Este curso usa Python 3 y su biblioteca estándar, un editor de texto y Git opcional para registrar avances. El mismo código se ejecuta en Ubuntu, Windows y macOS. El comando del intérprete puede cambiar; las rutas de los programas se construyen con pathlib cuando hace falta trabajar con archivos. No se escriben rutas personales como C:\Usuarios\nombre dentro de las reglas del programa.

## Caso resuelto paso a paso

| Necesidad | Herramienta | Comprobación |
|---|---|---|
| Editar | Editor de texto o VS Code | Archivo guardado como UTF-8 y .py |
| Ejecutar | Python 3 | Comando muestra versión y ejecuta archivo |
| Verificar | unittest | Pruebas pasan y detectan un error introducido |
| Historial | Git | Diferencia y registro del cambio visibles |
| Modelar | Markdown y Mermaid | Modelo coincide con reglas |

La guía de instalación ofrece comandos separados por sistema. Las prácticas no requieren una cuenta de pago ni paquetes externos.

## Práctica guiada

Lee la guía de ambiente. Comprueba la versión de Python. Crea una carpeta sin depender de rutas del ejemplo. Guarda un archivo .py y ejecútalo desde su carpeta. Modifica un mensaje y confirma que ejecutas la copia correcta.

## Errores que conviene detectar

- Confundir editor, intérprete y entorno integrado.
- Afirmar que CPython no realiza ninguna compilación.

## Ejercicio para resolver

Explica qué investigar cuando el editor muestra el código nuevo pero la terminal sigue mostrando el resultado anterior.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Comprueba que guardaste el archivo, que la terminal está en la carpeta correcta y que ejecutas el mismo nombre. Imprime temporalmente un mensaje distintivo. Revisa la ruta de la terminal antes de reinstalar herramientas.

</details>

## Preguntas de comprensión

¿Editor e intérprete son equivalentes? ¿Por qué no usar un archivo .py.txt? ¿Qué ventaja tiene un entorno sin dependencias externas?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/08-dominios-de-aplicacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/10-versiones-pruebas-y-calidad/README.md)
