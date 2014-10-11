
def is_increasing(seq):
    if len(seq) < 1:
        return False
    previous = seq[0]
    for i in range(1, len(seq)):
        if int(seq[i]) <= previous:
            return False
        else:
            previous = int(seq[i])
    return True


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()
