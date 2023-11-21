matrix_size = int(input())
the_matrix = [[_ for _ in input().split(", ")] for _ in range(matrix_size)]
primary_diagonal = []
secondary_diagonal = []

for idx in range(matrix_size):
    primary_diagonal.append(the_matrix[idx][idx])

counter = matrix_size - 1
for idx_2 in range(len(the_matrix)):
    secondary_diagonal.append(the_matrix[idx_2][counter])
    counter -= 1

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(list(map (int, primary_diagonal)))}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(list(map (int, secondary_diagonal)))}")
