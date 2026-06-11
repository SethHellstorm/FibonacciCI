"""
Módulo de la sucesión de Fibonacci con validación de entradas
y manejo de excepciones.
"""


def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo término de la sucesión de Fibonacci.

    La sucesión está definida como:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)  para n ≥ 2

    Implementación iterativa: O(n) tiempo, O(1) espacio.

    Args:
        n (int): Índice del término deseado. Debe ser un entero
                 mayor o igual a 0.

    Returns:
        int: El n-ésimo número de Fibonacci.

    Raises:
        TypeError:  Si `n` no es un número entero.
        ValueError: Si `n` es negativo.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(-1)
        Traceback (most recent call last):
            ...
        ValueError: n debe ser ≥ 0. Se recibió: -1
    """

    # Validación de tipo
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(
            f"n debe ser int. Se recibió: {type(n).__name__!r}"
        )

    # Validación de dominio
    if n < 0:
        raise ValueError(
            f"n debe ser ≥ 0. Se recibió: {n}"
        )

    # Cálculo iterativo
    try:
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    except MemoryError:
        raise MemoryError(
            f"No hay memoria suficiente para calcular F({n})."
        )


def pedir_numero() -> int:
    """
    Solicita al usuario un número entero no negativo por consola.

    Repite la solicitud hasta recibir una entrada válida.

    Returns:
        int: El número ingresado por el usuario.
    """
    while True:
        try:
            entrada = input("Ingresa el índice n (entero ≥ 0): ").strip()
            n = int(entrada)
            if n < 0:
                print(f"  ✗ Error: el número debe ser ≥ 0. Intenta de nuevo.")
                continue
            return n
        except ValueError:
            print(f"  ✗ Error: '{entrada}' no es un entero válido. Intenta de nuevo.")


# ── Ejecución interactiva ────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Calculadora de Fibonacci ===\n")
    try:
        n = pedir_numero()
        resultado = fibonacci(n)
        print(f"\n  F({n}) = {resultado}")
    except (TypeError, ValueError, MemoryError) as e:
        print(f"\n  ✗ {type(e).__name__}: {e}")