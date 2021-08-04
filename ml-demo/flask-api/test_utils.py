import pytest

from utils import mysum3


@pytest.mark.parametrize("x, y, z, expected", [
    (1, 2, 3, 16),
    (-10, -20, -30, -50),
])
def test_mysum3(x, y, z, expected):
    assert mysum3(x, y, z) == expected
