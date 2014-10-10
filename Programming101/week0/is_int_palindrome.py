
def is_int_palindrome(n):
    digits = list(str(n))
    if digits == digits[::-1]:
        return True
    return False
