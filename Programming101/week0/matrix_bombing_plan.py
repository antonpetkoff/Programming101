from sum_matrix import sum_matrix
import copy


def handle_neighbour(m, (x, y), bomb):
    if x >= 0 and x < len(m[0]) and y >= 0 and y < len(m):
        if m[y][x] >= bomb:
            m[y][x] -= bomb
        else:
            m[y][x] = 0


def blow_bomb(m, (x, y)):
    bomb = m[y][x]
    for x_pos in range(x-1, x+2):
        for y_pos in range(y-1, y+2):
            if not (x_pos == x and y_pos == y):
                handle_neighbour(m, (x_pos, y_pos), bomb)
    return sum_matrix(m)


def matrix_bombing_plan(m):
    result = {}
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            matrix = copy.deepcopy(m)
            result[(y, x)] = blow_bomb(matrix, (x, y))
    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(m))
    m2 = [[4,8,3], [5,2,7], [3, 9, 6]]
    print(matrix_bombing_plan(m2))

if __name__ == '__main__':
    main()
