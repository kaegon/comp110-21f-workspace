"""Example of testing test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0 
    i: int = 0 
    for x in xs:
        total += x
    return total
    
