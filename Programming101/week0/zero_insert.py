
def zero_insert(n):
    digits = list(str(n))
    result = ""
    for i in range(1, len(digits)):
        if digits[i-1] == digits[i]:
            result += str(digits[i-1]) + "0"
        elif (int(digits[i-1]) + int(digits[i])) % 10 == 0:
            result += str(digits[i-1]) + "0"
        else:
            result += str(digits[i-1])
    result += str(digits[len(digits) - 1])
    return int(result)


def main():
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(1))
    print(zero_insert(6446))


if __name__ == '__main__':
    main()
