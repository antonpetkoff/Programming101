
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
