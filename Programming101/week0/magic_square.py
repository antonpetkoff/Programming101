
def magic_square(matrix):
    leftDiagonal = 0
    rightDiagonal = 0
    currentColSum = 0
    currentRowSum = 0
    previousColSum = None
    previousRowSum = None

    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            if row == col:
                leftDiagonal += matrix[row][col]
            if row + col == len(matrix) - 1:
                rightDiagonal += matrix[row][col]
            currentColSum += matrix[row][col]
        currentRowSum = sum(matrix[row])

        if currentRowSum != currentColSum:
            return False
        if previousColSum is not None and currentColSum != previousColSum:
            return False
        if previousRowSum is not None and currentRowSum != previousRowSum:
            return False
        currentColSum = 0

    if leftDiagonal != rightDiagonal:
        return False
    return True
