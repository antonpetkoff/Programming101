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


def main():
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))


if __name__ == '__main__':
    main()
