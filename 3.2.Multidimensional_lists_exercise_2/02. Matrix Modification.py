def add_matrix(the_matrix, the_row, the_col, the_value):
    the_matrix[the_row][the_col] += the_value
    return the_matrix


def subtract_matrix(the_matrix, the_row, the_col, the_value):
    the_matrix[the_row][the_col] -= the_value
    return the_matrix


def print_matrix(the_matrix):
    for el in the_matrix:
        print(*el, sep=" ")


def main():
    rows_count = int(input())
    matrix = [[int(_) for _ in input().split()] for _ in range(rows_count)]
    while True:
        command = input()
        if command == "END":
            break
        command = command.split()
        action = command[0]
        row_coord, col_coord, value = list(map(int, command[1:]))

        if (row_coord < 0 or row_coord >= rows_count) or (col_coord < 0 or col_coord >= len(matrix[0])):
            print("Invalid coordinates")
            continue

        if action == "Add":
            matrix = add_matrix(matrix, row_coord, col_coord, value)
        elif action == "Subtract":
            matrix = subtract_matrix(matrix, row_coord, col_coord, value)

    print_matrix(matrix)


main()
