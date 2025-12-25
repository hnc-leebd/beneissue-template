"""Division module for the calculator."""


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient of a divided by b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
