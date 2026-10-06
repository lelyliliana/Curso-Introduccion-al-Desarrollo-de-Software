# Actividades y productos del proceso de software

[Recurso anterior](../../unidad-1/03-disciplinas-y-responsabilidades/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/05-modelos-de-desarrollo/README.md)

## Objetivo

Relacionar necesidades, planificación, modelado, construcción y despliegue.

## Conceptos y explicación

Un proceso de software organiza actividades para crear y evolucionar un producto. Incluye comprender necesidades, planificar, modelar, implementar, verificar y poner una versión en uso. Las actividades pueden repetirse y superponerse: descubrir un caso límite durante una prueba puede obligar a ajustar un requisito.

Una actividad tiene propósito amplio; una tarea es una acción concreta; un producto de trabajo es la evidencia resultante. «Hacer análisis» no indica cuándo termina el trabajo. «Escribir tres criterios de aceptación y revisarlos con un usuario» produce algo evaluable. El proceso debe ajustarse al tamaño y riesgo del proyecto; agregar documentos sin utilidad no lo vuelve más riguroso.

La gestión de cambios, la calidad y la seguridad atraviesan el proceso. **Verificación** contrasta el producto con su especificación; **validación** revisa si resuelve la necesidad en su contexto. Aprobar todas las pruebas escritas puede ser insuficiente si los requisitos olvidaron una situación real. El despliegue no cierra automáticamente el trabajo: hay incidencias, nuevas necesidades y mantenimiento.

## Caso resuelto paso a paso

Requisito R1: «Consultar la cantidad disponible de un kit».

| Actividad | Tarea concreta | Evidencia |
|---|---|---|
| Comunicación | Acordar significado de disponible | Regla: total menos préstamos activos |
| Planificación | Priorizar consulta antes de reportes | Lista de entregas |
| Modelado | Definir datos y estados | Tabla y diagrama |
| Construcción | Implementar y probar consulta | Código y pruebas |
| Despliegue | Ejecutar con datos ficticios | Guía y registro de resultados |

Una prueba de R1 exige que total 5 y préstamos 2 produzcan disponible 3. Una validación adicional observa si quien entrega kits comprende esa cifra.

## Práctica guiada

Formula un requisito. Escribe un criterio de aceptación medible. Enumera tareas que producen evidencias. Revisa la correspondencia requisito → diseño → implementación → prueba. Registra un cambio sin borrar su motivación.

## Errores que conviene detectar

- Confundir «hacer análisis» con un producto que pueda revisarse.
- Suponer que aprobar una especificación demuestra adecuación a la necesidad real.

## Ejercicio para resolver

Descompón «permitir devoluciones» en tareas y productos. Incluye un caso que pase verificación pero pueda fallar en uso.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Regla: solo devolver un préstamo activo. Productos: transición de estado, función y casos activo/inexistente/ya devuelto. Puede calcularse bien el stock pero el mensaje usar términos que el operador no entiende. La validación con usuarios detecta ese problema.

</details>

## Preguntas de comprensión

¿Por qué probar no es únicamente ejecutar? ¿Qué diferencia hay entre tarea y producto? ¿Qué se pierde al cambiar un requisito sin registrarlo?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/03-disciplinas-y-responsabilidades/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/05-modelos-de-desarrollo/README.md)
