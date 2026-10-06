# Convenciones de representación y pseudocódigo

[Inicio](../README.md) · [Siguiente recurso](../unidad-2/01-valor-posicional/README.md)

| Concepto | Matemática/pseudocódigo | Python |
|---|---|---|
| Asignación | x ← valor | x = valor |
| Igualdad | x = y | x == y |
| División verdadera | a / b | a / b |
| Cociente entero no negativo | a DIV b | a // b |
| Residuo | a MOD b | a % b |
| Potencia | a elevado a b | a ** b |
| AND | AB o A·B | a and b (bool) |
| OR | A+B | a or b (bool) |
| NOT | A′ | not a |

El pseudocódigo de reparto usa DIV/MOD solo con dividendo no negativo y divisor positivo. En Python, // es división piso también para negativos. OR es inclusivo. El símbolo + del álgebra booleana no es suma aritmética. ^ no es potencia en Python.

Los subíndices señalan base: 101₂ y 101₁₀ no representan la misma cantidad. Los prefijos del código son 0b,0o,0x. Un valor con signo y un patrón de complemento a dos deben declarar convención y ancho.

Los índices Python empiezan en cero. Las posiciones de presentación pueden numerarse desde uno si se indica. El extremo final de range y slice se excluye.

## Plantilla para analizar un problema

- Necesidad y alcance.
- Entradas con tipos y unidades.
- Resultado esperado.
- Reglas, restricciones y supuestos.
- Procedimiento o modelo.
- Caso normal, caso límite y caso inválido.
- Evidencia de comprobación y limitaciones.
