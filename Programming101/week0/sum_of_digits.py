
def sum_of_digits(n):
    sumDigits = 0
    digits = list(str(abs(int(n))))
    for digit in digits:
        sumDigits += int(digit)
    return sumDigits


def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))


if __name__ == '__main__':
    main()
