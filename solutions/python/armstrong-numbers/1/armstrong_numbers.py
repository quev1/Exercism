def is_armstrong_number(number):
    digits = [int(n) for n in str(number)]
    total = 0
    for digit in digits:
        total += digit ** len(digits)
    return total == number
    
