
def nth_fibonacci(n):
    if n < 3:
        return 1
    first = second = 1
    term = 0
    for i in range(n-2):
        term = first + second
        first = second
        second = term
    return term
