# Caso integrador: requisitos de un inventario

[Recurso anterior](../../unidad-1/11-tendencias-y-evaluacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/01-valor-posicional/README.md)

## Objetivo

Producir una especificación pequeña, trazable y verificable.

## Conceptos y explicación

Un caso integrador une necesidad, alcance, reglas, modelos y pruebas. En este curso la primera unidad prepara la especificación; las siguientes aportan representación de datos, lógica e implementación. El documento debe permitir distinguir lo acordado de lo pendiente.

El alcance inicial incluye registrar kits, consultar por código y listar existencias. Se excluyen préstamos reales y datos personales: son ampliaciones futuras, no funciones escondidas. Un criterio de aceptación establece una situación, una acción y un resultado observable. La trazabilidad conecta ese criterio con una prueba y una función.

Las restricciones de la primera versión son operación local, datos ficticios, cantidades enteras no negativas y códigos únicos. La persistencia necesita un formato y una política para archivos inválidos. La definición de terminado incluye validación, pruebas y guía. Los límites explícitos evitan atribuir a un ejercicio educativo cualidades de un sistema de producción.

## Caso resuelto paso a paso

| ID | Regla | Criterio de aceptación |
|---|---|---|
| R1 | Código único | Segundo alta con K01 se rechaza |
| R2 | Cantidad no negativa | -1 se rechaza; 0 se acepta |
| R3 | Consulta por código | Inexistente informa ausencia |
| R4 | Persistencia | Guardar y cargar conserva registros |
| R5 | Carga consistente | Archivo inválido no sustituye datos activos |

Datos: K01, Sensores, 4; K02, Cables, 8. No se presupone una base de datos o una interfaz web. El proyecto final implementa esta versión con Python.

## Práctica guiada

Escribe problema y alcance. Asigna identificadores a reglas. Define datos válidos e inválidos. Añade modelo y pruebas. Revisa que cada requisito pueda comprobarse sin interpretar frases ambiguas.

## Errores que conviene detectar

- Escribir «debe funcionar bien» como criterio de aceptación.
- Dejar sin prueba la conservación de estado cuando falla una carga.

## Ejercicio para resolver

Agrega el requisito «actualizar cantidad» y sus criterios de aceptación. Indica qué archivo, función y prueba cambiarían en la implementación futura.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

R6 permite reemplazar cantidad de un código existente por entero no negativo. Pruebas: K01 a 0 conserva código y nombre; -1 se rechaza sin cambio; inexistente informa ausencia. Se cambia la función de actualización, el menú, la documentación y las pruebas relacionadas.

</details>

## Preguntas de comprensión

¿Por qué no prometer todas las funciones desde el inicio? ¿Qué demuestra la trazabilidad? ¿Qué regla garantiza la carga consistente?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/11-tendencias-y-evaluacion/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/01-valor-posicional/README.md)
