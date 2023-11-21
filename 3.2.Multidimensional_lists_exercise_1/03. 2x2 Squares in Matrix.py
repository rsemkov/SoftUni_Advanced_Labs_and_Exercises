rows, cols = [int(x) for x in input().split()]
the_matrix = [[_ for _ in input().split()] for _ in range(rows)]
matching_chars_counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if the_matrix[row][col] == the_matrix[row][col + 1] == the_matrix[row + 1][col] == the_matrix[row + 1][col + 1]:
            matching_chars_counter += 1

print(matching_chars_counter)
