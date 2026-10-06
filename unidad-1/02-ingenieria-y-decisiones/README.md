# Ingeniería y decisiones con restricciones

[Recurso anterior](../../unidad-1/01-sistemas-y-entorno/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/03-disciplinas-y-responsabilidades/README.md)

## Objetivo

Justificar una solución considerando evidencia, costos y restricciones.

## Conceptos y explicación

La ingeniería diseña y mejora soluciones para necesidades concretas mediante conocimientos, modelos, experimentación y juicio. No consiste únicamente en construir objetos ni en usar una herramienta. Una decisión técnica debe explicar qué necesidad atiende, qué restricciones respeta y cómo se evaluará.

Las restricciones pueden ser presupuesto, plazo, conectividad, accesibilidad o seguridad. Los criterios permiten comparar opciones: facilidad de uso, recuperación de errores, costo de operación y mantenibilidad. Un criterio que solo dice «mejor calidad» es demasiado vago; debe traducirse en observaciones. Los criterios pueden entrar en conflicto: una solución muy flexible puede exigir más capacitación.

Un supuesto es una afirmación provisional, como «la conexión estará disponible». Un riesgo es un evento incierto con consecuencias. Registrar ambos permite revisar una elección si aparecen nuevas evidencias. El prototipo ayuda a aprender, pero su aceptación visual no demuestra capacidad, seguridad ni confiabilidad de la versión definitiva.

## Caso resuelto paso a paso

La biblioteca dispone de conexión intermitente y una persona para operar préstamos. Se comparan una hoja local, una aplicación local y un servicio web.

| Opción | Ventaja | Limitación | Evidencia necesaria |
|---|---|---|---|
| Hoja local | Inicio rápido | Edición accidental | Probar recuperación de una fila |
| Aplicación local | Reglas uniformes | Respaldo manual | Simular reinicio y restauración |
| Servicio web | Acceso compartido | Dependencia de conectividad | Medir interrupciones del sitio |

Se elige una primera aplicación local porque el servicio debe continuar sin red. La elección podría cambiar si se necesitan varias sedes. Esta conclusión es contextual, no una regla universal.

## Práctica guiada

Escribe la necesidad en una frase. Separa restricciones obligatorias y criterios deseables. Compara tres alternativas con la misma tabla. Ejecuta una prueba pequeña de la incertidumbre más importante. Registra la decisión y la condición que obligaría a revisarla.

## Errores que conviene detectar

- Comparar alternativas usando criterios diferentes para cada una.
- Afirmar que una copia existe sin haber probado su restauración.

## Ejercicio para resolver

Elige entre respaldo manual y automático para el inventario. Define dos criterios observables, un riesgo de cada alternativa y una prueba de restauración.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Criterios: tiempo para recuperar el archivo y pérdida máxima aceptable de cambios. El respaldo manual puede olvidarse; el automático puede copiar un archivo ya corrupto. Guarda versiones y restaura una copia en otra carpeta; compara cantidad de registros y datos, sin reemplazar primero el original.

</details>

## Preguntas de comprensión

¿Por qué una herramienta popular puede ser una mala elección? ¿Un supuesto confirmado elimina todos los riesgos? ¿Qué prueba distingue respaldo de recuperación?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/01-sistemas-y-entorno/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/03-disciplinas-y-responsabilidades/README.md)
