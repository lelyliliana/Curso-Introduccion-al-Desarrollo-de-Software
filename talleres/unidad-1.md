# Taller 1. Diseño de un sistema de reserva de salas

[Inicio](../README.md) · [Unidad 1](../unidad-1/README.md) · [Siguiente recurso](../unidad-2/01-valor-posicional/README.md)

## Situación

Un espacio de aprendizaje tiene salas A y B. Las reservas son por bloques identificados: mañana y tarde. Se usan códigos ficticios de solicitantes. Una misma sala no puede tener dos reservas activas en un bloque. Cancelar libera el bloque. La primera versión se utilizará localmente por una persona; la conexión puede fallar.

## Objetivo

Producir una especificación breve que un equipo pueda implementar y comprobar. No se requiere programar todavía.

## Actividades

1. Delimita el sistema. Identifica personas, datos, reglas, equipos y entorno. Distingue la aplicación del servicio completo.
2. Formula el problema sin mencionar una herramienta. Describe una consecuencia del conflicto de reservas.
3. Define cinco requisitos identificados R1..R5. Incluye existencia de sala, bloques válidos, conflicto, cancelación y consulta.
4. Para cada requisito escribe un caso normal, uno límite o inválido y su resultado esperado.
5. Modela estados de reserva: activa/cancelada. Declara si una cancelada puede reactivarse y cómo afecta disponibilidad.
6. Compara una hoja local, una aplicación local y una web con los mismos criterios. Justifica la selección y un supuesto que puede cambiarla.
7. Propón tres entregas pequeñas. Incluye pruebas y documentación en las condiciones de terminado.
8. Asigna responsabilidades de análisis, desarrollo, pruebas y operación. Señala una decisión de privacidad y otra de accesibilidad.
9. Evalúa una propuesta de «usar un clasificador automático para aceptar reservas». Define qué necesidad atendería y qué alternativa simple existe.

## Plantilla de entrega

Presenta: problema y alcance; tabla de entradas/salidas; requisitos y casos; modelo; comparación de alternativas; plan de entregas; riesgos y revisión de decisiones. La extensión debe permitir revisar todos los casos sin repetición innecesaria.

## Caso de prueba resuelto

| Paso | Solicitud | Estado esperado |
|---|---|---|
| 1 | Reservar A/mañana para P01 | Activa |
| 2 | Reservar A/mañana para P02 | Rechazo por conflicto |
| 3 | Cancelar reserva de P01 | Cancelada y bloque libre |
| 4 | Reservar A/mañana para P02 | Activa |
| 5 | Cancelar de nuevo la primera | Sin liberar la reserva de P02 |

El paso 5 evita que una cancelación repetida elimine un bloqueo distinto por error. La identidad de la reserva es importante, no solo sala y bloque.

<details>
<summary>Solución orientativa</summary>

R1 admite únicamente salas A y B; R2 admite mañana/tarde; R3 rechaza una segunda reserva activa de la misma pareja sala/bloque; R4 cancela por identificador de reserva y no altera otras; R5 consulta disponibilidad considerando solo reservas activas. Las entradas son sala, bloque y código ficticio; las salidas son confirmación, rechazo y agenda.

Un modelo simple hace activa → cancelada y trata cancelada como terminal. Una nueva reserva recibe otro identificador. La opción local evita depender de conectividad, pero exige respaldo y recuperación comprobables. Entregas: consulta de agenda, alta con conflictos y cancelación. Cada una incluye casos y mensajes claros; la última debe conservar la prueba de cancelación repetida.

No se necesitan nombres reales ni clasificación predictiva para validar dos salas y dos bloques. Mensajes textuales de estado permiten comprender el resultado sin depender de colores. Si luego operan varias sedes simultáneamente, se revisan concurrencia y arquitectura: la elección inicial puede dejar de servir.

</details>

## Autoevaluación

| Criterio | Peso |
|---|---|
| Sistema, alcance y problema claros | 20% |
| Requisitos y casos verificables | 30% |
| Modelo consistente | 20% |
| Alternativas, riesgos y entregas | 20% |
| Claridad y decisiones de uso | 10% |

Revisa que cada regla tenga evidencia y que las decisiones respondan a las restricciones del caso.
