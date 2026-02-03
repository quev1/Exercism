def square_root(number):
    if number == 0:
        return 0
    if number < 0:
        raise ValueError("square_root(number) is not defined for negative numbers.")

    approx = 0
    while approx**2 < number:
        approx += 1 
    return approx