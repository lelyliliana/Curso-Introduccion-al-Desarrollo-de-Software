from pathlib import Path
import json
import os
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ENV = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")

def ejecutar(comando, carpeta, entrada=""):
    return subprocess.run(comando, cwd=carpeta, input=entrada, capture_output=True, text=True, encoding="utf-8", env=ENV, timeout=60)

def normalizar(texto):
    return texto.replace("\r\n", "\n").rstrip("\n")

def main():
    manifest = json.loads((ROOT / "scripts/manifest.json").read_text(encoding="utf-8"))
    for item in manifest:
        carpeta = ROOT / item["path"]
        with tempfile.TemporaryDirectory() as temporal:
            proceso = ejecutar([sys.executable, "-X", "utf8", str(carpeta / "main.py")], temporal, item["input"])
        esperado = (carpeta / "esperado.txt").read_text(encoding="utf-8")
        if proceso.returncode or normalizar(proceso.stdout) != normalizar(esperado):
            raise RuntimeError(f"Ejemplo {item['path']}\nEsperado:\n{esperado}\nObtenido:\n{proceso.stdout}\nError:\n{proceso.stderr}")
    print(f"Ejemplos comprobados: {len(manifest)}")
    pruebas = ejecutar([sys.executable, "-X", "utf8", "-m", "unittest", "discover", "-s", "tests", "-v"], ROOT)
    print(pruebas.stderr, end="")
    if pruebas.returncode:
        raise RuntimeError("Fallaron las pruebas automatizadas")
    enlaces = 0
    for archivo in ROOT.rglob("*.md"):
        texto = archivo.read_text(encoding="utf-8")
        # Los enlaces se revisan fuera de bloques de código.
        texto = re.sub(r"```.*?```", "", texto, flags=re.S)
        for destino in re.findall(r"\[[^\]]*\]\(([^)]+)\)", texto):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", destino) or destino.startswith("#"):
                continue
            ruta = unquote(destino.split("#", 1)[0])
            if ruta and not (archivo.parent / ruta).exists():
                raise RuntimeError(f"Enlace inválido en {archivo.relative_to(ROOT)}: {destino}")
            enlaces += 1
    print(f"Enlaces locales comprobados: {enlaces}")
    print("Verificación completa")

if __name__ == "__main__":
    main()
