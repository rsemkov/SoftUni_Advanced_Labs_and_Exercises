def matrix_creator(the_rows):
    the_matrix = [[_ for _ in input().split()] for _ in range(the_rows)]
    return the_matrix


def matrix_swap(row1, col1, row2, col2, the_matrix):
    the_matrix[row1][col1], the_matrix[row2][col2] = the_matrix[row2][col2], the_matrix[row1][col1]
    matrix_printer(the_matrix)
    return the_matrix


def input_validity_checker(the_row, the_col, the_input):
    if the_input[0] != "swap" or len(the_input) != 5:
        print("Invalid input!")
        return False
    coordinates_list = list(map(int, the_input[1:]))
    if coordinates_list[0] >= the_row or coordinates_list[2] >= the_row or coordinates_list[1] >= the_col or \
            coordinates_list[3] >= the_col:
        print("Invalid input!")
        return False
    return True


def matrix_printer(the_matrix):
    for item in the_matrix:
        print(" ".join(item))


def main():
    rows, cols = map(int, input().split())
    matrix = matrix_creator(rows)
    while True:
        command = input()
        if command == "END":
            break
        command = command.split()
        if input_validity_checker(rows, cols, command):
            a, b, c, d = map(int, command[1:])
            matrix = matrix_swap(a, b, c, d, matrix)


main()
