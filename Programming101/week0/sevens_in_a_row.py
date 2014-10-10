
def sevens_in_a_row(arr, n):
    goal = n
    sevensCount = 0
    for number in arr:
        if number == 7:
            sevensCount += 1
        else:
            sevensCount = 0
        if sevensCount == goal:
            return True
    return False
