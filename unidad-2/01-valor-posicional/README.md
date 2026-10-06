# Sistemas numéricos y valor posicional

[Recurso anterior](../../unidad-1/12-caso-integrador-de-ingenieria/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/02-decimal-y-fracciones/README.md)

## Objetivo

Interpretar representaciones en bases 2, 8, 10 y 16.

## Conceptos y explicación

Una base b define b símbolos y pesos posicionales b⁰, b¹, b² y así sucesivamente hacia la izquierda del separador. La posición, no solo el símbolo, determina el valor. El sistema decimal usa 0 a 9; el binario 0 y 1; el octal 0 a 7; el hexadecimal 0 a 9 y A a F. En hexadecimal A representa diez y F quince.

El número es la cantidad abstracta; la representación depende de la base. Treinta y siete puede escribirse 37₁₀, 100101₂, 45₈ o 25₁₆. El prefijo de Python `0b`, `0o` o `0x` indica cómo leer el literal; después de interpretarlo, el valor entero no conserva una «base original».

Cada dígito debe ser menor que la base. «102» no es un número binario válido. El signo negativo no es un dígito posicional; se estudia por separado de la representación fija en bits. Los ceros iniciales no cambian el valor, aunque pueden indicar un ancho requerido en un formato.

## Caso resuelto paso a paso

Descomposición: 37₁₀ = 3×10¹ + 7×10⁰. En binario: 100101₂ = 1×2⁵ + 1×2² + 1×2⁰ = 32 + 4 + 1.

| Base | Representación | Valor decimal |
|---|---|---|
| 2 | 100101 | 37 |
| 8 | 45 | 37 |
| 10 | 37 | 37 |
| 16 | 25 | 37 |

El programa confirma que los cuatro literales representan el mismo entero.

## Código completo

Archivo: [main.py](main.py).

```python
valores = [37, 0b100101, 0o45, 0x25]
print(valores)
print(all(valor == 37 for valor in valores))
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
[37, 37, 37, 37]
True
```

Compara con [esperado.txt](esperado.txt). Una diferencia de contenido merece revisión; los saltos de línea pueden variar entre sistemas.

## Práctica guiada

Predice los valores. Ejecuta el programa. Descompón cada representación usando potencias de su base. Cambia un dígito e identifica cuánto varía el valor. Prueba un literal inválido en un archivo separado y observa el error de sintaxis.

## Errores que conviene detectar

- Interpretar 101 sin indicar su base.
- Usar un dígito cuyo valor es igual o superior a la base.

## Ejercicio para resolver

Representa 26₁₀ en base 2, 8 y 16, y demuestra una equivalencia por expansión.

<details>
<summary>Solución y razonamiento (abre después de intentarlo)</summary>

26₁₀ = 11010₂ = 32₈ = 1A₁₆. La expansión hexadecimal es 1×16 + 10 = 26. Los símbolos A a F representan valores, no variables.

</details>

## Preguntas de comprensión

¿Un entero guarda su base de escritura? ¿Por qué 8 no es dígito octal? ¿Qué cambia al añadir un cero a la izquierda?

## Evidencia de aprendizaje

Entrega tu desarrollo del ejercicio, el razonamiento o prueba de escritorio y al menos un caso límite. Explica cualquier cambio de contrato. Conserva los resultados que permitan comprobar tu conclusión.

[Recurso anterior](../../unidad-1/12-caso-integrador-de-ingenieria/README.md) · [Índice de la unidad](../README.md) · [Siguiente recurso](../../unidad-2/02-decimal-y-fracciones/README.md)
