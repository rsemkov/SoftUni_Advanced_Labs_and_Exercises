rows, cols = list(map(int, input().split()))

for row in range(rows):
    for col in range(cols):
        print(f"{chr(97 + row)}{chr(97 + col + row)}{chr(97 + row)}", end=" ")
    print()
