
def simplify_fraction(fraction):
    divisor = min(fraction)
    while divisor > 1:
        if fraction[0] % divisor == 0 and fraction[1] % divisor == 0:
            return (fraction[0] // divisor, fraction[1] // divisor)
        else:
            divisor -= 1
    return fraction
