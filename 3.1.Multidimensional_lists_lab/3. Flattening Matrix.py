rows = int(input())

result = []
for row in range(rows):
    current_row = list(map(int, input().split(", ")))
    for item in current_row:
        result.append(item)

print(result)
