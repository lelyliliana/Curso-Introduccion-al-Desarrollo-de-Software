# Operadores aritméticos, comparación y lógica

[Recurso anterior](../../unidad-3/07-tipos-y-precision/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/09-condicionales/README.md)

## Objetivo

Combinar operadores con significado y precedencia claros.

## Conceptos y explicación

En Python `+,-,*,/` realizan operaciones aritméticas; `/` produce división verdadera y `//` división piso. Con negativos, // redondea hacia menos infinito, no hacia cero. El residuo cumple a=(a//b)×b+a%b, con b distinto de cero. `**` expresa potencia; `^` realiza XOR bit a bit sobre enteros.

`==,!=,<,<=,>,>=` comparan valores. `is` compara identidad y se usa típicamente con None; no reemplaza == para texto o números. Se puede escribir 0<=cantidad<=10. Los operadores `not`, `and`, `or` combinan condiciones; and y or usan cortocircuito, de modo que pueden evitar evaluar una segunda parte innecesaria.

Los paréntesis hacen explícita una agrupación cuando conviene. Potencia tiene particularidades: −2**2 es −(2**2), mientras que (−2)**2 es 4. La concatenación de texto usa + pero no mezcla automáticamente str e int. Las f-strings evitan conversiones dispersas al presentar resultados.

## Caso resuelto paso a paso

El ejemplo contrasta -7//3=-3 y -7%3=2: -7 = (-3)×3+2. Compara potencia 2**3=8 y XOR 2^3=1. Después comprueba que una cantidad de 4 con código no vacío cumple el permiso.

| Expresión | Resultado |
|---|---|
| 2+3*4 | 14 |
| (2+3)*4 | 20 |
| -2**2 | -4 |
| (-2)**2 | 4 |

## Código completo

Archivo: [main.py](main.py).

```python
print(-7 // 3, -7 % 3)
print(2 ** 3, 2 ^ 3)
print(2 + 3 * 4, (2 + 3) * 4)
print(-2**2, (-2)**2)
cantidad, codigo = 4, "K01"
print(0 <= cantidad <= 10 and codigo != "")
```

## Ejecución

Abre una terminal en la carpeta de esta lección. Si aún no tienes Python, sigue la [guía de ambiente](../../docs/ambiente-y-herramientas.md).

Windows (PowerShell):

```powershell
python main.py
```

Ubuntu y macOS:

```bash
python3 main.py
```

### Salida esperada

```text
-3 2
8 1
14 20
-4 4
True
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Evalúa las expresiones a mano. Ejecuta. Comprueba la identidad de división. Cambia cantidad a 11 y código a vacío. Explica qué operador determina cada resultado.

## Errores que conviene detectar

- Usar ^ para potencia en lugar de **.
- Suponer que // trunca hacia cero cuando el resultado es negativo.

## Ejercicio para resolver

Predice 7//3,7%3,-7//3,-7%3 y crea una condición segura para comprobar si un texto opcional no es None y empieza por K.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

Resultados 2,1,-3,2. Condición: texto is not None and texto.startswith("K"). El cortocircuito evita llamar startswith sobre None. El contrato debe asegurar que un valor no nulo sea texto.

</details>

## Preguntas de comprensión

¿Qué distingue / y //? ¿Por qué is no reemplaza ==? ¿Qué parte se omite por cortocircuito?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-3/07-tipos-y-precision/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-3/09-condicionales/README.md)
