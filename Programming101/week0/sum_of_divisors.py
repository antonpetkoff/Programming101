
def sum_of_divisors(n):
    sumDivisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            sumDivisors += i
    return sumDivisors


def main():
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))


if __name__ == '__main__':
    main()
