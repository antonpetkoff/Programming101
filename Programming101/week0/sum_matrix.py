
def sum_matrix(m):
    sum = 0
    for row in m:
        for col in row:
            sum += col
    return sum
