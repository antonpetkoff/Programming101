
def is_decreasing(seq):
    if len(seq) < 1:
        return False
    previous = seq[0]
    for i in range(1, len(seq)):
        if int(seq[i]) >= previous:
            return False
        else:
            previous = int(seq[i])
    return True


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()
