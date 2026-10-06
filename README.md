# Introducción al Desarrollo de Software

Curso para estudiar fundamentos de ingeniería de sistemas, representación numérica, álgebra booleana y programación con Python. El recorrido combina explicaciones, casos resueltos, ejercicios, soluciones y un proyecto local de inventario de kits.

## Ruta de aprendizaje

1. [Unidad 1. Introducción a la ingeniería de sistemas](unidad-1/README.md): sistemas, ingeniería, responsabilidades, proceso, modelos, dominios, herramientas y evaluación de tecnologías.
2. [Unidad 2. Sistemas de numeración y álgebra booleana](unidad-2/README.md): decimal, binario, octal, hexadecimal, operaciones, representación con signo, expresiones, Karnaugh y compuertas.
3. [Unidad 3. Introducción a la programación](unidad-3/README.md): solución de problemas, Python, variables, tipos, operadores, decisiones, ciclos, funciones, recursión, listas y diccionarios.

El orden conserva los tres ejes del programa y desarrolla sus temas con explicaciones originales y herramientas actuales. La primera unidad se trabaja con casos y modelos; las otras incluyen programas ejecutables. No necesitas haber programado antes.

## Cómo empezar

Lee [cómo estudiar](docs/como-estudiar.md) y la [guía de ambiente para Ubuntu, Windows y macOS](docs/ambiente-y-herramientas.md). Puedes descargar el repositorio como ZIP (botón Code → Download ZIP) y descomprimirlo, o clonarlo con Git.

```bash
git clone https://github.com/lelyliliana/Curso-Introduccion-al-Desarrollo-de-Software.git
cd Curso-Introduccion-al-Desarrollo-de-Software
```

Comienza por el [primer recurso](unidad-1/01-sistemas-y-entorno/README.md). Cada lección enlaza el recurso anterior, su índice y el siguiente recurso.

## Recursos del curso

- [Mapa de unidades y temas](docs/mapa-de-contenidos.md).
- [Convenciones de pseudocódigo y lógica](docs/convenciones.md).
- [Glosario](docs/glosario.md).
- [Fuentes de consulta](docs/fuentes.md).
- Talleres: [unidad 1](talleres/unidad-1.md), [unidad 2](talleres/unidad-2.md), [unidad 3](talleres/unidad-3.md).
- [Proyecto integrador](unidad-3/19-proyecto-integrador/README.md).
- [Verificación y pruebas](docs/verificacion.md).
- [Cierre del curso](docs/cierre.md).

## Prácticas y compatibilidad

El código usa Python 3.10 o posterior y su biblioteca estándar. No requiere paquetes externos. Las comprobaciones automáticas del repositorio usan Python 3.12 y 3.14 en Ubuntu, Windows y macOS. Usa una versión estable compatible; evita versiones preliminares para las prácticas.

Para comprobar ejemplos, pruebas y enlaces desde la raíz:

Windows:

```powershell
python scripts/verificar.py
```

Ubuntu/macOS:

```bash
python3 scripts/verificar.py
```

## Autoría

Material educativo de Lely Liliana Díaz Izquierdo. Los datos de los ejercicios son ficticios. Las referencias externas se identifican en las fuentes; las explicaciones y prácticas del repositorio se desarrollan como material propio del curso.
