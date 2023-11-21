rows, cols = [int(x) for x in input().split(", ")]
the_matrix = []
biggest_square = ""
biggest_square_elements_sum = 0

for _ in range(rows):
    the_matrix.append([int(x) for x in input().split(", ")])

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        a, b, c, d = the_matrix[row][col], the_matrix[row][col + 1], the_matrix[row + 1][col], the_matrix[row + 1][col + 1]
        current_sum = a + b + c + d
        if current_sum > biggest_square_elements_sum:
            biggest_square_elements_sum = current_sum
            biggest_square = f"{a} {b}\n{c} {d}"

print(f"{biggest_square}\n{biggest_square_elements_sum}")
