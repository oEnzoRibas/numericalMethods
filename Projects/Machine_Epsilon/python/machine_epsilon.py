import numpy as np

def machine_precision_single(VAL):
    aSingle = np.float32(1)
    sSingle = np.float32(VAL + aSingle)

    while( sSingle > VAL):
        aSingle = aSingle/2
        sSingle = np.float32(VAL + aSingle)

    prec = 2 * aSingle
    return prec

def machine_precision_double(VAL):
    """
    This function calculates the machine epsilon for double-precision floating-point numbers
    for a given value. It iteratively halves the value of `aDouble` until the sum of `VAL` 
    and `aDouble` is indistinguishable from `VAL`. The machine epsilon is then calculated 
    as twice the final value of `aDouble`.

    :param VAL: The value for which the machine epsilon is to be calculated.
    :type VAL: float

    """

    aDouble = np.float64(1)
    sDouble = np.float64(VAL + aDouble)

    while( sDouble > VAL):
        aDouble = aDouble/2
        sDouble = np.float64(VAL + aDouble)

    prec = 2 * aDouble
    return prec

def main():
    """
    This function calculates the machine epsilon for floating-point numbers for a given set of values.
    It uses the numpy library to find the smallest number that can be added to each value in the list
    such that the result is different from the original value.
    """

    nums = [1,10,17,100,184,1000,1575,10000,17893]
    for val in  nums:
        print(f"Machine Epsilon Single for val {val}: {machine_precision_single(val)}")
    for val in nums:
        print(f"Machine Epsilon Double for val {val}: {machine_precision_double(val)}")

main()