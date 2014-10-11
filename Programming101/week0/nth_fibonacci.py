
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


def main():
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(10))


if __name__ == '__main__':
    main()
