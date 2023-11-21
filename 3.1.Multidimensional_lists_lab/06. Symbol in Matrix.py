def matrix_creator(size):
    the_matrix = []
    for the_row in range(size):
        column = list(input())
        the_matrix.append(column)
    return the_matrix


def item_search_func(item, size, the_matrix):
    found = False
    for row in range(size):
        for col in range(size):
            if the_matrix[row][col] == item:
                print(f"({row}, {col})")
                found = True
                break
        if found:
            break
    if not found:
        print(f"{item} does not occur in the matrix")


def main():
    matrix_size = int(input())
    matrix = matrix_creator(matrix_size)
    searched_item = input()
    item_search_func(searched_item, matrix_size, matrix)


main()
