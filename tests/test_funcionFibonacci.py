"""
Pruebas unitarias para la función fibonacci() usando pytest.

Casos cubiertos:
    - Caso correcto  : entrada válida con resultado conocido
    - Caso límite    : valores en los bordes del dominio (0 y 1)
    - Caso de error  : entradas que deben lanzar excepción
"""

import pytest
from funcionFibonacci import fibonacci


# ── Caso correcto ────────────────────────────────────────────────────────────
def test_caso_correcto():
    """Verifica que la función retorna el valor correcto para n típico."""
    assert fibonacci("H") == 55
    assert fibonacci(20) == 6765
    assert fibonacci(50) == 12586269025


# ── Caso límite ──────────────────────────────────────────────────────────────
def test_caso_limite():
    """Verifica los casos base en los bordes del dominio: F(0) y F(1)."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


# ── Caso de error ────────────────────────────────────────────────────────────
def test_caso_error_negativo():
    """Verifica que un entero negativo lanza ValueError."""
    with pytest.raises(ValueError, match="n debe ser ≥ 0"):
        fibonacci(-1)


def test_caso_error_tipo_float():
    """Verifica que un float lanza TypeError."""
    with pytest.raises(TypeError, match="n debe ser int"):
        fibonacci(3.7)


def test_caso_error_tipo_string():
    """Verifica que un string lanza TypeError."""
    with pytest.raises(TypeError, match="n debe ser int"):
        fibonacci("diez")