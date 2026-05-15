"""
Torres de Hanoi - Solución con seguimiento de estado
=====================================================
Cada línea del output muestra el estado de los tres pegs
(A, B, C) después de cada movimiento, incluyendo el estado inicial.
"""


def hanoi_solver(n: int) -> str:
    """
    Resuelve las Torres de Hanoi para n discos y devuelve el estado
    de los tres pegs tras cada movimiento.

    Parámetros:
        n (int): Número de discos. Los discos se numeran de n (más grande) a 1 (más pequeño).

    Retorna:
        str: Líneas separadas por '\n'. Cada línea tiene el formato:
             '[A] [B] [C]'
             donde A, B, C son listas con los discos en cada peg
             (el primer elemento es el disco en el fondo, el último es la cima).
             Incluye el estado inicial (línea 0) y uno por cada movimiento.

    Número total de líneas: 2^n  (estado inicial + 2^n - 1 movimientos).
    """

    # Los pegs son listas que actúan como pilas (stack).
    # El ÚLTIMO elemento es la cima (disco más pequeño disponible).
    # Índice 0 es el fondo (disco más grande del peg).
    peg_a: list[int] = list(range(n, 0, -1))  # [n, n-1, ..., 1]
    peg_b: list[int] = []
    peg_c: list[int] = []

    # Acumulador de líneas de salida
    lines: list[str] = []

    def estado() -> str:
        """Snapshot actual de los tres pegs como string."""
        return f"{peg_a} {peg_b} {peg_c}"

    # Línea 0: estado inicial antes de cualquier movimiento
    lines.append(estado())

    # Mapa nombre → referencia real a la lista del peg
    pegs: dict[str, list[int]] = {"A": peg_a, "B": peg_b, "C": peg_c}

    def _mover(discos: int, origen: str, destino: str, auxiliar: str) -> None:
        """
        Mueve `discos` discos del peg `origen` al peg `destino`
        usando `auxiliar` como apoyo. Registra el estado tras cada movimiento.

        Caso base  : discos == 0 → nada que hacer, retorna inmediatamente.
        Caso recursivo:
          1. Mover (discos-1) de origen   → auxiliar  (liberar el disco grande)
          2. Mover el disco más grande    de origen   → destino  + registrar
          3. Mover (discos-1) de auxiliar → destino   (apilar encima del grande)
        """
        if discos == 0:
            return

        _mover(discos - 1, origen, auxiliar, destino)  # Paso 1

        disco = pegs[origen].pop()       # saca el disco de la cima del origen
        pegs[destino].append(disco)      # lo coloca en la cima del destino
        lines.append(estado())           # registra el nuevo estado

        _mover(discos - 1, auxiliar, destino, origen)  # Paso 3

    _mover(n, "A", "C", "B")

    return "\n".join(lines)


# ── Ejemplo de uso y verificación ────────────────────────────────────────────
if __name__ == "__main__":
    resultado = hanoi_solver(5)
    print(resultado)

    lineas = resultado.strip().split("\n")
    print(f"\nLíneas totales (inicial + movimientos): {len(lineas)}")
    print(f"Esperadas (2^5 = 32):                   {2**5}")
    print(f"¿Correcto?                              {len(lineas) == 2**5}")
