from is_prime import is_prime


def prime_number_of_divisors(n):
    divisorsCount = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisorsCount += 1
    return is_prime(divisorsCount)
