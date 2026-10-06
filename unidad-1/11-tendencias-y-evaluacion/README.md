# Tendencias tecnológicas y evaluación crítica

[Recurso anterior](../../unidad-1/10-versiones-pruebas-y-calidad/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/12-caso-integrador-de-ingenieria/README.md)

## Objetivo

Evaluar una tecnología por necesidad, evidencia y limitaciones.

## Conceptos y explicación

Las tendencias cambian; una lista de predicciones de un año no debe presentarse como estado permanente del sector. Para este curso se estudian líneas de trabajo y criterios de evaluación: composición de servicios, automatización, confianza en sistemas algorítmicos, plataformas de cómputo, aprendizaje automático y digitalización inclusiva.

Las arquitecturas compuestas combinan componentes mediante interfaces. Microservicios, aplicaciones monolíticas modulares y servicios administrados son opciones con costos diferentes. Distribuir un sistema introduce fallos de red, coordinación y observabilidad; no lo hace automáticamente mejor. La confianza algorítmica requiere resultados evaluados, trazabilidad y manejo de errores, no solo publicidad del proveedor.

Más allá del silicio se investigan y desarrollan distintas tecnologías de cómputo. No se asume que una reemplazará de inmediato todas las computadoras. La inteligencia artificial puede apoyar clasificación y generación, pero sus resultados requieren evaluación; capacidad de generar texto no equivale a comprender requisitos ni garantiza corrección del código. Digitalizar incluye acceso, habilidades, conectividad y accesibilidad, además de colocar formularios en línea.

## Caso resuelto paso a paso

La biblioteca considera un clasificador automático de solicitudes. Antes de adoptarlo, define necesidad: reducir tiempo de clasificación sin omitir solicitudes válidas.

| Pregunta | Evidencia |
|---|---|
| ¿Mejora una regla sencilla? | Comparación con una línea base |
| ¿Qué errores comete? | Falsos positivos y negativos |
| ¿Qué datos utiliza? | Inventario y origen de datos |
| ¿Quién corrige resultados? | Flujo de revisión humana |
| ¿Cuánto cuesta mantenerlo? | Operación, cambios y capacitación |

La primera versión puede usar categorías elegidas por el usuario; no siempre necesita un modelo predictivo.

## Práctica guiada

Define la necesidad antes de nombrar la tecnología. Identifica una alternativa simple. Propón evaluación con datos ficticios. Escribe limitaciones y condiciones de retiro. Incluye consecuencias para usuarios que no pueden acceder fácilmente.

## Errores que conviene detectar

- Presentar predicciones de un año como hechos permanentes.
- Añadir servicios distribuidos sin analizar sus fallos de comunicación.

## Ejercicio para resolver

Evalúa «migrar el inventario a microservicios porque es moderno». Escribe dos preguntas y una alternativa.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Preguntas: ¿qué problemas de escala o autonomía existen? ¿quién operará la comunicación y los fallos entre servicios? Alternativa: aplicación modular local o un servicio sencillo, cuya complejidad corresponde al tamaño del inventario.

</details>

## Preguntas de comprensión

¿Una tendencia justifica una compra? ¿Qué significa línea base? ¿Cómo participa la inclusión en una decisión técnica?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/10-versiones-pruebas-y-calidad/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/12-caso-integrador-de-ingenieria/README.md)
