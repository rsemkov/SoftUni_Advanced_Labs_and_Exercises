rows = int(input())
the_matrix = []
for row in range(rows):
    current_column = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    the_matrix.append(current_column)

print(the_matrix)

