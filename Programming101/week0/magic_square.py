
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


def main():
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
                        [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


if __name__ == '__main__':
    main()
