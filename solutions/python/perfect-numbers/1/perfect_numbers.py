def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    
    for num in range(1, number):
        if number % num == 0:
            factors.append(num)

    factors_sum = sum(factors)

    if factors_sum > number:
        return "abundant"
    elif factors_sum < number:
        return "deficient"
    return "perfect"