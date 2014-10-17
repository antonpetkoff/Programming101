
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
