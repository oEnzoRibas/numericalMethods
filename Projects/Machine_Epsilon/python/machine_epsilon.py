import numpy as np

def machine_precision_single(VAL):
    aSingle = np.float32(1)
    sSingle = np.float32(VAL + aSingle)

    while( sSingle > VAL):
        aSingle = aSingle/ np.float32(2)
        sSingle = np.float32(VAL + aSingle)

    prec =  np.float32(2)  * aSingle
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
        aDouble = aDouble/np.float64(2)
        sDouble = np.float64(VAL + aDouble)

    prec =  np.float64(2)  * aDouble
    return prec
    
    #128 may not be supported in all systems
def machine_precision_longdouble(VAL):
    """
    This function calculates the machine epsilon for long double-precision floating-point numbers
    for a given value. It iteratively halves the value of `aLongDouble` until the sum of `VAL` 
    and `aLongDouble` is indistinguishable from `VAL`. The machine epsilon is then calculated 
    as twice the final value of `aLongDouble`.

    :param VAL: The value for which the machine epsilon is to be calculated.
    :type VAL: float

    """

    aDouble = np.float128(1)
    sDouble = np.float128(VAL + aDouble)

    while( sDouble > VAL):
        aDouble = aDouble/np.float128(2)
        sDouble = np.float128(VAL + aDouble)

    prec = np.float128(2) * aDouble
    return prec

def main():
    """
    This function calculates the machine epsilon for floating-point numbers for a given set of values.
    It uses the numpy library to find the smallest number that can be added to each value in the list
    such that the result is different from the original value.
    """

    nums = [1,10,17,100,184,1000,1575,10000,17893]
    for val in  nums:
        print(f"Machine Epsilon Single for val {val}: {machine_precision_single(np.float32(val))}")
    for val in nums:
        print(f"Machine Epsilon Double for val {val}: {machine_precision_double(np.float64(val))}")
    
    #128 may not be supported in all systems
    for val in nums:
        print(f"Machine Epsilon Double for val {val}: {machine_precision_longdouble(np.float128(val))}")

main()