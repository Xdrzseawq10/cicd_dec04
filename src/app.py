import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# ---------- Advanced operations ----------
def square(x):
    return x * x


def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is not allowed")
    return math.sqrt(x)


def log(x, base=10):
    if x <= 0:
        raise ValueError("Log input must be greater than 0")
    if base <= 0 or base == 1:
        raise ValueError("Log base must be greater than 0 and not equal to 1")
    return math.log(x, base)


def sin(x, degrees=False):
    if degrees:
        x = math.radians(x)
    return math.sin(x)


def cos(x, degrees=False):
    if degrees:
        x = math.radians(x)
    return math.cos(x)


def percentage(value, percent=None):
    """
    percentage(10) -> 0.1
    percentage(200, 10) -> 20
    """
    if percent is None:
        return value / 100
    return value * (percent / 100)