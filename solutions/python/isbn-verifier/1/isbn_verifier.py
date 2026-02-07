def is_valid(isbn):
    transformed_isbn = isbn.replace("-", "")
    multiplicator = 10
    isbn_value = 0 
    
    if len(transformed_isbn) != 10:
        return False
    
    for i, char in enumerate(transformed_isbn):
            if char.isdigit():
                isbn_value += int(char) * multiplicator
                multiplicator -= 1
            elif char == "X" and i == 9:
                isbn_value += 10 * multiplicator
                multiplicator -= 1
            else:
                return False

    return isbn_value % 11 == 0