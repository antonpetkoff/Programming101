
def list_to_number(digits):
    n = len(digits)
    number = 0
    for i in range(0, n):
        number += int(digits[i]) * (10 ** (n-i-1))
    return number


def main():
    print(list_to_number([1, 2, 3]))
    print(list_to_number([9, 9, 9, 9, 9]))
    print(list_to_number([1, 2, 3, 0, 2, 3]))


if __name__ == '__main__':
    main()
