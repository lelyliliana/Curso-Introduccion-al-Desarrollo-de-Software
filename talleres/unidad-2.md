# Taller 2. Representación y lógica de un panel

[Inicio](../README.md) · [Unidad 2](../unidad-2/README.md) · [Siguiente recurso](../unidad-3/01-analisis-del-problema/README.md)

## Situación

Un panel informa cantidad de kits y permiso de entrega. La cantidad se transmite inicialmente como entero sin signo de ocho bits. El permiso es verdadero si la credencial C es válida y existe disponibilidad D. Una alerta se activa si hay error E o no hay disponibilidad.

## Actividades

1. Representa 0,26,53 y255 en binario, octal y hexadecimal. Expande53 en dos bases para demostrar equivalencia.
2. Convierte10011.01₂ a decimal indicando pesos negativos. Explica por qué0.1₁₀ no tiene expansión binaria finita.
3. Convierte26 a binario por divisiones sucesivas. Registra dividendo,cociente,residuo y orden final.
4. Realiza1011₂+0110₂,1011₂−0110₂ y101₂×11₂. Comprueba en decimal.
5. ¿Cabe256 en el campo de ocho bits? Si se cambia a complemento a dos, ¿qué intervalo puede representarse? Codifica−5.
6. Construye las tablas de permiso C·D y alerta E+D′. No confundas OR con XOR.
7. Aplica De Morgan a la negación del permiso. Explica la regla verbal resultante.
8. Simplifica F=A′BC′+A′BC+ABC′+ABC con un mapa de tres variables. Usa orden Gray y comprueba las ocho entradas.
9. Construye la tabla de un sumador completo de A,B,Cin. Usa S=A XOR B XOR Cin y Cout=AB+Cin(A XOR B). Verifica A+B+Cin=2Cout+S.
10. Explica qué no demuestra la simulación ideal de las compuertas.

## Entrega

Incluye conversiones con procedimientos, tablas completas, mapa y comprobaciones. Puedes usar Python para verificar después de resolver a mano; el resultado automático no sustituye el razonamiento.

<details>
<summary>Soluciones y comprobaciones</summary>

| Decimal | Binario | Octal | Hexadecimal |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 26 | 11010 | 32 | 1A |
| 53 | 110101 | 65 | 35 |
| 255 | 11111111 | 377 | FF |

53=6×8+5=3×16+5. La fracción10011.01₂ es19.25₁₀. Para26: divisiones26→13,r0;13→6,r1;6→3,r0;3→1,r1;1→0,r1. Se leen11010. Operaciones:10001₂,101₂ y1111₂. 256 necesita nueve bits; ocho bits con signo cubren−128..127 y−5 se codifica11111011.

Permiso para CD=00,01,10,11:0,0,0,1. Alerta para ED=00,01,10,11:1,0,1,1. Negar permiso produce C′+D′: credencial inválida o falta de disponibilidad. El mapa reduce F a B porque A y C varían en el grupo de cuatro unos.

| A | B | Cin | Cout | S |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

La igualdad aritmética confirma cada fila ideal. No comprueba retardos, voltajes, ruido ni fallos físicos. La lógica de acceso tampoco prueba por sí sola seguridad de credenciales.

</details>

## Autoevaluación

Conversiones justificadas30%; operaciones y rangos20%; tablas y leyes20%; Karnaugh y sumador20%; claridad y límites10%. Verifica que cada celda está en la combinación correcta y que nunca se omite base o ancho cuando son necesarios.
