def matrix_creator(the_rows):
    the_matrix = []
    for row in range(the_rows):
        current_row = list(map(int, input().split()))
        the_matrix.append(current_row)
    return the_matrix


def columns_sum(the_matrix, the_columns):
    for idx in range(the_columns):
        current_sum = 0
        for item in the_matrix:
            current_sum += item[idx]
        print(current_sum)


def main():
    rows, columns = map(int, input().split(", "))
    matrix = matrix_creator(rows)
    columns_sum(matrix, columns)


main()
