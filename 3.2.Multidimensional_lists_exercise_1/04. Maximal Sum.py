rows, cols = [int(x) for x in input().split()]
the_matrix = [[int(y) for y in input().split()] for _ in range(rows)]
biggest_square = ""
biggest_square_elements_sum = 0

for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        a, b, c, d, e, f, g, h, i = the_matrix[row][col], the_matrix[row][col + 1], the_matrix[row][col + 2],\
                                    the_matrix[row + 1][col], the_matrix[row + 1][col + 1], the_matrix[row + 1][col + 2],\
                                    the_matrix[row + 2][col], the_matrix[row + 2][col + 1], the_matrix[row + 2][col + 2]
        current_sum = a + b + c + d + e + f + g + h + i
        if current_sum >= biggest_square_elements_sum:
            biggest_square_elements_sum = current_sum
            biggest_square = f"{a} {b} {c}\n{d} {e} {f}\n{g} {h} {i}"

print(f"Sum = {biggest_square_elements_sum}\n{biggest_square}")
