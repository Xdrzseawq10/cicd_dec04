import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import app


def test_add():
    assert app.add(5, 6) == 11
    assert app.add(-1, 1) == 0


def test_sub():
    assert app.sub(10, 7) == 3
    assert app.sub(0, 5) == -5


def test_mul():
    assert app.mul(4, 5) == 20
    assert app.mul(-2, 3) == -6


def test_div():
    assert app.div(10, 2) == 5
    assert app.div(-9, 3) == -3


def test_div_by_zero_boundary():
    with pytest.raises(ZeroDivisionError):
        app.div(10, 0)


def test_square():
    assert app.square(5) == 25
    assert app.square(-3) == 9


def test_sqrt():
    assert app.sqrt(0) == 0
    assert app.sqrt(9) == 3


def test_sqrt_negative_boundary():
    with pytest.raises(ValueError):
        app.sqrt(-1)


def test_log_default_base10():
    assert pytest.approx(app.log(100)) == 2


def test_log_custom_base():
    assert pytest.approx(app.log(8, 2)) == 3


def test_log_x_boundary():
    with pytest.raises(ValueError):
        app.log(0)
    with pytest.raises(ValueError):
        app.log(-10)


def test_log_base_boundary():
    with pytest.raises(ValueError):
        app.log(10, 1)
    with pytest.raises(ValueError):
        app.log(10, 0)
    with pytest.raises(ValueError):
        app.log(10, -2)


def test_sin_radians():
    assert pytest.approx(app.sin(math.pi / 2)) == 1.0


def test_sin_degrees():
    assert pytest.approx(app.sin(90, degrees=True)) == 1.0


def test_cos_radians():
    assert pytest.approx(app.cos(0)) == 1.0


def test_cos_degrees():
    assert pytest.approx(app.cos(180, degrees=True)) == -1.0


def test_percentage_convert_to_fraction():
    assert app.percentage(10) == 0.1
    assert app.percentage(0) == 0.0


def test_percentage_of_value():
    assert app.percentage(200, 10) == 20
    assert app.percentage(-50, 10) == -5
