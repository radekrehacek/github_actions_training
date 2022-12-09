def eval_poly(poly: list, x: float) -> float:
    """
    Evaluate polynomial at x
    :param poly:
    :param x: float
    :return:
    """
    # Initialize result
    result = poly[0]

    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, len(poly)):
        result = result * x + poly[i]

    return result
