matrix_size = int(input())
the_matrix = []
primary_diagonal_sum = 0
for rows_cols in range(matrix_size):
    current_column = [int(x) for x in input().split()]
    the_matrix.append(current_column)
    primary_diagonal_sum += the_matrix[rows_cols][rows_cols]

print(primary_diagonal_sum)
