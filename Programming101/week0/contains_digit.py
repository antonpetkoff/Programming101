
def contains_digit(number, digit):
    allDigits = list(str(number))
    for item in allDigits:
        if int(item) == digit:
            return True
    return False
