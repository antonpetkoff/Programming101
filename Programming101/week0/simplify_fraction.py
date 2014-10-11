
def simplify_fraction(fraction):
    divisor = min(fraction)
    while divisor > 1:
        if fraction[0] % divisor == 0 and fraction[1] % divisor == 0:
            return (fraction[0] // divisor, fraction[1] // divisor)
        else:
            divisor -= 1
    return fraction


def main():
    print(simplify_fraction((3, 9)))
    print(simplify_fraction((1, 7)))
    print(simplify_fraction((4, 10)))
    print(simplify_fraction((63, 462)))


if __name__ == '__main__':
    main()
