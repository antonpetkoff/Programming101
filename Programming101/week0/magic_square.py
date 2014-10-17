
def magic_square(matrix):
    n = len(matrix)
    leftDiagonal = 0
    rightDiagonal = 0
    rowSums = [0 for i in range(n)]
    colSums = [0 for i in range(n)]

    for row in range(n):
        for col in range(n):
            if row == col:
                leftDiagonal += matrix[row][col]
            if row + col == len(matrix) - 1:
                rightDiagonal += matrix[row][col]
            colSums[col] += matrix[row][col]
        rowSums[row] = sum(matrix[row])

    if leftDiagonal != rightDiagonal:
        return False

    sums = rowSums + colSums
    for i in range(1, len(sums)):
        if sums[i-1] != sums[i]:
            return False

    return True
