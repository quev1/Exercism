def equilateral(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        test = (a == b == c)
        return bool(test)
    else:
        return False

def isosceles(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        test = (a == b or b == c or a == c)
        return bool(test)
    else:
        return False
        
def scalene(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        test = (a != b != c != a)
        return bool(test)
    else:
        return False
