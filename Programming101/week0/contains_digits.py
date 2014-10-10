from contains_digit import contains_digit


def contains_digits(number, digits):
    for i in range(len(digits)):
        if not contains_digit(number, digits[i]):
            return False
    return True
