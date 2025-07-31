def triangle_inequality_check(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b

def zero_size_triangle(sides):
    return all([side == 0 for side in sides])

def equilateral(sides):
    if zero_size_triangle(sides):
        return False

    a, b, c = sides
    return a == b == c and a == c


def isosceles(sides):
    a, b, c = sides

    if not triangle_inequality_check(sides):
        return False
    
    return a == b or a == c or b == c


def scalene(sides):
    if not triangle_inequality_check(sides):
        return False

    return not (equilateral(sides) or isosceles(sides))
