# ref assignment 7_recursion.py

# maybe use fibonacci sequence to draw a spiral graphic...
# or draw room walls...


def fibonacci(n):
    """ Returns array of numbers in Fibonacci sequence up to n. """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
