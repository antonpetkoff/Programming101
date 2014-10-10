from is_prime import is_prime


def goldbach(n):
    divisor = 1
    tuples = []
    while divisor <= n/2:
        if is_prime(divisor) and is_prime(n-divisor):
            tuples.append((divisor, n - divisor))
        divisor += 1
    return tuples
