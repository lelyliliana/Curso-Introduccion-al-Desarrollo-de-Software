# Modelos de desarrollo y adaptación

[Recurso anterior](../../unidad-1/04-proceso-de-software/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/06-agilidad-y-entregas/README.md)

## Objetivo

Comparar enfoques secuenciales, incrementales, iterativos y orientados al riesgo.

## Conceptos y explicación

Un modelo representa una manera de organizar el desarrollo. El modelo secuencial sitúa actividades en una secuencia con entregables y revisiones. Puede ser útil con requisitos estables y acuerdos definidos, pero el costo de descubrir tarde una necesidad puede ser alto. No significa que sea físicamente imposible retroceder.

**Incremental** agrega capacidades en entregas: primero consulta, después registro, luego reportes. **Iterativo** revisa y mejora una solución: se ajusta la misma consulta después de observar su uso. Ambos pueden combinarse. El prototipado reduce incertidumbre; un prototipo exploratorio no debería publicarse como producto terminado sin evaluar lo que le falta.

El enfoque en espiral organiza ciclos alrededor de objetivos, alternativas y riesgos. No es simplemente «hacer cascada muchas veces». La selección del proceso depende de incertidumbre, criticidad, personas y restricciones. Ningún modelo garantiza calidad por sí solo. La seguridad y las pruebas se integran al enfoque elegido, no se dejan necesariamente para el final.

## Caso resuelto paso a paso

Entrega 1 consulta stock ficticio. Entrega 2 registra préstamos. Entrega 3 permite devolver. Eso es crecimiento incremental. Después de la entrega 1 se cambia «cantidad» por «unidades disponibles» y se mejora la búsqueda: esa revisión es iterativa.

Riesgo prioritario: pérdida del inventario al reiniciar. Antes de añadir gráficos, se ensaya guardar y restaurar datos. Una interfaz atractiva sin recuperación no reduce ese riesgo.

## Práctica guiada

Ordena capacidades por valor. Identifica la mayor incertidumbre. Elige una entrega que produzca aprendizaje. Escribe qué revisarás en la iteración siguiente y qué resultado esperas del experimento de riesgo.

## Errores que conviene detectar

- Llamar incremental a cualquier revisión de la misma capacidad.
- Usar un prototipo exploratorio como versión terminada sin revisar riesgos.

## Ejercicio para resolver

Compara un prototipo desechable de interfaz con una primera versión evolutiva del inventario. Indica qué se conservaría y qué se comprobaría antes de uso real.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

El desechable prueba vocabulario y flujo; su código puede no mantenerse. La versión evolutiva necesita reglas claras, pruebas y control de cambios. En ambos casos se revisan datos, seguridad, recuperación y necesidades pendientes antes de uso real.

</details>

## Preguntas de comprensión

¿Una entrega puede ser incremental e iterativa? ¿Qué riesgo aparece al confundir prototipo con producto? ¿Por qué no existe un modelo ideal para todos los proyectos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/04-proceso-de-software/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/06-agilidad-y-entregas/README.md)
