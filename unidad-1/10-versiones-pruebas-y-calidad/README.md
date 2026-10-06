# Control de versiones, pruebas y calidad

[Recurso anterior](../../unidad-1/09-herramientas-y-entorno/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/11-tendencias-y-evaluacion/README.md)

## Objetivo

Relacionar cambios pequeños, pruebas y revisión con un historial comprensible.

## Conceptos y explicación

Git registra versiones de archivos y sus relaciones. GitHub aloja repositorios y ofrece colaboración; son productos distintos. Un commit reúne cambios con un propósito. Una rama permite desarrollar una línea de trabajo sin modificar inmediatamente otra. Un historial útil contiene cambios revisables y mensajes que explican el resultado.

Antes de confirmar, inspecciona el estado y la diferencia. No añadas contraseñas, archivos personales, entornos virtuales ni resultados generados. El repositorio contiene código, ejemplos ficticios y documentación. Un respaldo y un historial cumplen funciones diferentes: el historial no sirve de respaldo si solo existe en el mismo disco que se pierde.

Una prueba define entradas, resultado esperado y comparación. La prueba unitaria revisa una unidad pequeña; la integración revisa interacción; una prueba de aceptación revisa una condición del usuario. La automatización aumenta repetibilidad, pero las pruebas disponibles no prueban ausencia de todos los defectos. La integración continua ejecuta comprobaciones cuando se incorporan cambios.

## Caso resuelto paso a paso

En una copia descargada del curso, estos comandos solo inspeccionan:

```bash
git status
git diff
git log --oneline -5
```

Para iniciar un ejercicio propio en una carpeta nueva:

```bash
git init
git add main.py
git commit -m "Validar unidades antes de registrar un kit"
```

Configura tu identidad Git antes del primer commit según la guía. El archivo `.gitignore` evita incluir cachés de Python y salidas generadas. Una prueba de cantidad -1 debe fallar con un error de validación, no almacenarla silenciosamente.

## Práctica guiada

Inspecciona archivos cambiados. Revisa una diferencia línea por línea. Ejecuta pruebas relacionadas. Selecciona archivos explícitos. Escribe un mensaje con el comportamiento resultante y confirma. Consulta el historial para comprobar el registro.

## Errores que conviene detectar

- Confundir Git con GitHub o historial local con respaldo externo.
- Confirmar archivos sin inspeccionar la diferencia.

## Ejercicio para resolver

Propón un commit que cambie validación de cantidad y otro que cambie formato de reportes. Justifica separarlos y define una prueba para el primero.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Son propósitos distintos, y separarlos facilita revisar o revertir. La validación se prueba con -1, 0 y 1: rechazar solo el negativo. El reporte puede revisarse con una salida esperada independiente.

</details>

## Preguntas de comprensión

¿Un commit remoto sustituye todos los respaldos? ¿Qué detecta git diff? ¿Una prueba positiva cubre datos inválidos?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/09-herramientas-y-entorno/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-1/11-tendencias-y-evaluacion/README.md)
