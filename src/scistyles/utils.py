# extra formatting utilities, not related to stylesheets
from math import floor, log10

# todo: use single dispatch to provide multiple interfaces, ex:
#       format_ve(v, s), format_ve([v, s]), format_ve(lmfit.Parameter)
#       tentative hierarchy:
#           format_with_error(value : float, error :float)
#           format_param([value, error]) = format_with_error(value, error)
#           format_param(param: lmfit.Parameter) = format_with_error(value, error)
# todo: add keyword arguments to control styling.
def format_parameter(param):
    """Format lmfit.Parameter to value(err), with 2 decimal places."""
    try:
        decimal_place = floor(log10(param.stderr))-1
    except ValueError: # error is 0 for frozen parameters
        decimal_place = floor(log10(abs(param.value))+4)
    scale = 10**-decimal_place
    fmt = f"{{:.0{abs(decimal_place)}f}}({{:.0f}})"
    return fmt.format(param.value, param.stderr*scale)

def format_value_error(value, err, nd=2):
    """Format value and error to "value(err)", with `nd` decimal places."""
    if nd < 1:
        raise ValueError("Minimum 1 decimal place.")
    try:
        decimal_place = floor(log10(err))-nd+1
    except ValueError: # error is 0 for frozen parameters
        decimal_place = floor(log10(abs(value))+4)
    scale = 10**-decimal_place
    fmt = f"{{:.0{abs(decimal_place)}f}}({{:.0f}})"
    return fmt.format(value, err*scale)