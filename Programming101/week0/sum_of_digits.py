
def sum_of_digits(n):
    sumDigits = 0
    digits = list(str(abs(int(n))))
    for digit in digits:
        sumDigits += int(digit)
    return sumDigits
