# extra formatting utilities, not related to stylesheets
from math import floor, log10
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import lmfit


def format_value_error(value, err, nd=2):
    """Format value and error to "value(err)", with `nd` decimal places."""
    if nd < 1:
        raise ValueError("Minimum 1 decimal place.")
    if err < 0:
        raise ValueError("Error cannot be negative.")
    try:
        decimal_place = floor(log10(err))-nd+1
    except ValueError: # err == 0
        decimal_place = nd
    scale = 10**-decimal_place
    fmt = f"{{:.0{abs(decimal_place)}f}}({{:.0f}})"
    return fmt.format(value, err*scale)

def format_parameter(param: "lmfit.Parameter", nd=2):
    """Format lmfit.Parameter to value(err), with `nd` decimal places."""
    return format_value_error(param.value, param.stderr, nd)