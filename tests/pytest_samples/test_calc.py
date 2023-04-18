import pytest

from python_tools.pytest_samples.calc import mul


@pytest.mark.parametrize(
    "a,b,expected",
    [(2, 3, 6), (5, 4, 20), (-1, 1, -1)]
)
def test_mul_should_succeed_with_int_params(a, b, expected) -> None:
    assert mul(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [('1', 1, 1)]
)
def test_mul_should_succeed_with_str_params(a, b, expected) -> None:
    assert mul(a, b) == expected
