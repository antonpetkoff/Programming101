
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True
