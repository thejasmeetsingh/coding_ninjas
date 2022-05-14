def is_safe_sub_grid(grid, row, col, num):
    _row = row - (row % 3)
    _col = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if grid[i + _row][j + _col] == num:
                return False
    return True


def is_safe_horizontal(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
    return True


def is_safe_vertical(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
    return True


def is_safe_position(grid, row, col, num):
    return is_safe_vertical(grid, col, num) and is_safe_horizontal(grid, row, num) and is_safe_sub_grid(grid, row, col,
                                                                                                        num)


def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None


def sudoku_solver(grid):
    row, col = find_empty_location(grid)

    if row is None:
        return True

    for num in range(1, 10):
        if is_safe_position(grid, row, col, num):
            grid[row][col] = num
            if sudoku_solver(grid):
                return True
            grid[row][col] = 0

    return False


if __name__ == "__main__":
    grid = []

    for _ in range(9):
        grid.append(list(map(int, input().split())))

    print('true' if sudoku_solver(grid) else 'false')
