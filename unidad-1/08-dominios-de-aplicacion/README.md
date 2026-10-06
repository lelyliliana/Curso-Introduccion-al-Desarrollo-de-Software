# Dominios de aplicación del software

[Recurso anterior](../../unidad-1/07-modelamiento/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/09-herramientas-y-entorno/README.md)

## Objetivo

Clasificar software por propósito y reconocer categorías que se superponen.

## Conceptos y explicación

El dominio de aplicación es el contexto de problemas, usuarios, reglas y necesidades que atiende el software. Clasificar ayuda a identificar restricciones, pero las categorías no son compartimentos exclusivos. Una aplicación web puede usar inteligencia artificial y formar parte de una línea de productos.

El software de sistema proporciona servicios para otros programas y administra recursos: sistemas operativos, controladores y componentes de infraestructura. El software de aplicación atiende tareas de usuarios. El científico y de ingeniería apoya cálculos, simulación y análisis, cuya validez depende también del modelo y de los datos. El embebido o integrado opera dentro de un dispositivo y puede tener límites de memoria, energía o tiempo de respuesta.

Una línea de productos comparte activos y variaciones planificadas; no basta con copiar carpetas para cada cliente. Web y móvil describen plataformas o formas de acceso. La inteligencia artificial describe técnicas, no una garantía de exactitud. Algunos sistemas tienen requisitos de tiempo real: cumplir un plazo forma parte de la corrección, no significa simplemente «muy rápido».

## Caso resuelto paso a paso

| Software | Categoría principal | Restricción relevante |
|---|---|---|
| Controlador de impresora | Sistema | Compatibilidad con equipo y sistema operativo |
| Catálogo de kits | Aplicación | Integridad de códigos y cantidades |
| Simulador de circuitos | Científico/ingeniería | Exactitud del modelo y tolerancias |
| Control de temperatura | Embebido | Tiempo de respuesta y energía |
| Catálogos con opciones por sede | Línea de productos | Variaciones y pruebas compartidas |
| Consulta desde navegador | Web | Accesibilidad y comunicación |
| Clasificador de solicitudes | Inteligencia artificial | Evaluación de errores y datos |

El catálogo puede pertenecer simultáneamente a aplicación, web y línea de productos.

## Práctica guiada

Identifica usuarios y tarea. Propón una categoría principal y otra compatible. Define una restricción derivada del dominio. Escribe una prueba o medición que la examine.

## Errores que conviene detectar

- Clasificar web e inteligencia artificial como categorías incompatibles.
- Confundir «tiempo real» con un tiempo de ejecución simplemente pequeño.

## Ejercicio para resolver

Clasifica una aplicación móvil que reconoce imágenes de plantas y envía resultados a investigadores. Explica por qué el resultado necesita evaluación.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Es móvil por acceso, aplicación por tarea e inteligencia artificial por clasificación; puede apoyar trabajo científico. La identificación puede equivocarse. Se requiere un conjunto de evaluación, tipos de error y revisión de resultados antes de decisiones importantes.

</details>

## Preguntas de comprensión

¿Dominio y lenguaje son lo mismo? ¿Toda aplicación embebida es de tiempo real? ¿Copiar código produce una línea de productos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/07-modelamiento/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/09-herramientas-y-entorno/README.md)
