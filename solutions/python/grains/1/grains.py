def square(number):
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")
    
def total():
    grain = 0
    for number in range(1, 65):
        grain += square(number)
    return grain
    
