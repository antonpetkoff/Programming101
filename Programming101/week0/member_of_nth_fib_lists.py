
def member_of_nth_fib_lists(listA, listB, needle):
    term = []
    while len(term) < len(needle):
        term = listA + listB
        listA = listB
        listB = term
    if term == needle:
        return True
    return False
