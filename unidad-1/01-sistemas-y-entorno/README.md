# Sistemas, límites y entorno

[Recurso anterior](../../docs/como-estudiar.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/02-ingenieria-y-decisiones/README.md)

## Objetivo

Delimitar un sistema e identificar entradas, transformaciones, salidas y retroalimentación.

## Conceptos y explicación

Un sistema es un conjunto de elementos relacionados que produce un comportamiento conjunto. Sus elementos pueden ser personas, reglas, información, software y equipos. La aplicación que vemos en una pantalla es solamente una parte de muchos sistemas de información. Una biblioteca también necesita responsables, procedimientos y lectores.

El **límite** señala qué se estudia o controla. El **entorno** contiene factores externos con los que se intercambia información o recursos. Cambiar el límite cambia el análisis: una impresora puede ser parte del sistema de préstamo o un servicio externo. Las entradas son datos o recursos recibidos; las salidas son resultados. La retroalimentación usa información sobre el resultado para ajustar decisiones posteriores. Una lista de componentes sin relaciones todavía no explica el sistema.

Un sistema abierto intercambia con su entorno. Un sistema cerrado es una idealización útil en ciertos modelos, no una característica automática de todo programa. La disponibilidad del software tampoco garantiza que el servicio completo funcione: puede faltar energía, capacitación o una regla clara para devolver materiales.

## Caso resuelto paso a paso

Una biblioteca presta kits electrónicos. El sistema abarca recepción de solicitudes, autorización, entrega y devolución. El proveedor de kits queda fuera del límite.

| Elemento | Ejemplo | Relación |
|---|---|---|
| Entrada | Identificador del kit y solicitud | Permite buscar disponibilidad |
| Transformación | Validar y registrar préstamo | Cambia el estado del kit |
| Salida | Comprobante y kit entregado | Informa quién debe devolverlo |
| Retroalimentación | Devoluciones atrasadas | Permite ajustar recordatorios |
| Entorno | Calendario académico | Modifica horarios de atención |

Si el sistema cuenta kits pero no registra préstamos, su cifra de disponibles deja de representar la realidad. El problema está en la relación entre actividades, aunque cada pantalla funcione.

## Práctica guiada

Dibuja el límite. Sitúa responsables y datos dentro de él. Conecta solicitud, entrega y devolución. Identifica un evento externo que pueda interrumpir el servicio. Explica qué dato permitiría detectar el problema.

## Errores que conviene detectar

- Describir la biblioteca solamente como su programa e ignorar personas y procedimientos.
- Confundir el informe de atrasos con la devolución física: son relaciones distintas.

## Ejercicio para resolver

Modela un sistema de reserva de salas. Identifica dos entradas, dos salidas, un responsable y un mecanismo de retroalimentación. Describe qué ocurre si una reserva no se cancela cuando el usuario deja de necesitarla.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

La solicitud y el horario son entradas; la confirmación y la agenda son salidas. El responsable administra conflictos. La medición de reservas no utilizadas permite mejorar recordatorios. La cancelación libera el intervalo, por lo que debe actualizar la agenda y no solo enviar un correo.

</details>

## Preguntas de comprensión

¿Qué cambia al incluir el proveedor dentro del límite? ¿Puede funcionar el programa y fallar el sistema? ¿Qué diferencia hay entre salida y retroalimentación?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../docs/como-estudiar.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/02-ingenieria-y-decisiones/README.md)
