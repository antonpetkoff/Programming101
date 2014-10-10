
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
