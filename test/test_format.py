import pytest
from scistyles.format import format_value_error, format_parameter
from math import pi


def test_basic():
    # test basic functionnality
    v = 3.14159265
    err = 0.12345
    assert format_value_error(v, err) == "3.14(12)"
    assert format_value_error(-v, err) == "-3.14(12)"

def test_rounding():
    # test rounding of value
    assert format_value_error(10.200, 0.1234) == "10.20(12)"
    assert format_value_error(10.209, 0.1234) == "10.21(12)"
    assert format_value_error(10.205, 0.1234) == "10.21(12)"
    # test rounding of error
    assert format_value_error(10.205, 0.129) == "10.21(13)"

def test_minimum_precision():
    assert format_value_error(3.14159, 0.1234, nd=1) == "3.1(1)"

def test_nd():
    assert format_value_error(3.14159, 0.1234, nd=3) == "3.142(123)"


@pytest.mark.parametrize("nd", [0, -1])
def test_invalid_precision(nd):
    with pytest.raises(ValueError, match="Minimum 1 decimal place"):
        format_value_error(3.14, 0.12, nd=nd)


def test_zero_error():
    assert format_value_error(3.14159, 0) == "3.14(0)"
    assert format_value_error(3.14159, 0, nd=4) == "3.1416(0)"


def test_zero_value_with_nonzero_error():
    assert format_value_error(0, 0.1234) == "0.00(12)"


def test_error_rounding_carries():
    assert format_value_error(10.205, 0.199) == "10.21(20)"


@pytest.mark.parametrize(
    ("value", "error", "expected"),
    [
        (1234.5, 12.3, "1234(12)"),
        (0.001234, 0.0000123, "0.001234(12)"),
        (-0.001234, 0.0000123, "-0.001234(12)"),
    ],
)
def test_different_magnitudes(value, error, expected):
    assert format_value_error(value, error) == expected


def test_neg_error():
    with pytest.raises(ValueError):
        format_value_error(10.205, -0.199) == "10.21(20)"

def test_format_parameter():
    lmfit = pytest.importorskip("lmfit")

    v = 3.14159265
    err = 0.1234
    param = lmfit.Parameter("x", value=v)
    param.stderr=err

    assert format_parameter(param) == format_value_error(v, err)
