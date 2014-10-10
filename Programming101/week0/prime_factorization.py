from is_prime import is_prime


def prime_factorization(n):
    divisor = 2
    tuples = []
    while n > 1:
        if n % divisor == 0 and is_prime(divisor):
            power = 0
            while n % divisor == 0:
                n //= divisor
                power += 1
            tuples.append((divisor, power))
        else:
            divisor += 1
    return tuples
