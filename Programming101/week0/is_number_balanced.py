
def is_number_balanced(n):
    if n < 10:
        return True
    digits = list(str(n))
    length = len(str(n))
    sumLeft = sumRight = 0
    for i in range(0, length//2):
        sumLeft += int(digits[i])
        sumRight += int(digits[length - i - 1])
    return True if sumLeft == sumRight else False
