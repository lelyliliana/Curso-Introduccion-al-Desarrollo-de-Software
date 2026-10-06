# Ambiente para Ubuntu, Windows y macOS

[Inicio](../README.md) · [Siguiente recurso](../unidad-1/01-sistemas-y-entorno/README.md)

## Requisitos

Python 3.10 o posterior, una terminal y un editor de texto. Las prácticas usan la biblioteca estándar; no hay que ejecutar pip install. Puedes usar un editor sencillo o VS Code con su extensión de Python. Primero comprueba la ejecución en terminal para saber qué intérprete estás utilizando.

Descarga versiones estables de [Python](https://www.python.org/downloads/). Los programas del curso funcionan con versiones recientes sin depender de una versión menor exacta. Las pruebas automáticas usan 3.12 y 3.14.

## Windows (PowerShell)

1. Visita la [página oficial para Windows](https://www.python.org/downloads/windows/). El gestor de instalación de Python permite instalar versiones y proporciona los comandos python y py. Sigue su instalador para tu equipo.
2. Si usas el gestor y todavía no has instalado un intérprete, abre PowerShell y usa:

```powershell
py install 3.14
```

3. Cierra y abre la terminal y comprueba:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

Si ya tienes una instalación anterior válida, no hace falta cambiarla para el curso. Algunos equipos ofrecen `py -3` en lugar de `python`; verifica con `py -3 --version` y sustituye el comando en las prácticas. Con el gestor nuevo puedes consultar versiones con `py list`. Para problemas de alias o instalaciones simultáneas, consulta la [guía oficial de Windows](https://docs.python.org/3/using/windows.html).

4. Descomprime el ZIP del curso. Entra en una lección y ejecuta:

```powershell
cd "C:\ruta\Curso-Introduccion-al-Desarrollo-de-Software\unidad-3\04-python-y-ejecucion"
python main.py
```

`C:\ruta` es un marcador que debes reemplazar por tu carpeta real. No lo copies literalmente. Evita archivos guardados como main.py.txt: activa la visualización de extensiones en el explorador.

## Ubuntu

Comprueba primero si ya tienes una versión compatible:

```bash
python3 --version
```

Si falta el intérprete, instala el de los repositorios de tu distribución:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

La versión disponible depende de tu versión de Ubuntu. Si es anterior a 3.10, utiliza una versión de Ubuntu con soporte y un intérprete compatible. No sustituyas manualmente el Python del sistema ni uses sudo pip para este curso.

Si descomprimiste el curso en Descargas, ejecuta:

```bash
cd ~/Descargas/Curso-Introduccion-al-Desarrollo-de-Software
cd unidad-3/04-python-y-ejecucion
python3 main.py
```

Si tu carpeta está en otro lugar, utiliza esa ruta. Para nombres con espacios, entrecomilla la ruta completa usando su ruta absoluta.

## macOS

1. Descarga el instalador estable para macOS desde [Python](https://www.python.org/downloads/macos/). Comprueba compatibilidad del instalador con tu versión de macOS y el procesador del equipo.
2. Instala y abre otra terminal.
3. Comprueba:

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

4. Entra en la carpeta descomprimida y ejecuta:

```bash
cd ~/Downloads/Curso-Introduccion-al-Desarrollo-de-Software/unidad-3/04-python-y-ejecucion
python3 main.py
```

No dependas de un intérprete que el sistema incluya para sus propias herramientas. Usa la instalación compatible que verificaste.

## Archivos, rutas y codificación

Guarda el código como UTF-8. No añadas los indicadores >>> de la consola interactiva a los archivos. Las rutas relativas se interpretan desde la carpeta actual de la terminal. El proyecto usa pathlib y escribe explícitamente UTF-8; sus nombres de carpeta no dependen del sistema operativo.

Si los acentos se presentan incorrectamente, revisa la codificación del archivo y de la terminal. Para comprobar la salida UTF-8 del intérprete puedes ejecutar `python -X utf8 main.py` (Windows) o `python3 -X utf8 main.py` (Ubuntu/macOS) y usar una terminal que interprete UTF-8. Las pruebas automáticas fijan UTF-8 para evitar diferencias de captura.

## Entorno virtual opcional

El curso no necesita paquetes externos. Si deseas practicar aislamiento sin activar scripts de PowerShell:

Windows:

```powershell
python -m venv .venv
.venv\Scripts\python.exe main.py
```

Ubuntu/macOS:

```bash
python3 -m venv .venv
.venv/bin/python main.py
```

Ejecuta esos comandos en una carpeta con main.py. No incluyas .venv en tu repositorio.

## Git opcional

Puedes descargar ZIP sin instalar Git. Si usas Git, consulta su [instalación oficial](https://git-scm.com/downloads). Para configurar la identidad de tus commits:

```bash
git config --global user.name "Tu nombre"
git config --global user.email "Tu correo para commits"
```

Sustituye los marcadores por la identidad que deseas publicar en tu historial. Si quieres preservar privacidad, GitHub ofrece una dirección de correo de privacidad en sus ajustes. La configuración no inicia sesión ni concede permisos a un repositorio.
