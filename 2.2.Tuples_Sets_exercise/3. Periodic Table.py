n = int(input())
elements_set = set()
for _ in range(n):
    current_elements = input().split()
    for element in current_elements:
        elements_set.add(element)

print(*elements_set, sep="\n")
