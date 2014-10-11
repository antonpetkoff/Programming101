from is_int_palindrome import is_int_palindrome


def is_hack_number(n):
    binStr = str(bin(n))[2:]
    if not is_int_palindrome(int(binStr)):
        return False
    onesCount = 0
    for digit in binStr:
        if digit == "1":
            onesCount += 1
    if not onesCount % 2 == 0:
        return True
    return False


def next_hack(n):
    n += 1
    while(not is_hack_number(n)):
        n += 1
    return n


def main():
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))


if __name__ == '__main__':
    main()
