rows_cols = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for row in range(rows_cols):
    current_col = [int(x) for x in input().split()]
    matrix.append(current_col)

for primary in range(rows_cols):
    primary_diagonal.append(matrix[primary][primary])

idx = -1
for secondary in range(rows_cols):
    secondary_diagonal.append(matrix[secondary][idx])
    idx -= 1

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)
