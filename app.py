def add(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b