
def list_to_number(digits):
    n = len(digits)
    number = 0
    for i in range(0, n):
        number += int(digits[i]) * (10 ** (n-i-1))
    return number
