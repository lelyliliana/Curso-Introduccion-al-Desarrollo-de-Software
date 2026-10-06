# Verificación del curso

[Inicio](../README.md) · [Siguiente recurso](cierre.md)

## Comprobación completa

Desde la raíz ejecuta `python scripts/verificar.py` en Windows o `python3 scripts/verificar.py` en Ubuntu/macOS. El script ejecuta cada práctica en una carpeta temporal, suministra las entradas reproducibles, compara las salidas esperadas, ejecuta las pruebas y comprueba enlaces locales de Markdown.

Se fija UTF-8 para la captura y se normalizan saltos CRLF/LF. Las carpetas temporales evitan que una práctica escriba dentro de otra. Un fallo devuelve un estado de error y explica la diferencia; no se modifica la salida esperada para ocultar un problema.

## Pruebas automatizadas

```bash
python -m unittest discover -s tests -v
```

En Ubuntu/macOS sustituye python por python3. Las pruebas revisan conversiones de0..1023, límites de complemento a dos, equivalencias booleanas, sumador completo, contratos de cantidades, clasificación, ciclos, recursión, registros, copias y persistencia. Incluyen archivos inválidos y un recorrido del menú.

La configuración de GitHub Actions ejecuta estas comprobaciones en Ubuntu, Windows y macOS con Python3.12 y3.14. Puedes consultar el resultado en la pestaña Actions del repositorio.

## Qué significa un resultado correcto

Las pruebas demuestran cumplimiento de los casos definidos, dentro de sus contratos. No garantizan ausencia de todos los defectos ni evalúan un circuito físico. Las explicaciones, modelos y casos manuales deben revisarse también. Cuando amplíes una regla, agrega casos y ejecuta las pruebas existentes para detectar regresiones.
