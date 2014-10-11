
def nth_fib_lists(listA, listB, n):
    if n < 1 or len(listA) == 0 and len(listB) == 0:
        return []
    elif n == 1:
        return listA
    elif n == 2:
        return listB
    term = []
    for i in range(n - 2):
        term = listA + listB
        listA = listB
        listB = term
    return term


def main():
    print(nth_fib_lists([1], [2], 1))
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1, 2], [1, 3], 3))
    print(nth_fib_lists([], [1, 2, 3], 4))
    print(nth_fib_lists([], [], 100))


if __name__ == '__main__':
    main()
