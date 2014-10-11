
def member_of_nth_fib_lists(listA, listB, needle):
    term = []
    while len(term) < len(needle):
        term = listA + listB
        listA = listB
        listB = term
    if term == needle:
        return True
    return False


def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    print(member_of_nth_fib_lists([1, 2], [3, 4],
                                  [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
    print(member_of_nth_fib_lists([7, 11], [2],
                                  [7, 11, 2, 2, 7, 11, 2]))
    print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))


if __name__ == '__main__':
    main()
