from ._if_not_valid_raise import (_if_not_int_or_float_raise,
                                  _if_not_positive_raise)

def right_rect_pyramid(bl, bw, h):
    """Calculates the volume of a right rectangle pyramid using the formula:
    (base length * base width * pyramid height)/3

    Parameters
    ----------
    bl: int or float
        The base length of the equation.

    bw: int or float
        The base width of the equation.

    h: int or float
        The pyramid height of the equation.

    Returns
    -------
    Float
        (bl * bw * h)/3

    Raises
    ------
    ValueError
        If bl, bw or h::
            Is not an integer.
            Is not positive.

    Examples
    --------
    >>> school_algorithms.right_rect_pyramid(3, 4, 7)
    28.0
    
    """
    _if_not_int_or_float_raise(bl, bw, h)
    _if_not_positive_raise(bl, bw, h)
    return (bl * bw * h)/3
