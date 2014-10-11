
def get_subgrid(source, start, stop):
    subgrid = []
    for i in range(3):
        subgrid.append(source[i][start:stop])
    return subgrid


def check_subgrid(subgrid):
    n = len(subgrid)
    numbers = set()
    for row in range(n):
        for col in range(n):
            numbers.add(subgrid[row][col])
    if len(numbers) != 9:
        return False
    return True


def sudoku_solved(sudoku):
    n = len(sudoku)
    rowSets = [set() for i in range(n)]
    colSets = [set() for i in range(n)]
    for row in range(n):
        for col in range(n):
            rowSets[row].add(sudoku[row][col])
            colSets[col].add(sudoku[row][col])

    for i in range(n):
        if len(rowSets[i]) != 9 or len(colSets[i]) != 9:
            return False

    # check subgrids
    for row in range(3, 10, 3):
        tempGrid = sudoku[row-3:row]
        for col in range(3, 10, 3):
            if not check_subgrid(get_subgrid(tempGrid, col-3, col)):
                return False

    return True


def main():
    print(sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4, 8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5, 2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))
    print(sudoku_solved([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))


if __name__ == '__main__':
    main()

