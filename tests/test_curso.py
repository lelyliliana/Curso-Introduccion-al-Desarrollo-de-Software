import copy
import importlib.util
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def modulo(ruta):
    archivo = ROOT / ruta / "main.py"
    spec = importlib.util.spec_from_file_location(ruta.replace("-", "_").replace("/", "_"), archivo)
    resultado = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resultado)
    return resultado

BIN = modulo("unidad-2/03-binario-y-conversion")
COMP = modulo("unidad-2/07-bits-signo-y-limites")
COSTO = modulo("unidad-3/01-analisis-del-problema")
REPARTO = modulo("unidad-3/02-diseno-y-algoritmos")
TOTAL = modulo("unidad-3/03-pruebas-depuracion-y-mantenimiento")
ENTRADA = modulo("unidad-3/06-entrada-y-validacion")
ESTADO = modulo("unidad-3/09-condicionales")
SUMA = modulo("unidad-3/11-while-y-terminacion")
BUSCA = modulo("unidad-3/13-break-continue-y-anidacion")
FACTORIAL = modulo("unidad-3/16-recursion")
REGISTRO = modulo("unidad-3/18-diccionarios-y-registros")
PROYECTO = modulo("unidad-3/19-proyecto-integrador")

class Representacion(unittest.TestCase):
    def test_conversion_binaria_1024_valores(self):
        for n in range(1024):
            with self.subTest(n=n):
                patron = BIN.a_binario(n)
                self.assertEqual(patron, format(n, "b"))
                self.assertEqual(int(patron, 2), n)

    def test_conversion_rechaza_dominio(self):
        for n in (-1, True, 1.5, "3"):
            with self.subTest(n=n), self.assertRaises(ValueError):
                BIN.a_binario(n)

    def test_complemento_256_valores(self):
        for n in range(-128, 128):
            with self.subTest(n=n):
                patron = COMP.complemento(n, 8)
                valor = int(patron, 2)
                recuperado = valor - 256 if patron[0] == "1" else valor
                self.assertEqual(len(patron), 8)
                self.assertEqual(recuperado, n)

    def test_complemento_limites(self):
        for n, bits in ((128, 8), (-129, 8), (0, 0), (0, True), (True, 8)):
            with self.subTest(n=n, bits=bits), self.assertRaises(ValueError):
                COMP.complemento(n, bits)

    def test_leyes_booleanas(self):
        for a, b, c in itertools.product((False, True), repeat=3):
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(not (a and b), (not a) or (not b))
                self.assertEqual(not (a or b), (not a) and (not b))
                self.assertEqual(a or ((not a) and b), a or b)
                f = ((not a) and b and (not c)) or ((not a) and b and c) or (a and b and (not c)) or (a and b and c)
                self.assertEqual(f, b)

    def test_sumador_completo(self):
        for a, b, cin in itertools.product((0, 1), repeat=3):
            with self.subTest(a=a, b=b, cin=cin):
                suma = a ^ b ^ cin
                cout = (a & b) | (cin & (a ^ b))
                self.assertEqual(a + b + cin, 2 * cout + suma)

class Programacion(unittest.TestCase):
    def test_costo_y_reparto(self):
        self.assertEqual(COSTO.costo(3, 12000), 36000)
        self.assertEqual(COSTO.costo(0, 12000), 0)
        for datos in ((-1, 2), (2, -1), (True, 2), (2, "3")):
            with self.subTest(datos=datos), self.assertRaises(ValueError):
                COSTO.costo(*datos)
        for k, m, esperado in ((17, 5, (3, 2)), (3, 5, (0, 3)), (0, 5, (0, 0)), (20, 4, (5, 0))):
            self.assertEqual(REPARTO.repartir(k, m), esperado)
        for datos in ((1, 0), (-1, 2), (3, -1), (1.0, 2)):
            with self.subTest(datos=datos), self.assertRaises(ValueError):
                REPARTO.repartir(*datos)

    def test_umbral_descuento(self):
        for monto, esperado in ((0, 0), (99999, 99999), (100000, 90000), (100010, 90009)):
            self.assertEqual(TOTAL.total(monto), esperado)
        for monto in (-1, True, 100001):
            with self.subTest(monto=monto), self.assertRaises(ValueError):
                TOTAL.total(monto)

    def test_entrada_y_estado(self):
        for texto, esperado in (("0", 0), ("3", 3), ("10", 10), (" 4 ", 4)):
            self.assertEqual(ENTRADA.cantidad_desde_texto(texto), esperado)
        for texto in ("-1", "11", "tres", "3.5", ""):
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                ENTRADA.cantidad_desde_texto(texto)
        for n, esperado in ((0, "agotado"), (1, "bajo"), (2, "bajo"), (3, "disponible")):
            self.assertEqual(ESTADO.estado(n), esperado)
        with self.assertRaises(ValueError):
            ESTADO.estado(-1)

    def test_suma_101_valores(self):
        for n in range(101):
            with self.subTest(n=n):
                self.assertEqual(SUMA.sumar_hasta(n), n * (n + 1) // 2)
        with self.assertRaises(ValueError):
            SUMA.sumar_hasta(-1)

    def test_busqueda_matriz(self):
        for matriz, objetivo, esperado in (([], 1, None), ([[]], 1, None), ([[4, 0], [8, 2]], 8, (1, 0)), ([[8, 8]], 8, (0, 0)), ([[4]], 8, None)):
            self.assertEqual(BUSCA.buscar(matriz, objetivo), esperado)

    def test_factorial_101_valores(self):
        for n in range(101):
            with self.subTest(n=n):
                self.assertEqual(FACTORIAL.factorial(n), math.factorial(n))
        for n in (-1, 101, True, 1.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                FACTORIAL.factorial(n)

    def test_alta_y_normalizacion(self):
        inventario = {}
        REGISTRO.alta(inventario, " K01 ", " Sensores ", 0)
        self.assertEqual(inventario, {"K01": {"nombre": "Sensores", "unidades": 0}})
        previo = copy.deepcopy(inventario)
        with self.assertRaises(ValueError):
            REGISTRO.alta(inventario, "K01", "Otro", 4)
        self.assertEqual(inventario, previo)

class Inventario(unittest.TestCase):
    def setUp(self):
        self.inventario = {}
        PROYECTO.alta(self.inventario, "K01", "Sensores", 4)

    def test_altas_invalidas_preservan_estado(self):
        casos = [("K01", "Otro", 8), ("", "Otro", 8), ("K02", "", 8), ("K02", "Otro", -1), ("K02", "Otro", True), ("K02", "Otro", 1.5), ("K\n02", "Otro", 1)]
        previo = copy.deepcopy(self.inventario)
        for datos in casos:
            with self.subTest(datos=datos), self.assertRaises(ValueError):
                PROYECTO.alta(self.inventario, *datos)
            self.assertEqual(self.inventario, previo)

    def test_consulta_independiente_y_ausente(self):
        consulta = PROYECTO.consultar(self.inventario, " K01 ")
        consulta["unidades"] = 0
        self.assertEqual(self.inventario["K01"]["unidades"], 4)
        self.assertIsNone(PROYECTO.consultar(self.inventario, "K99"))

    def test_actualizar_validacion(self):
        PROYECTO.actualizar(self.inventario, "K01", 0)
        self.assertEqual(self.inventario["K01"]["unidades"], 0)
        previo = copy.deepcopy(self.inventario)
        for codigo, unidades in (("K99", 2), ("K01", -1), ("K01", True)):
            with self.subTest(codigo=codigo, unidades=unidades), self.assertRaises(ValueError):
                PROYECTO.actualizar(self.inventario, codigo, unidades)
            self.assertEqual(self.inventario, previo)

    def test_persistencia_con_acentos(self):
        PROYECTO.alta(self.inventario, "K02", "Medición", 0)
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "subcarpeta" / "inventario.json"
            PROYECTO.guardar(self.inventario, ruta)
            self.assertIn("Medición", ruta.read_text(encoding="utf-8"))
            self.assertEqual(PROYECTO.cargar(ruta), self.inventario)
            PROYECTO.guardar({}, ruta)
            self.assertEqual(PROYECTO.cargar(ruta), {})

    def test_documentos_invalidos_no_se_aplican(self):
        valido = PROYECTO.documento(self.inventario)
        documentos = [[], {}, {"version": 2, "kits": []}, {"version": True, "kits": []}, {"version": 1, "kits": {}}, {"version": 1, "kits": [{"codigo": "K02", "nombre": "Otro", "unidades": -1}]}, {"version": 1, "kits": valido["kits"] * 2}, {"version": 1, "kits": [*valido["kits"], {"codigo": "K02", "nombre": "Otro", "unidades": True}]}, {"version": 1, "kits": [{"codigo": "K02", "nombre": "Otro", "unidades": 1, "extra": 2}]}]
        previo = copy.deepcopy(self.inventario)
        for documento in documentos:
            with self.subTest(documento=documento):
                with self.assertRaises(ValueError):
                    candidato = PROYECTO.desde_documento(documento)
                    self.inventario = candidato
                self.assertEqual(self.inventario, previo)

    def test_archivos_invalidos(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "inventario.json"
            for texto in ("{", '{"version":1,"version":1,"kits":[]}', '{"version":1,"kits":[{"codigo":"K01","nombre":"A","nombre":"B","unidades":1}]}'):
                ruta.write_text(texto, encoding="utf-8")
                with self.subTest(texto=texto), self.assertRaises(ValueError):
                    PROYECTO.cargar(ruta)
            ruta.write_bytes(b"\xff")
            with self.assertRaises(UnicodeError):
                PROYECTO.cargar(ruta)
            with self.assertRaises(FileNotFoundError):
                PROYECTO.cargar(Path(carpeta) / "no-existe.json")

    def test_menu_reglas_y_recuperacion(self):
        guion = "6\n1\nK01\nSensores\n4\n1\nK01\nOtro\n8\n3\nK01\n-1\n2\nK01\n5\n3\nK01\n0\n6\n2\nK01\n4\n9\n0\n"
        with tempfile.TemporaryDirectory() as carpeta:
            proceso = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "unidad-3/19-proyecto-integrador/main.py"), "--menu"], input=guion, text=True, encoding="utf-8", capture_output=True, cwd=carpeta, timeout=20)
            self.assertEqual(proceso.returncode, 0, proceso.stderr)
            for esperado in ("Error:", "Código duplicado", "Unidades deben ser un entero no negativo", "Sensores: 4", "Inventario guardado", "Cantidad actualizada", "Inventario cargado", "K01 | Sensores | 4", "Opción inválida", "Fin"):
                self.assertIn(esperado, proceso.stdout)
            datos = PROYECTO.cargar(Path(carpeta) / "salida" / "inventario.json")
            self.assertEqual(datos["K01"]["unidades"], 4)

if __name__ == "__main__":
    unittest.main()
