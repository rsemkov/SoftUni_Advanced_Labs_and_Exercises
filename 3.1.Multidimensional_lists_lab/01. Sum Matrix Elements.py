rows, columns = list(map(int, (input().split(", "))))
the_matrix = []
total_sum = 0
for row in range(rows):
    current_column = list(map(int, (input().split(", "))))
    the_matrix.append(current_column)
    total_sum += sum(current_column)

print(total_sum)
print(the_matrix)
