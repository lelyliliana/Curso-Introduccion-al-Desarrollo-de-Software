# Taller 3. Inventario y movimientos ficticios

[Inicio](../README.md) · [Unidad 3](../unidad-3/README.md) · [Proyecto](../unidad-3/19-proyecto-integrador/README.md) · [Siguiente recurso](../docs/cierre.md)

## Situación

Amplía el inventario del proyecto para consultar kits por fragmento de nombre y registrar una salida de unidades. Todos los movimientos son ficticios. La cantidad solicitada debe ser entero positivo, el código debe existir y la cantidad no debe superar la disponible. Un rechazo debe conservar el estado.

## Actividades

1. Escribe los contratos de filtrar_por_nombre y retirar. Define qué pasa con filtro vacío y diferencias de mayúsculas.
2. Diseña pruebas de código ausente, cantidad cero, negativa, no entera y superior a disponibilidad. Incluye un retiro exacto que deje cero.
3. Implementa el filtrado produciendo registros independientes. No expongas los diccionarios internos mutables.
4. Implementa retirar fuera del menú. Valida antes de modificar y conserva la estructura de registros.
5. Añade opciones de menú y mensajes comprensibles. Captura solo los errores esperados en la interacción.
6. Verifica que guardar y cargar conservan los nuevos valores. Ensaya un archivo con duplicado y otro con cantidad negativa sin sustituir datos activos.
7. Escribe pruebas automatizadas de la ampliación y ejecuta las existentes.
8. Documenta instalación, ejecución, reglas, ejemplos, formato y limitaciones. Explica por qué no equivale a un sistema de préstamos reales.
9. Evalúa el costo de filtrar y retirar. Declara un modelo de tamaño de textos y acceso al diccionario.

## Prueba de escritorio de retiro

| Solicitud sobre K01 con4 | Resultado | Unidades posteriores |
|---|---|---|
| Retirar2 | Éxito | 2 |
| Retirar3 | Rechazo | 2 |
| Retirar0 | Rechazo | 2 |
| Retirar2 | Éxito | 0 |

Cada fila comienza con el estado producido por la anterior. No vuelvas a inicializar4 sin aclararlo.

<details>
<summary>Solución orientativa de las reglas</summary>

```python
def retirar(inventario, codigo, cantidad):
    if type(cantidad) is not int or cantidad <= 0:
        raise ValueError("Cantidad entera positiva requerida")
    if codigo not in inventario:
        raise ValueError("Código inexistente")
    actual = inventario[codigo]["unidades"]
    if cantidad > actual:
        raise ValueError("Disponibilidad insuficiente")
    inventario[codigo]["unidades"] = actual - cantidad


def filtrar_por_nombre(inventario, fragmento):
    if not isinstance(fragmento, str) or not fragmento.strip():
        raise ValueError("Fragmento no vacío requerido")
    clave = fragmento.strip().casefold()
    return {
        codigo: registro.copy()
        for codigo, registro in inventario.items()
        if clave in registro["nombre"].casefold()
    }
```

Estas funciones suponen un inventario válido, como el construido por alta/cargar. La versión final debe conservar la validación de código textual y su normalización del proyecto. casefold facilita comparación sin distinción de mayúsculas, pero no elimina acentos ni resuelve todas las necesidades lingüísticas. Sensores coincide con SEN; Sensor y Cables no se vuelven equivalentes.

Retirar tiene acceso O(1) promedio con claves de tamaño acotado y aritmética tratada como operación elemental. Filtrar visita n registros y además procesa sus textos: no basta declarar O(n) si la longitud puede crecer sin límite. Con una longitud máxima acotada puede modelarse O(n). Guardar sigue ordenando códigos, por lo que conserva su costo O(n log n) bajo ese modelo.

La salida no registra solicitante, fecha ni préstamo activo; por eso no permite reconstruir préstamos. Para esa ampliación harían falta nuevas entidades, reglas, pruebas y decisiones de privacidad.

</details>

## Entrega y autoevaluación

Entrega contratos, código, prueba de escritorio, pruebas y guía. Revisa: análisis y contratos20%; reglas y conservación del estado30%; pruebas25%; documentación y uso15%; costos y límites10%. No basta una captura del menú: incluye casos que demuestren comportamiento ante errores.
