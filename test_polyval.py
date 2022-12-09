import polyval
import pytest

test_polynomials = (
    [5, 2, 1],
    [1, 0]
)

test_x = [-5, -0.5, 0, 0.5, 5]

test_expectations = (
    [116, 1.25, 1, 3.25, 136],
    [-5, -0.5, 0, 0.5, 5]
)


@pytest.mark.parametrize('poly,expected', list(zip(test_polynomials, test_expectations)))
def test_eval_poly(poly, expected):
    """
    basic test for the polynomial evaluation
    """
    res = []
    for x in test_x:
        res.append(polyval.eval_poly(poly, x))
    assert res == expected
