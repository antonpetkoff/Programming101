from is_prime import is_prime


def goldbach(n):
    divisor = 1
    tuples = []
    while divisor <= n/2:
        if is_prime(divisor) and is_prime(n-divisor):
            tuples.append((divisor, n - divisor))
        divisor += 1
    return tuples


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))


if __name__ == '__main__':
    main()
