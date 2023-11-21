names_count = int(input())
names_set = {input() for _ in range(names_count)}
print(*names_set, sep="\n")
