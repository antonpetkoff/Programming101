
def comparator(a, b):       # compare two fractions
    if a[0] / float(a[1]) > b[0] / float(b[1]):
        return 1            # a > b
    elif a[0] / float(a[1]) == b[0] / float(b[1]):
        return 0            # a = b
    return -1               # a < b


def sort_fractions(fractions):
    return sorted(fractions, comparator)


def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7),
                          (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()
